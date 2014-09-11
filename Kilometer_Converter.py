__author__ = 'dwight'

# Write a program that asks the user to enter a distance in kilometers, and then converts that distance to miles.


def main():
    print('Kilometers to Miles Converter')
    print('-----------------------------')
    kilometers = float(input('Enter number of kilometers: '))
    print(kilometers, 'km =', km_to_mi(kilometers), 'mi')


def km_to_mi(kilometers):
    return kilometers * 0.6214


main()