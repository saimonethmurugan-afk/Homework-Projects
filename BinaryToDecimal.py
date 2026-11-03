#This program converts any binary number inputted by the user to a standard decimal number.

binary = input("Please enter a binary number: ")

decimal = 0

#Converting the binary number to decimal
for digit in binary:
    decimal  = decimal * 2 + int(digit) 

print(f"The decimal equivalent is: {decimal}.")
