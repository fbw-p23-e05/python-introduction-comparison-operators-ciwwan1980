# Your task is to write a program which asks the user three times about two integer numbers to compare. 
# >Hint: Use `while` loop to perform the same operation more than once!  

# Use both comparison and logical operators, for example use logical comparison between two or more comparion operators: 

count = 0

while count < 3:
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
    
    print("Comparisons for pair", count + 1, ":")
    
    if first_number == second_number:
        print("Numbers are equal")
    else:
        print("Numbers are not equal")
    
    if first_number < second_number:
        print("First number is less than second number")
    else:
        print("First number is not less than second number")
    
    if first_number > 0 and second_number > 0:
        print("Both numbers are positive")
    else:
        print("At least one number is not positive")
    
    count += 1
