# 'Magic/Dunder Methods'

#QUESTION NO 1 - (__len__) - Create a Playlist class that stores a list of songs.
                # Override __len__ so len(playlist) returns the number of songs.

# class Playlist:
#     def __init__(self,songs):
#         self.songs = songs

#     def __len__(self):
#         return len(self.songs)
    
# p = Playlist(["Oldsong","90's song","bollywood song","Punjabi song"])
# print(len(p))


#QUESTION NO 2 - (__repr__) -  Write a class User with name and email.
                # Override __repr__ to return a string like: User('Tom', 'tom@example.com').

# class User:
#     def __init__(self,name,email):
#         self.name = name
#         self.email = email

#     def __repr__(self):
#         return f"User('{self.name}', '{self.email}')"
    
# p1 = User("Saloni","saloni@example.com")
# print(p1)


#QUESTION NO 3 - (__eq__) -  In the Book class, override __eq__ so two books are equal if their titles and authors match.

# class Book:
#     def __init__(self,title,author):
#         self.title = title
#         self.author = author
    
#     def __eq__(self, other):
#         if not isinstance(other,Book):
#             return False
#         return self.title == other.title and self.author == other.author
    
# b1 = Book("The Divine Comedy","Dante")
# b2 = Book("The lliad","Homer")
# b3 = Book("The lliad","Homer")

# print(b1 == b2)
# print(b2 == b3)

#QUESTION NO 4 - (__getitem__) - Create a class ShoppingList that stores a list of items.
                # Override __getitem__ to access items like list_obj[0].

class ShoppingList:
    def __init__(self,item):
        self.item = item

    def __getitem__(self,index):
        self.index = index
        return self.item[index]

s = ShoppingList(["Shampoo","Facewash","Conditioner","Moistoriser","Sunscreen"])
print(s[0])
print(s[3])
print(s[1])


#QUESTION NO 5 - (__call__) - Create a class Multiplier with a factor.
             # Override __call__ so calling the object multiplies a number.

class Multiplier:
    def __init__(self,factor):
        self.factor = factor

    def __call__(self, x):
        return x * self.factor
    
m = Multiplier(5)
print(m(6))


        




