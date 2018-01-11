
#This program returns the number of digits in a given number
def digitCount(val):
    numDigits = 1
    while (val/10) > 0:
        numDigits += 1
        val /= 10
    return numDigits

#Get input from the user by stdin
val = int(input("Enter a number: "))

#call function and print result
print(digitCount(val))