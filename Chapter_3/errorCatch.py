def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Cannot divide by 0.')

print('This function divides 42 by a chosen number.')
print('Type any integer number')
number = int(input())
print(spam(number))