# Calculator
# simple Python for calculator operations

def display_welcome():
    """Display welcome message and instructions"""
    print("=" * 50)
    print("🧮 BASIC CALCULATOR PROGRAM")
    print("=" * 50)
    print("This program performs basic arithmetic operations.")
    print("Supported operations: +, -, *, /")
    print("-" * 50)

def get_number(prompt):
    """Get a valid number from user input"""
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("❌ Error: Please enter a valid number!")

def get_operation():
    """Get a valid operation from user input"""
    valid_operations = ['+', '-', '*', '/']
    
    while True:
        operation = input("Enter operation (+, -, *, /): ").strip()
        
        if operation in valid_operations:
            return operation
        else:
            print("❌ Error: Please enter a valid operation (+, -, *, /)")

def perform_calculation(num1, num2, operation):
    """Perform the calculation based on the operation"""
    if operation == '+':
        result = num1 + num2
        operation_name = "Addition"
    elif operation == '-':
        result = num1 - num2
        operation_name = "Subtraction"
    elif operation == '*':
        result = num1 * num2
        operation_name = "Multiplication"
    elif operation == '/':
        if num2 == 0:
            return None, "Division by zero error"
        result = num1 / num2
        operation_name = "Division"
    
    return result, operation_name

def display_result(num1, num2, operation, result, operation_name):
    """Display the calculation result in a formatted way"""
    print("\n" + "=" * 40)
    print("📊 CALCULATION RESULT")
    print("=" * 40)
    print(f"Operation: {operation_name}")
    print(f"Calculation: {num1} {operation} {num2} = {result}")
    
    # Format result based on whether it's a whole number
    if isinstance(result, float) and result.is_integer():
        print(f"Final Answer: {int(result)}")
    else:
        print(f"Final Answer: {result:.2f}")
    print("=" * 40)

def ask_continue():
    """Ask user if they want to perform another calculation"""
    while True:
        choice = input("\nWould you like to perform another calculation? (y/n): ").lower().strip()
        if choice in ['y', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False
        else:
            print("Please enter 'y' for yes or 'n' for no.")

def main():
    """Main program function"""
    display_welcome()
    
    while True:
        try:
            # Get user inputs
            print("\n📝 Enter your calculation details:")
            num1 = get_number("Enter the first number: ")
            num2 = get_number("Enter the second number: ")
            operation = get_operation()
            
            # Perform calculation
            result, operation_name = perform_calculation(num1, num2, operation)
            
            # Check for division by zero error
            if result is None:
                print(f"\n❌ Error: {operation_name}")
                print("Cannot divide by zero! Please try again.")
                continue
            
            # Display result
            display_result(num1, num2, operation, result, operation_name)
            
            # Ask if user wants to continue
            if not ask_continue():
                break
                
        except KeyboardInterrupt:
            print("\n\n👋 Program interrupted by user. Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ An unexpected error occurred: {e}")
            print("Please try again.")
    
    print("\n🎉 Thank you for using the Basic Calculator!")
    print("Calculator program ended.")

# en example
def run_examples():
    """Demonstrate the calculator with examples"""
    print("\n" + "=" * 50)
    print("📚 EXAMPLE CALCULATIONS")
    print("=" * 50)
    
    # calculations
    examples = [
        (10, 5, '+'),
        (20, 8, '-'),
        (7, 3, '*'),
        (15, 3, '/'),
        (10, 0, '/'),  # Division by zero example
    ]
    
    for num1, num2, op in examples:
        result, op_name = perform_calculation(num1, num2, op)
        
        if result is None:
            print(f"{num1} {op} {num2} = Error: {op_name}")
        else:
            if isinstance(result, float) and result.is_integer():
                print(f"{num1} {op} {num2} = {int(result)}")
            else:
                print(f"{num1} {op} {num2} = {result:.2f}")

# Run the program
if __name__ == "__main__":

    
    
    # Run the main calculator program
    main()