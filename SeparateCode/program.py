def main():

    print("Stock Data Visualizer\n-------------------------\n")
    stock=input("Enter the stock symbol you are looking for: ")
    user_choice()
    time()
    date()

def user_choice():
    print("\nChart Types\n---------------------\n")
    options = ['1. Bar', '2. Line']
    user_input = ''
    input_message = "Pick an option:\n"

    for index, item in enumerate(options):
        input_message += f'{index+1}) {item}\n'

    input_message += 'Your choice: '

    while user_input not in map(str, range(1, len(options) + 1)):
        user_input = input(input_message)
            
    print('You picked: ' + options[int(user_input) - 1])



def time():
    print("Select the time series of the chart you want to generate: \n--------------\n")

    while True:
        choice = input("1. Intraday\n2. Daily\n3. Weekly\n4. Monthly\nPick an option: ")
        choice = int(choice)

        if choice < 1 or choice > 4:
            print("Input must be an integer 1-4")
        else:
            break

    print("You chose " + str(choice))

def date():
    startDate = input("(Enter The start date yyyy-mm-dd) ")
    endDate = input("(Enter the end date yyyy-mm-dd) ")

    while input("Would you like to view more stock Data? Press 'y' to continue.") == 'y':
        main()
   




if __name__ == "__main__":
    main()





  

