def diamond_pattern(n):
    for i in range(n):
        print(" " * (n - i - 1) + "*" + " " * (2 * i - 1) + ("*" if i != 0 else ""))
    for i in range(n - 2, -1, -1):
        print(" " * (n - i - 1) + "*" + " " * (2 * i - 1) + ("*" if i != 0 else ""))

def hollow_square(n):
    for i in range(n):
        if i == 0 or i == n - 1:
            print("* " * n)
        else:
            print("* " + "  " * (n - 2) + "*")

def right_triangle(n):
    for i in range(n):
        print("* " * (i + 1))

def number_pyramid(n):
    for i in range(1, n + 1):
        print("1 " * i)

def number_pyramid_increment(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

def main():
    n = 5
    print("Diamond Pattern:")
    diamond_pattern(n)
    print("\nHollow Square Pattern:")
    hollow_square(n)
    print("\nRight Triangle Pattern:")
    right_triangle(n)
    print("\nNumber Pyramid:")
    number_pyramid(n)
    print("\nNumber Pyramid with Incrementing Numbers:")
    number_pyramid_increment(n)

main()
input("\nPress Enter to exit...")
