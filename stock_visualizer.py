def menu():
    print('Stock Visualizer\n')
    print('------------------\n')
    print('Select 1 or 2 for Chart Type\n')
    print('1. Bar')
    print('2. Line')

menu()
graph_type = int(input(''))

while graph_type != 0:
    if graph_type == 1:
        print('You chose', graph_type)
    elif graph_type == 2:
        print('You chose', graph_type)
    else: print("Please enter a valid input")
    
    print()
    menu()
    graph_type = int(input(''))

def time_series():
    print('Select the Time Series of the Chart You Wish to Generate\n')
    print('----------------------------------------------------------\n')
    print('Select 1 or 2 for Chart Type\n')
    print('1. Intraday')
    print('2. Daily')
    print('3. Weekly')
    print('4. Monthly')

time_series()
time_type = int(input(''))

while time_type != 0:
    if time_type == 1:
        print('Success!')
    elif time_type == 2:
        print('Success!')
    elif time_type == 3:
        print('Success!')
    elif time_type == 4:
        print('You chose', time_type)
    else: print("Please enter a valid input")

    menu()
    time_type = int(input(''))