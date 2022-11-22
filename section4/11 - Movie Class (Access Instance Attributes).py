"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""


class Movie:

    def __init__(self, title, year, language, rating):
        self.title = title
        self.year = year
        self.language = language
        self.rating = rating


my_favourite_movie = Movie("Pride and Prejudice", 2005, "English", 4.8)
your_favourite_movie = Movie("Titanic", 1997, "English", 4.6)

print("My Favourite Movie:")
print(my_favourite_movie.title)
print(my_favourite_movie.year)
print(my_favourite_movie.language)
print(my_favourite_movie.rating)
print()
print("Your Favourite Movie:")
print(your_favourite_movie.title)
print(your_favourite_movie.year)
print(your_favourite_movie.language)
print(your_favourite_movie.rating)
