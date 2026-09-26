#Creates a book class
class book:

    #Builder The Constructor of a title, author, how many pages of a book
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    #Constructs a method that checks if the page length is greater than 300
    def is_long(self):
        return self.pages > 300

    #Constructs a printing method 
    def __str__(self):
        return "{} by {} ({} pages)".format(self.title, self.author, self.pages)

#Asks again until the user types a number.
def ask_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a number.")


#The main program where I define user input and call these methods
title = input("Book title: ")
author = input("Author :  ")
pages = ask_number("Pages  :")
dune = book(title, author, pages)

print(dune)
print(dune.is_long())
