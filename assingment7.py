# Assignment 7: Patterns and Odd Tables

# Pattern 1: Multiplication Table Pattern
def multiplication_table_pattern(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(i * j, end="\t")
        print()

# Pattern 2: Print Odd Tables (1 to 20)
def odd_tables():
    for i in range(1, 21, 2):  # Loop through odd numbers
        print(f"Table of {i}:")
        for j in range(1, 11):  # Print table up to 10
            print(f"{i} x {j} = {i * j}")
        print()  # Add a newline after each table

# Main function to display patterns and tables
def main():
    n = 5  # Size of the multiplication table pattern
    print("Multiplication Table Pattern:")
    multiplication_table_pattern(n)
    print("\nOdd Tables (1 to 20):")
    odd_tables()

# Run the program
main()
input("\nPress Enter to exit...")
