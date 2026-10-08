# # # name = input("what is your name? ").strip()

# # # if "," in name:
# # #     last,first = name.split(", ")
# # #     name = f"{first} {last}"
    
# # # print(f"hello {name}")

# # name = input("enter your name? ")

# # if "," in name:
# #     last,middle, first = name.split(", ")
# #     name = f"{first} {middle} {last}"
    
# # print(f"Bonjour {name}")

# import re

# name = input("Wie heißt du? ").strip()

# matches = re.search(r"^(.+), (.+)$", name)
# if matches:
#         last, first = matches.groups()
#         name = f"{first} {last}"
    
# print(f"Hallo {name}")


# import re 

# location = input("Where are you from? ").strip()

# matches = re.search(r"^(.+), (.+)$", location)
# if matches:
#     country,city = matches.groups()
#     location = f"{city}, {country}"

# print(f"{location}")

import re

name = input("What is your name? ").strip()

matches= re.search(r"^(.+), (.+)$", name)
if matches:
    last, first = matches.groups()
    name = f"{first} {last}"

print(f"Namaste {name}")
