import requests
import datetime
from lxml import etree
import pygal

def reverseLists():
    chartOpen.reverse()
    chartHigh.reverse()
    chartLow.reverse()
    chartClose.reverse()
    chartDates.reverse()

symbol = "GOOGL"
chartType = "line"
timeSeries = "TIME_SERIES_MONTHLY"
apiKey = "33451WDSYYNTOXAH"

beginning = "2021-03-22"
end = "2022-01-16"

chartOpen = []
chartHigh = []
chartLow = []
chartClose = []
chartDates = []

print(beginning[0:4])

beginningDate = datetime.datetime(int(beginning[0:4]), int(beginning[5:7]), int(beginning[9:11]))
endDate = datetime.datetime(int(end[0:4]), int(end[5:7]), int(end[9:11]))

apiURL = "https://www.alphavantage.co/query?function=" + timeSeries + "&symbol=" + symbol + "&outputsize=full&apikey=" + apiKey

r = requests.get(apiURL)
data = r.json()


## compare dates with datetime

for entry in data["Monthly Time Series"]:
    
    entryDate = datetime.datetime(int(entry[0:4]), int(entry[5:7]), int(entry[8:10]))
    if(entryDate >= beginningDate and entryDate <= endDate):
        entryObject = data["Monthly Time Series"][entry]

        chartOpen.append(float(entryObject["1. open"]))
        chartHigh.append(float(entryObject["2. high"]))
        chartLow.append(float(entryObject["3. low"]))
        chartClose.append(float(entryObject["4. close"]))
        chartDates.append(entry)


reverseLists()

line_chart = pygal.Line()
line_chart.title = 'Stock Data for ' + symbol + ": " + beginning + " to " +  end
line_chart.x_labels = chartDates
line_chart.add('Open', chartOpen)
line_chart.add('High',  chartHigh)
line_chart.add('Low',      chartLow)
line_chart.add('Close',  chartClose)
line_chart.render_in_browser()
        


