# print('Hello')

# age = 21
# name = 'Dagna'
# todayiscold = True
# sentence = 'My name is {} and i am {} years old.'.format(name,age)
# # print(sentence)

# if todayiscold:
#     print('You are an adult')
#     print('Get your shit together')

# if age>18:
#     print('You are an adult')
#     print('Get your shit together')
# else:
#     print('Today is not cold')
#     print('Grow up')


# year = 1830
# if year >= 2000 and year <= 2100:
#     print('Yo')
# else:
#     print('No')

# def hello(name, age=0):     #default function
#     print("hello {} you are {} years old".format(name,age))

# hello("Angad",27)

# def tripleprint(word):
#     new = word*3
#     print(new)

# tripleprint("hello")

# dognames = ["Fido","Sean","sally","Marks"]
# print(dognames)

# dognames.append("Zack")
# print(dognames)

# dognames[1]= "Jane"
# print(dognames)

# for dog in dognames:
#     print(dog)

# i=0
# while i<10:
#     print(i)
#     i=i+1

# dogs = {"Fido":8,"Sally":17,"Sean":2}
# print(dogs["Sally"])

# dogs["Sarah"]=6
# print(dogs)

# class Dog:
#     doginfo = 'Hey dogs are cool'


#     def bark(self,str):
#         print("BARKS!"+str)

# mydog = Dog()
# mydog.bark('hoho')

# mydog.name = 'Zuri'
# mydog.age = 2
# print(mydog.name)
# print(mydog.age)
# print(Dog.doginfo)

# class Cat:
#     def __init__(self, name, age, color):
#         self.name = name
#         self.age = age
#         self.color = color

#     def meow(self,str):
#         print("Meow!"+str)

# catto = Cat("Zuri",2,"White")
# print(catto.name)
class Car:
    def __init__(self,year, make, model):
        self.year = year
        self.make = make
        self.model = model
    
    def age(self):
        age = 2020 - self.year
        return age
        
obj = Car(2018,"Ford","cruz")
print(obj.age())