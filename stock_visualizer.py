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
        print('Success!')
    elif graph_type == 2:
        print('Success!')
    else: print("Please enter a valid input")

    print()
    menu()
    graph_type = int(input(''))

