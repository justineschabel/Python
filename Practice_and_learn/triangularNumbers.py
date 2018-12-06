#This program calculates the number of objects in an equilateral triangle with "numRows" rows


def numBalls(numRows):
    count = 0
    for i in range(1,numRows + 1, 1):
        count+= i
    return count

#get numRows from user by stdin
numRows = int(input("Enter number of rows to calculate number of balls total: "))

#call function and print result
print (numBalls(numRows))

