"""
Debugged by: Group 4
File: computesquare.py
Illustrates the definition of a main function.
"""

def main():
    """The main function for this script."""
    number = float(input("Enter a number: "))
    result = square(number)
    print("The square of", number, "is", result)

def square(x):
    """Returns the square of x. """
    return x ** 0.5

# The entry point for program execution
if __name__ == "__main__":
    main()
