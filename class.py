# class Hello:
#     def __init__(self,name):
#         self.name = name
#         print("Happy Radha-Ashthami",name)

# Hello("Krishna")



# class Main:
#     def __init__(self,name,Age):
#         self.name=name
#         self.Age=Age
#         print("Hello",name,"you are",Age,"years old")

# Main("krishn",21)




# class Rectangle:
#     def __init__(self, length,width):
#         self.length = length
#         self.width = width
#     def area(self):
#         if (self.length> 0) and (self.width > 0):
#             print(f"The Area of rectangle is {self.length*self.width}")
#         else:
#             print("Number cannot be negative")
#     def perimeter(self):
#         if self.length>0 and self.width>0:
#             print("The perimeter of rectangle is", 2 * (self.length + self.width))
#         else:
#             print("Number cannot be negative")


# rec=Rectangle(3,4)
# rec1=rec.area()
# peri=rec.perimeter()


# class Book:
#     def __init__(self,book_titles):
#         self.book_titles=book_titles

#     def __str__(self):
#         return f"Book Title: {self.book_titles}"

# class Library:
#     def __init__(self):
#         self.books = []
#     def add(self,book):
#         self.books.append(book)
#     def remove(self,book_title):
#         for book in self.books:
#             if book.book_titles == book_title:
#                 self.books.remove(book)
#                 print(f"Book {book_title} removed from the library")
#             else:
#                 print("book not found")
        
#     def display(self):
#         for book in self.books:
#             print(book)


# li = Library()
# boo1 = Book("Hastar")
# boo2 = Book("Anabella")
# li.add(boo1)
# li.add(boo2)
# li.display()
# li.remove("Hastar")
# li.display()

# class Students:
#     def __init__(self, name):
#         self.name = name
#         self.grade=[]

#     def add_grade(self):
#         grade = input("Enter grade: ")
#         self.grade.append(grade)

#     def cal_avg(self):
#         if self.grade:
#             return sum(float, self.grade) / len(self.grade)
#         else:
#             return 0

# std=Students
# std.name="John"

# class Zoo:
#     def __init__(self,name,place,colour):
#         self.name = name
#         self._place=place
#         self.__colour=colour
        

#     def __bird(self):
#         print(f"The Bird name is {self.name},and Place is {self._place},and the color is {self.__colour}")
#         def access(self):
#             return self.__colour
    
# Z=Zoo("crow","tree","black")
# print(Z)
# print(Z._place)
# print(bird.access())

import numpy as np

arr=np.array([12,13,24])
print(arr)

li=np.array([12,13,24,23,2,12,32])
print(li[:1])
print(li[3:])
#----------------------------
z=np.zeros((2,2))
print(z)
#-------------------------
one=np.ones((3,2))
print(one)
#-------------------------------
arr1=np.array([2,3,4])
arr2=np.array([5,6,7])
arr3=arr1+arr2
print(arr3)
#-----------------------------
sum_arr=np.array([2,4,5])
sum_arr1=np.sum(sum_arr)
print(sum_arr1)
#-------------------------------
mean1=np.array([2,3,4])
means=np.mean(mean1)
print(means)
#-----------------------------
std=np.array([2,3,4])
std1=np.array([5,6,7])
conc=np.concatenate((std,std1),axis=0)
print(conc)
#-------------------------------
resized=np.array([1,2,3,4,5])
resized.resize(2,2)
print(resized)
#-------------------------------
spl=np.array([1,2,3,4,5,6])
split=np.array_split(spl,2)
print(split)
#----------------------------
arr=np.array([1,9,5,7,3,56,76])
sorted=np.sort(arr)
print(sorted)
#-------------------------------
arr=np.array([1,9,5,7,3,56,76])
print(max(arr))
print(min(arr))

#2d matrix
#----------------



