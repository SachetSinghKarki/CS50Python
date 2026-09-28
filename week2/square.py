def main():
    print_square(4)


# def print_square(size):
#     # for each row in sqaure
#     for i in range(size):
#         # print each * in the row
#         for j in range(size):
#             # The star
#             print("*", end="")
#         print()

def print_square(size):
    for i in range(size):
        print("*" * size)


main()
