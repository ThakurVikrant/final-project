#Hexagon program

while True:
    try:
        size = int(input("Enter a size for the hexagon: "))
        if size <= 0:
            raise ValueError
        break
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

for i in range(size):
    print(" " * (size-i-1) + "* " * (i+1))

for i in range(size-1):
    print(" " * (i+1) + "* " * (size-i-1))

