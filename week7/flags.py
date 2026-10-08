import re

email= input("Enter your email? ")

if re.search(r"^\w+@\w+\.edu$", email, re.IGNORECASE):
    print("valid")
    
else:
    print("invalid")