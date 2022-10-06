"""
    Steps  to Solve the Challenge
    1. Create a List of Possible Operation
    2. If the input is in the List Created Pass else request the User to enter an input again
    3. Create a List to Store Number to perform Operation.
    4. A While Loop to keep requesting for an Integer and Once the User Enter Ok we break out from the Loop to perform the Operation
    5. Sort the List in Reverse order to make the Largest Number come First
    5. A For loop to loop through the Sorted List and store the result
    6. Print out the Result
"""

def solve(a, b, sign):
    """_summary_

    Args:
        a (int): An Integer
        b (int): An Integer
        sign (str): Mathematical Sign

    Returns:
        int: Return the Result after performing the Operation
    """
    if sign == "+":
        return a + b
    elif sign == "-":
        return a-b
    elif sign == "*":
        return a*b
    else:
        return a/b

def calculator():
    symbol = "+ - / *"
    print(f"Welcome to use this calculator\nOperation to Perform {symbol}\n")
    operation = ["+", "-", "/", "*"]
    val = False
    while val == False:
        operation_input = input(f"Enter a Valid Operation {symbol}: ")
        if operation_input in operation:
            val = True
            
    num_list = []
    print("\nTo Perform an operation enter an Integer and to perform an operation Enter Ok")
    bool_val = False
    while bool_val == False:
        num = input("Enter a number: ")
        try:
            if num.upper() == "OK" and len(num_list) > 1:
                bool_val = True
            elif float(num) > 0:
                num_list.append(float(num))
            else:
                print("Enter a Valid Input")
        except ValueError:
            print("Enter a Valid Input")
    
    num_list_sorted = sorted(num_list, reverse=True)
    first_index = num_list_sorted[0]
    result = 0
    for i in range(len(num_list)):
        if i == 0:
            result = num_list_sorted[i]
        else:
            result = solve(result, num_list_sorted[i],operation_input)
    
    print(f"Result of Performing {operation_input} on {num_list_sorted} is {result}")
    

if __name__ == "__main__":
    calculator()