# Your task is to write a Python program to convert month name to a number of days. 
# >Hint: Print list of months at the beginning.  

# User should be prompted to enter name of the month and the output shoul be the number of days in given month.

months = {
    "January": 31,
    "February": 28,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
}

print("List of months:", ", ".join(months.keys()))
# join expects a sequence of strings to concatenate. So i print only keys and values (integer)

while True:
    month_input = input("Input the name of Month: ")
    month_name = month_input.capitalize()

    if month_name in months:
        days = months[month_name]
        print("Number of days:", days, "days")
        break  
    else:
        print("Invalid month name. Please try again.")
