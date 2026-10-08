# # # # # # email=input("What is your email? ").strip()

# # # # # # if "@" in email and "." in email:
# # # # # #     print("valid")
# # # # # # else:
# # # # # #     print('Invalid')

# # # # # email = input("What is your email? ").strip()

# # # # # username, domain = email.split("@")

# # # # # if (username) and ("." in domain): 
# # # # #     print("valid")

# # # # # else:
# # # # #     print("invalid")

# # # # import re

# # # # email = input("Email? ").strip()

# # # # if re.search(r".+@.+\.edu", email):
# # # #     print("Valid")
# # # # else:
# # # #     print("invalid")

# # # import re

# # # email = input("email? ").strip()

# # # if re.search(r"^.+@.+\.edu$", email):
# # #     print("Valid")

# # # else:
# # #     print("invalid")

# # import re 

# # email = input("Enter email? ").strip()

# # if re.search(r"^[^@]+@[^@]+\.edu$", email):
# #     print("valid")

# # else:
# #     print("invalid")

# import re 

# email = input("What email?  ")

# if re.search(r"^\w+@\w+\.edu$", email):
#     print("valid")
# else:
#     print("invalid")



import re 

animal = input("Cat or dog ")

if re.search("Cat", animal):
    print("Valid")
else:
    print("invalid")