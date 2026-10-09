# import random
# class Hat:
    
#     def __init__(self):
#         self.houses=["London", "Berlin", "NewYork", "Paris"]
    
#     def sort(self, name):
#         house = random.choice(self.houses)
#         print(f"{name} is in {house}")
        


# hat = Hat()
# hat.sort("Leo")

import random

class Hat:
    houses = ["London", "Newyork", "Paris", "Berlin"]
    
    @classmethod
    def sort(cls, name):
        print(f"{name} is in", random.choice(cls.houses))
        
Hat.sort("Leo")