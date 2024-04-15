def valid_int(question, mini, maxi):
    x = int(input(question))
    while x < mini or x > maxi:
        x = int(input(question))
    return x


def factorial(num):
    """
    Calculate to factorial:
    :param num:
    :return:
    """
    fact = 1
    if num == 0:
        return fact
    for i in range(1, num + 1, 1):  # or for i in range(1, num+1, -1). num + 1 because it's always minus a number
        fact *= i  # fact = fact * i
    return fact  # if num != 0


x = valid_int("Enter a value to calculate the factorial: ", 0, 99999)
print("Factorial of {}! = {}".format(x, factorial(x)))
print()
