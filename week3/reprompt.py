def main():
    y = get_int()
    print(f"x is {y}")
    
    
def get_int():
    while True:
        try:
           return int(input("What is x? "))       
        except ValueError:
            print("x is not an integer")


main()