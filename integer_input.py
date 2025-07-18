user_integer = int(input("Please enter an integer with atleast 3 digits : "))

if (user_integer < -99) or (user_integer > 99):
    digit_tens = (abs(user_integer) % 100) // 10
    print("Digit in the tens position is {}.".format(digit_tens))
else:
    print("Error: {} has less than three digits.".format(user_integer))