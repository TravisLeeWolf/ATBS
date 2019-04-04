# Define the function
def collatz(number):
    # Add a variable to return
    answer = 0

    if number ==1 :
        print("done")
        return 0
    # Using mod 2 to find if it is odd or even we can split the cases
    if number % 2 == 0:
        answer = number // 2
        print(answer)
        collatz(answer)
    else:
        answer = 3 * number + 1
        print(answer)
        collatz(answer)
    return answer




# Get user input
print('Let us use the collatz function.')
print('Type a number that is odd or even.')
# Here it has to run collatz() until the answer is 1
try:
    userNum = int(input())
    collatz(userNum)

except ValueError:
    print('Please type in a positive integer value.')

# Call the function
