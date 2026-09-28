name = input("Name? ").capitalize()

# if name == "x" or name == "y" or name == "z":
#     print(f"{name} is the leader of his country")

# else:
#     print("WHO?")
match name:
    case "b" | "y" | "a":
        print("Germany")
    case "z":
        print("USA")
    case "f":
        print("France")
    case _:
        print("WHO?")
