import datetime
from datetime import date

while (True):
    try:
        beginning_date = datetime.datetime.strptime(
            input("Please enter the beginning date (YYYY-MM-DD): "), '%Y-%m-%d')
    except ValueError:
        print("Incorrect data format, should be YYYY-MM-DD")
        # continue
    else:
        break

while (True):
    try:
        end_date = datetime.datetime.strptime(
            input("Please enter the end date (YYYY-MM-DD): "), '%Y-%m-%d')
        #end_date = '2022-10-16'
        end = str(end_date).replace('-', '')
        API_end_date = str(end_date.strftime("%Y-%m-%d"))
        today = date.today().strftime("%Y%m%d")
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
print(API_end_date)
