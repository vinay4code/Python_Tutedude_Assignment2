#Check if veven or odd
def check_even_odd(number):
    try:
        number = int(number)
    except ValueError:
        return "Invalid input. Please enter a valid integer."
    # Check if the number is even or odd
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
number = input("Enter a number: ")
print(f"{number} is an {check_even_odd(number)} number.")