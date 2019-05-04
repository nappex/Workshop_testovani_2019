def fizzbuzz(number):
    if number % 5 == 0 and number % 3 == 0:
        return "fizzbuzz"
    elif number % 5 == 0:
        return "buzz"
    elif number % 3 == 0:
        return "fizz"

    return number
