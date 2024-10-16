# Carlos Polanco
# This program uses a recursive function to convert a base 10 number 
# into a base 2 number

# base conversion function
def baseChange(n):
    if n == 0:
        # empty string so there is no leading 0
        # if I return '0', there would be a leading 0
        return ''
    else:
        # recursive function using remainder method
        return baseChange(n // 2) + str(n % 2)

# function to print the program heading
def printHeading():
     print("Carlos Polanco")
     print("This program uses a recursive function to convert") 
     print("a base 10 number into a base 2 number \n")


# endProg is the sentinel value
# num initialized to 0 so that the loop can be entered
# without having to enter a number twice
endProg = -1
num = 0

# calling function to print heading
printHeading()

# loop to keep asking for numbers to convert
while num != endProg:
        
        num = int(input("Please enter a positive number (-1 to exit): "))
        
        # if number entered is -1 then just print a goodbye message and exit
        if num == -1:
            print("Goodbye!")
        
        # if number is 0 then just print 0 = 0
        elif num == 0:
            print(f"{num} = {num}")

        # if number is negative, run the loop again
        elif num < 0:
            print("Try again, no negative numbers")
        
        # any other number, call the baseChange function and print the result.
        else:
            print(f"{num} = {baseChange(num)}")
