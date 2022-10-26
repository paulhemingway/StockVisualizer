def chart_type():
    print('Select 1 or 2 for Chart Type\n')
    print('1. Bar')
    print('2. Line')


def time_series():
    print('Select the Time Series of the Chart You Wish to Generate\n')
    print('----------------------------------------------------------\n')
    print('Select 1-4 for Time series\n')
    print('1. Intraday')
    print('2. Daily')
    print('3. Weekly')
    print('4. Monthly')

while True:
    menu=int(input('Select an option\n (1) Chart Type\n (2) Time Series'))
    if menu == 1:
        chart_type()
    elif menu == 2:
        time_series
   