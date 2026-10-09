# # # # # # # # # # # # name = input("Name: ")
# # # # # # # # # # # # country= input("Country: ")

# # # # # # # # # # # # print(f"{name} from {country}")

# # # # # # # # # # # def main():
# # # # # # # # # # #     name= get_name()
# # # # # # # # # # #     country= get_country()
# # # # # # # # # # #     print(f"{name} from {country}")

# # # # # # # # # # # def get_name():
# # # # # # # # # # #     return input("Name: ")

# # # # # # # # # # # def get_country():
# # # # # # # # # # #     return input("Country: ")
    
    

# # # # # # # # # # # if __name__ == "__main__":
# # # # # # # # # # #     main()


# # # # # # # # # # def main():
# # # # # # # # # #    name, country =get_student()
# # # # # # # # # #    print(f"{name} is from {country}")
    
# # # # # # # # # # def get_student():
# # # # # # # # # #     name = input("Name: ")
# # # # # # # # # #     country = input("Country: ")
# # # # # # # # # #     return name, country


# # # # # # # # # # if __name__ =="__main__" :
# # # # # # # # # #     main()

# # # # # # # # # def main():
# # # # # # # # #     student= get_student()
# # # # # # # # #     print(f"{student[0]} is from {student[1]}")


# # # # # # # # # def get_student():
# # # # # # # # #     name=input("Name: ")
# # # # # # # # #     country=input("Country: ")
# # # # # # # # #     return (name, country)


# # # # # # # # # if __name__ == "__main__":
# # # # # # # # #     main()


# # # # # # # # # TUPLES ARE IMMUTABLE
# # # # # # # # def main():
# # # # # # # #     student = get_student()
    
# # # # # # # #     if student[0] == "Leo":
# # # # # # # #         student[1] = "United Kingdom"
    
# # # # # # # #     print(f"{student[0]} is from {student[1]}")


# # # # # # # # def get_student():
# # # # # # # #     name= input("Name: ")
# # # # # # # #     country = input("Country: ")
# # # # # # # #     return (name, country)

# # # # # # # # if __name__ == "__main__":
# # # # # # # #     main()


# # # # # # # def main():
# # # # # # #     student = get_student()
# # # # # # #     if student[0] == "Leo":
# # # # # # #         student[1] = "United Kingdom"
# # # # # # #     print(f"{student[0]} is from {student[1]}")
    
    
# # # # # # # def get_student():
# # # # # # #     name = input("Name: ")
# # # # # # #     country = input("Country: ")
    
# # # # # # #     return [name, country]

# # # # # # # if __name__ == "__main__":
# # # # # # #     main()

# # # # # # def main():
# # # # # #     student =get_student()
# # # # # #     if student["name"] =="Leo":
# # # # # #         student["country"] = "United Kingdom"
# # # # # #     print(f"{student['name']} nation is {student['country']}")
    
    
# # # # # # def get_student():
# # # # # #     students = {}
# # # # # #     students['name'] = input("Name: ")
# # # # # #     students['country'] = input("Country: ")
# # # # # #     return students

# # # # # # if __name__ == "__main__":
# # # # # #     main()

# # # # # class Student:
# # # # #     ...

# # # # # def main():
# # # # #     student = get_student()
# # # # #     print(f"{student.name} is originally from {student.country}")

# # # # # def get_student():
# # # # #     student =Student()
# # # # #     student.name = input("Name: ")
# # # # #     student.country = input("Country: ")
# # # # #     return student
    
# # # # # if __name__ =="__main__":
# # # # #     main()

# # # # class Student:
# # # #     def __init__(self, name, country):
# # # #         self.name = name
# # # #         self.country = country
    
# # # # def main():
# # # #     student = get_student()
# # # #     print(f"{student.name} is one and only from {student.country}")

# # # # def get_student():
# # # #     name= input("Name: ")
# # # #     country = input("Country: ")
# # # #     student = Student(name, country)
# # # #     return student

# # # # if __name__ == "__main__":
# # # #     main()

# # # class Student:
# # #     def __init__(self, name, country):
# # #         if not name:
# # #             raise ValueError("Missing name")
# # #         if country not in ["UK", "USA", "Germany", "Australia"]:
# # #             raise ValueError("Country not in options")
# # #         self.name = name
# # #         self.country = country
    
# # # def main():
# # #     student = get_student()
# # #     # print(f"{student.name} country is {student.country}")
# # #     print(student)


# # # def get_student():
# # #     name = input("Name: ")
# # #     country = input("Country: ")
# # #     return Student(name, country)
  
        

# # # if __name__ == "__main__":
# # #     main()

# # class Student:
# #     def __init__(self, name, city, speciality):
# #         if not name :
# #             raise ValueError("No name")
# #         if city not in ["London","NewYork", "Berlin", "Manchester"]:
# #             raise ValueError("City not in the list")
        
# #         self.name = name
# #         self.city = city
# #         self.speciality = speciality
        
        
# #     def __str__(self):
# #         return f"{self.name} city is {self.city} and specializes in {self.speciality}"
    
# #     def charm(self):
# #         match self.speciality:
# #             case "Python":
# #                 return "🐍"
# #             case "Java":
# #                 return "☕️"
# #             case "C":
# #                 return "🅲"
# #             case ".NET":
# #                 return "🥅"
# #             case _:
# #                 return "No charm found 🔍" 

# # def main():
# #     student = get_student()
# #     print(student)
# #     print("Expected charm")
# #     print(student.charm())
    
# # def get_student():
# #     name=input("Name: ")
# #     city= input("City: ")
# #     speciality= input("Speciality: ")
# #     return Student(name, city, speciality)

# # if __name__ == "__main__":
# #     main()


# class Student:
#     def __init__(self, name, city):
#         self.name = name
#         self.city = city
        
#     def __str__(self):
#         return (f"{self.name} city is {self.city}")
    
#     @property
#     def name(self):
#         return self._name
    
#     @name.setter
#     def name(self,name):
#         if not name:
#             raise ValueError("No name")
        
#         self._name = name
    
#     @property
#     def city(self):
#         return self._city
    
#     @city.setter
#     def city(self, city):
        
#         if city not in ["London", "Berlin", "Newyork", "Sydney"]:
#             raise ValueError("City not in the list")
            
#         self._city = city

# def main():
#     student = get_student()
#     print(student)
    
# def get_student():
#     name = input("Name: ")
#     city = input("City: ")
#     return Student(name,city)
    
# if __name__ == "__main__":
#     main()

class Student:
    def __init__(self, name, country):
        self.name = name
        self.country = country
    
    def __str__(self):
        return f"{self.name} country is {self.country}"
        
    @classmethod
    def get(cls):
        name = input("Name: ")
        country = input("Country: ")
        return cls(name, country)
    

def main():
    student = Student.get()
    print(student)
    


if __name__ == "__main__":
    main()