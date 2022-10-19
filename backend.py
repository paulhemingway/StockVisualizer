import requests
import datetime
from lxml import etree
import pygal

symbol = "GOOGL"
chartType = "line"
timeSeries = "TIME_SERIES_DAILY"
apiKey = "33451WDSYYNTOXAH"

beginning = "2021-03-22"
end = "2021-08-16"

chartOpen = []
chartHigh = []
chartLow = []
chartClose = []

print(beginning[0:4])

beginningDate = datetime.datetime(int(beginning[0:4]), int(beginning[5:7]), int(beginning[9:11]))
endDate = datetime.datetime(int(end[0:4]), int(end[5:7]), int(end[9:11]))

apiURL = "https://www.alphavantage.co/query?function=" + timeSeries + "&symbol=" + symbol + "&outputsize=full&apikey=" + apiKey

r = requests.get(apiURL)
data = r.json()


## compare dates with datetime

for entry in data["Time Series (Daily)"]:
    
    entryDate = datetime.datetime(int(entry[0:4]), int(entry[5:7]), int(entry[8:10]))
    if(entryDate >= beginningDate and entryDate <= endDate):
        entryObject = data["Time Series (Daily)"][entry]

        chartOpen.append(float(entryObject["1. open"]))
        chartHigh.append(float(entryObject["2. high"]))
        chartLow.append(float(entryObject["3. low"]))
        chartClose.append(float(entryObject["4. close"]))


line_chart = pygal.Line()
line_chart.title = 'Stonks'
line_chart.x_labels = map(str, range(beginningDate.day, endDate.day))
line_chart.add('Open', chartOpen)
line_chart.add('High',  chartHigh)
line_chart.add('Low',      chartLow)
line_chart.add('Close',  chartClose)
line_chart.render_in_browser()
        
