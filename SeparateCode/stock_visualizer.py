def main():
    print('\nStock Visualizer\n')
    print('------------------\n')
    stockSymbol = stock_symbol()
    chartType = chart_type()
    timeSeries = time_series()

    print("Chart type: " + str(chartType))
    print("Time series: " + str(timeSeries))
    print("Stock: " + stockSymbol)

def stock_symbol():
    while True:
        stock = input("Enter the stock symbol you are looking for: ")
        if stock.isalpha() and len(stock) <= 5 and len(stock) > 0:
            break
        else:
            print("Stock must be alphabetic and up to 5 characters.")
            continue
    return stock

def chart_type():

    print('Select 1 or 2 for Chart Type\n')
    print('1. Bar')
    print('2. Line')

    while True:
        graph_type = int(input('Your selection: '))
        if graph_type == 1 or graph_type == 2:
            break
        else:
            print("Please enter a valid input")
            continue
    return graph_type

def time_series():
    print('Select the Time Series of the Chart You Wish to Generate\n')
    print('----------------------------------------------------------\n')
    print('Select 1 or 2 for Chart Type\n')
    print('1. Intraday')
    print('2. Daily')
    print('3. Weekly')
    print('4. Monthly')

    while True:
        time_type = int(input('Your selection: '))
        if time_type >= 1 and time_type <= 4:
            break
        else:
            print("Please enter a valid input")
            continue
    return time_type
main()
