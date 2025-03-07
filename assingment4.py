def main():
    print("Welcome to Python Operations Program")
    
    # Get user input
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    while True:
        print("\nSelect operation:")
        print("1. Arithmetic Operations")
        print("2. Bitwise Operations") 
        print("3. Relational Operations")
        print("4. Assignment Operations")
        print("5. Logical Operations")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            # Arithmetic Operations
            print(f"\nArithmetic Operations:")
            print(f"{num1} + {num2} = {num1 + num2}")
            print(f"{num1} - {num2} = {num1 - num2}")
            print(f"{num1} * {num2} = {num1 * num2}")
            print(f"{num1} / {num2} = {num1 / num2}")
            print(f"{num1} % {num2} = {num1 % num2}")
            print(f"{num1} ** {num2} = {num1 ** num2}")
            print(f"{num1} // {num2} = {num1 // num2}")
            
        elif choice == '2':
            # Bitwise Operations
            print(f"\nBitwise Operations:")
            print(f"{int(num1)} & {int(num2)} = {int(num1) & int(num2)}")
            print(f"{int(num1)} | {int(num2)} = {int(num1) | int(num2)}")
            print(f"{int(num1)} ^ {int(num2)} = {int(num1) ^ int(num2)}")
            print(f"~{int(num1)} = {~int(num1)}")
            print(f"{int(num1)} << 1 = {int(num1) << 1}")
            print(f"{int(num1)} >> 1 = {int(num1) >> 1}")
            
        elif choice == '3':
            # Relational Operations
            print(f"\nRelational Operations:")
            print(f"{num1} == {num2} = {num1 == num2}")
            print(f"{num1} != {num2} = {num1 != num2}")
            print(f"{num1} > {num2} = {num1 > num2}")
            print(f"{num1} < {num2} = {num1 < num2}")
            print(f"{num1} >= {num2} = {num1 >= num2}")
            print(f"{num1} <= {num2} = {num1 <= num2}")
            
        elif choice == '4':
            # Assignment Operations
            print(f"\nAssignment Operations:")
            a = num1
            print(f"a = num1 → a = {a}")
            a += num2
            print(f"a += num2 → a = {a}")
            a -= num2
            print(f"a -= num2 → a = {a}")
            a *= num2
            print(f"a *= num2 → a = {a}")
            a /= num2
            print(f"a /= num2 → a = {a}")
            a %= num2
            print(f"a %= num2 → a = {a}")
            
        elif choice == '5':
            # Logical Operations
            print(f"\nLogical Operations:")
            print(f"{num1} > 0 and {num2} > 0 = {num1 > 0 and num2 > 0}")
            print(f"{num1} > 0 or {num2} > 0 = {num1 > 0 or num2 > 0}")
            print(f"not {num1} > 0 = {not num1 > 0}")
            
        elif choice == '6':
            print("Exiting program...")
            break
            
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
