def main():
    print_column(3)

def print_column(height):
    #for _ in range(height):
    #    print("#")
    #simplified:
    print("#\n" * height, end="")

def print_row(width):
    print("?" * width)

def print_square(size):
    for i in range(size):
        #for j in range(size):
        #    print("#", end="")
        #print()
        #simplified:
        #print("#" * size)
        #dev style:
        print_row(size)


main()