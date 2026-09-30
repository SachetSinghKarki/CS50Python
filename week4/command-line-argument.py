# # # # import sys

# # # # print("Hello my name is", sys.argv[1])

# # # import sys

# # # try:
# # #     print("My name is ", sys.argv[1])

# # # except IndexError:
# # #     print("Two few arguments")

# # import sys

# # if len(sys.argv) < 2:
# #     print("Two few arguments")

# # elif len(sys.argv) > 2:
# #     print("Two many arguments")

# # print("My name is", sys.argv[1])

# import sys

# if len(sys.argv) < 2:
#     sys.exit("Two few arguments")

# elif len(sys.argv)> 2:
#     sys.exit("Two many arguments")

# print("My name is", sys.argv[1])

import sys

if len(sys.argv) <2:
    print("Two few arguments")

for arg in sys.argv:
    print("My name is",arg)

