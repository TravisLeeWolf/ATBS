# Define the function
def collatz(number):
    # Using mod 2 to find if it is odd or even we can split the cases
    if number % 2 == 0:
        answer = number // 2
    else:
        answer = 3 * number + 1
    return answer

print('Let us use the collatz function.')
print('Type a number that is odd or even.')
# Get user input
# Run collatz() until the answer is 1
try:
    userNum = int(input())
    check = collatz(userNum)
    print(check)
    while check != 1:
        check = collatz(check)
        print(check)
except ValueError:
    print('Please type in a positive integer value.')
