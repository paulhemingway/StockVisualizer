import datetime
from datetime import date
from time import strftime

# While statement to loop until correct value is entered
while (True):
    try:
        beginning_date = datetime.datetime.strptime(
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
        end = str(end_date).replace('-', '')
        end_output = str(end_date.strftime("%Y-%m-%d"))
        today = date.today().strftime("%Y%m%d")

        # adds a leading 0 to days to compare to today's date if not included already. datetime already adds leading zero to month
        if (len(end) < 8):
            slice = 6
            new = end[:slice] + "0" + end[slice:]
            end = new

        if (end > today):
            print("Date cannot be after current date")
            continue
    except ValueError:
        print("Incorrect data format, should be YYYY-MM-DD")
    else:
        break
print(end_output)
