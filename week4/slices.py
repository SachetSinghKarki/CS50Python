import sys

if len(sys.argv)<2:
    print("Two few arguments")
    
for arg in sys.argv[1:]:
    print("My name is", arg)