import datetime
from time import strftime
import requests
import pygal

timeSeriesTypes = ["INTRADAY", "DAILY_ADJUSTED", "WEEKLY", "MONTHLY"]
timeSeriesURL = ['Time Series (60min)', 'Time Series (Daily)', 'Weekly Time Series', 'Monthly Time Series']
apiKey = "33451WDSYYNTOXAH"

chartLists = {
    'chartOpen': [],
    'chartHigh': [],
    'chartLow': [],
    'chartClose': [],
    'chartDates': [],
}

def main():
    while True:
       
        emptyLists()
        print("Stock Data Visualizer\n-------------------------\n")

        stockSymbol = stock_symbol().upper()
        chartType = chart_type()
        timeSeriesValue = time_series()-1
        timeSeries = timeSeriesTypes[timeSeriesValue]
        timeSeriesProp = timeSeriesURL[timeSeriesValue]
        
        dates = get_dates()
        
        data = callAPI(stockSymbol, timeSeries)

        fillLists(data, dates, timeSeriesProp)
        reverseLists()
        renderChart(stockSymbol, dates, chartType)

        choice = input("Would you like to display another chart? (Y/N): ")
        if choice.upper() != "Y":
            break

def stock_symbol():
    stock=input("Enter the stock symbol you are looking for: ")

    # checks if stock is alphabetic and no more than 7 characters
    if stock.isalpha() and len(stock) <= 7:
        return stock
    else:
        print("Stock symbol must be alphabetic and 1-7 characters.")
        return 'NA'

def chart_type():
    print('Select 1 or 2 for Chart Type\n')
    print('1. Line')
    print('2. Bar')

    try:
        graph_type = int(input('Your selection: '))
        if graph_type == 1 or graph_type == 2:
          return graph_type
        else:
            raise ValueError
    except ValueError:
        print("Input must be a 1 or 2")
        

def time_series():
    print('Select the Time Series of the Chart You Wish to Generate\n')
    print('----------------------------------------------------------\n')
    print('1. Intraday')
    print('2. Daily')
    print('3. Weekly')
    print('4. Monthly')
    try:
        time_type = int(input('Your selection: '))
        if time_type >= 1 and time_type <= 4:
          return time_type
        else:
            print("Input must be an integer 1-4.")
    except ValueError:
        print("Input must be an integer 1-4.")
    return 0

def get_dates():
    # While statement to loop until correct value is entered
    
    try:
        start = datetime.datetime.strptime(
            input("Please enter the start date (YYYY-MM-DD): "), '%Y-%m-%d')
    except ValueError:
        print("Incorrect data format, should be YYYY-MM-DD")
        return
        # continue
        
    
    try:
        end = datetime.datetime.strptime(input("Please enter the end date (YYYY-MM-DD): "), '%Y-%m-%d')
        if(start >= end):
            print("End date must be AFTER the start date!")
    except ValueError:
        print("Invalid date, should be YYYY-MM-DD")
        return

    dates = [start, end]
    return dates

def callAPI(symbol, timeSeries):
    interval = '&interval=60min' if timeSeries == "INTRADAY" else ''
    apiURL = "https://www.alphavantage.co/query?function=" + "TIME_SERIES_" + timeSeries + "&symbol=" + symbol + interval + "&outputsize=full&apikey=" + apiKey
    print(apiURL)
    r = requests.get(apiURL)
    data = r.json()
    return data

def fillLists(data, dates, timeSeriesProp):
    try:
        for entry in data[timeSeriesProp]:
            entryDate = datetime.datetime(int(entry[0:4]), int(entry[5:7]), int(entry[8:10]))
            if(entryDate >= dates[0] and entryDate <= dates[1]):
                entryObject = data[timeSeriesProp][entry]
                chartLists['chartOpen'].append(float(entryObject["1. open"]))
                chartLists['chartHigh'].append(float(entryObject["2. high"]))
                chartLists['chartLow'].append(float(entryObject["3. low"]))
                chartLists['chartClose'].append(float(entryObject["4. close"]))
                chartLists['chartDates'].append(entry)
    except KeyError:
        print("No data for the stock was found.")
        exit()

def reverseLists():
    chartLists['chartOpen'].reverse()
    chartLists['chartHigh'].reverse()
    chartLists['chartLow'].reverse()
    chartLists['chartClose'].reverse()
    chartLists['chartDates'].reverse()

def emptyLists():
    chartLists['chartOpen'].clear()
    chartLists['chartHigh'].clear()
    chartLists['chartLow'].clear()
    chartLists['chartClose'].clear()
    chartLists['chartDates'].clear()

def renderChart(symbol, dates, chartType):
    chart = pygal.Line(x_label_rotation=65) if chartType ==1 else pygal.Bar(x_label_rotation=65)
    chart.title = 'Stock Data for ' + symbol + ": " + str(dates[0])[0:10] + " to " +  str(dates[1])[0:10]
    chart.x_labels = chartLists['chartDates']
    chart.add('Open', chartLists['chartOpen'])
    chart.add('High',  chartLists['chartHigh'])
    chart.add('Low',      chartLists['chartLow'])
    chart.add('Close',  chartLists['chartClose'])
    if(len(chartLists['chartClose']) == 0):
        print("No data was received for your inputs!")
        return
    chart.render_in_browser()
#main()