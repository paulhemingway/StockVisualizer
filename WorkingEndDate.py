import datetime
from datetime import date
from time import strftime

# While statement to loop until correct value is entered
while (True):
    try:
        begin_date = datetime.datetime.strptime(
            input("Please enter the beginning date (YYYY-MM-DD): "), '%Y-%m-%d')
    except ValueError:
        print("Incorrect data format, should be YYYY-MM-DD")
        # continue
    else:
        break

# this block is for the end date and has error checks so it cannot be after today
while (True):
    try:
        end_date = datetime.datetime.strptime(
            input("Please enter the end date (YYYY-MM-DD): "), '%Y-%m-%d')

        # converts end date to a string to compare to todays date as number
        compare_end = str(end_date).replace('-', '')
        compare_beginning = str(begin_date).replace('-', '')
        begin_output = str(begin_date.strftime("%Y-%m-%d"))
        end_output = str(end_date.strftime("%Y-%m-%d"))

        # adds a leading 0 to days to compare to begin date if not included already. datetime already adds leading zero to month
        if (len(compare_beginning) < 8):
            slice = 6
            new = compare_beginning[:slice] + "0" + compare_beginning[slice:]
            compare_beginning = new
            
        if (len(compare_end) < 8):
            slice = 6
            new = compare_end[:slice] + "0" + compare_end[slice:]
            compare_end = new
            
        if (compare_end < compare_beginning):
            print("End date cannot be after begin date")
            continue
        
    except ValueError:
        print("Incorrect data format, should be YYYY-MM-DD")
    else:
        break
print(begin_output)
print(end_output)

