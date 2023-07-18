import time

def main():
    print("Hello....!")
    print("This is a simple console calculator")
    time.sleep(1.5)

def two_inputs():
    user_input = input("Enter a number: ")
    second_user_input = input("Enter a second number: ")
    try:
        parsed_input_one = int(user_input)
        parsed_input_two = int(second_user_input)
    except ValueError:
        try:
            parsed_input_one = float(user_input)
            parsed_input_two = float(second_user_input)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            exit()

    return parsed_input_one, parsed_input_two

def perform_operation(operator, input_one, input_two):
    if operator == '+':
        return input_one + input_two
    elif operator == '-':
        return input_one - input_two
    elif operator == '*':
        return input_one * input_two
    elif operator == '/':
        if input_two != 0:
            return input_one / input_two
        else:
            print("Error: Division by zero!")
            exit()
    else:
        print("Invalid operator.")
        exit()


main()

parsed_input_one, parsed_input_two = two_inputs()

operator = input("What operation would you like to perform? (+, -, *, /): ")

result = perform_operation(operator, parsed_input_one, parsed_input_two)

print("Result:", result)
