"""
Practice problems to get the hang of converting among data types.
In this case, we focus on converting numeric data types to strings and vice-versa.
"""


def calculate_profit():
    """
    Imagine this scenario: a company has determined that its annual profit is typically 23 percent of total sales.
    Complete this function so that it asks the user to enter in the projected amount of total sales and then displays the profit that will be made from that amount.
    You can assume the user will enter only numeric characters, e.g. "3000", not "$3,000.00"
    The output should match the format of the following examples: "Profit: $690.00" for sales of $3,000, or "Profit: $2,300.00" for sales of $10,000, etc.
    """
    total_sales = input("What is your total sales? ")
    total_sales = int(total_sales)
    profit = 0.23 * total_sales
    print(f"Profit: ${profit:,.2f}")
# calculate_profit()
    



def calculate_quotient_and_remainder():
    """
    Complete this function so that it asks the user to input two integers.
    You program should calculate and output the quotient and remainder when the first number is divided by the second.
    Here's an example run of the function:
      Enter number #1: 5
      Enter number #2: 2
      2 goes into 5 a total of 2 times with a remainder of 1
    """
    first_number = input("What is your first integer? ") 
    first_number = int(first_number) 
    second_number = int(input("What is your second integer? "))
    quotient = first_number // second_number
    remainder = first_number % second_number
    print(f"{second_number} goes into {first_number} a total of {quotient} times with a remainder of {remainder}")
# calculate_quotient_and_remainder()


def calculate_miles_per_gallon():
    """
    A car's Miles Per Gallon (MPG) can be calculated using the following formula:
      MPG = Miles driven / Gallons of Gas Used
    Complete this function so that it asks the user for the number of miles driven and the gallons of gas used.
    It should calculate the car's MPG and display the result in the format indicated in this example run of the program:

      Miles driven: 100
      Gas used (gallons): 25
      Miles per gallon: 4.0
    """
    miles_driven = int(input("What is your miles driven? "))
    gas_used = int(input("How much gas did you use? "))
    mpg = miles_driven / gas_used
    print(f"Miles driven: {miles_driven}\nGas used(gallons): {gas_used}\nMiles per gallon: {mpg:.1f}")
# calculate_miles_per_gallon()



def align_text():
    """
    Complete this function such that it asks the user to enter in 3 price values (as floating point numbers).
    The print out the price values so that they are formatted to two decimal places. Also make sure that the price values are right aligned and line up at the decimal point.
    Here's a sample running of the program:

      Enter price #1: 1.55
      Enter price #2: 10
      Enter price #3: 9532.6

      Here are your prices!

      Price #1: $    1.55
      Price #2: $   10.00
      Price #3: $ 9532.60
    """
    # first_number = round(float(input("Enter price #1: ")),2)
    # second_number = round(float(input("Enter price #2: ")),2)
    # third_number = round(float(input("Enter price #3: ")),2)
    # print("\nHere are your prices!\n")
    # print("Price #1: $", format(first_number, ">8.2f"))
    # print("Price #2: $", format(second_number, ">8.2f"))
    # print("Price #3: $", format(third_number, ">8.2f"))
    first_number = float(input("Enter price #1: "))
    second_number = float(input("Enter price #2: "))
    third_number = float(input("Enter price #3: "))
    print("\nHere are your prices!\n")
    max_width = max(len(str(first_number)), len(str(second_number)), len(str(third_number))) + 2
    print(f"Price #1: ${first_number:>{max_width}.2f}",)
    print(f"Price #2: ${second_number:>{max_width}.2f}")
    print(f"Price #3: ${third_number:>{max_width}.2f}")
# align_text()

    
