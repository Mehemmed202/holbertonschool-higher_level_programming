#!/usr/bin/python3
"""FizzBuzz funksiyası üçün modul"""

def fizzbuzz():
    """
    1-dən 100-ə qədər rəqəmləri FizzBuzz qaydalarına uyğun çap edir.
    Hər elementdən sonra bir boşluq qoyulur.
    """
    for number in range(1, 101):
        if number % 15 == 0:
            print("FizzBuzz ", end="")
        elif number % 3 == 0:
            print("Fizz ", end="")
        elif number % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(number), end="")
