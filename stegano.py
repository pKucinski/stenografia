from options.FirstOption import FirstOption
from options.SecondOption import SecondOption
from options.ThirdOption import ThirdOption
from options.FourthOption import FourthOption
import sys


def zadanie1(option):
    first_option = FirstOption(msg)

    if option == "-e":
        first_option.encrypt()
    if option == '-d':
        first_option.decrypt()


def zadanie2(option):
    second_option = SecondOption(msg)

    if option == "-e":
        second_option.encrypt()
    if option == '-d':
        second_option.decrypt()


def zadanie3(option):
    third_option = ThirdOption(msg)

    if option == "-e":
        third_option.encrypt()
    if option == '-d':
        third_option.decrypt()


def zadanie4(option):
    fourth_option = FourthOption(msg)

    if option == "-e":
        fourth_option.encrypt()
    if option == '-d':
        fourth_option.decrypt()


if __name__ == '__main__':
    file = open("mess.txt", "r")
    msg = file.read()

    options = ["-1", "-2", "-3", "-4"]

    if sys.argv[1] not in options:
        print(help)
        exit(0)

    if sys.argv[1] == options[0]:
        zadanie1(sys.argv[2])
    elif sys.argv[1] == options[1]:
        zadanie2(sys.argv[2])
    elif sys.argv[1] == options[2]:
        zadanie3(sys.argv[2])
    elif sys.argv[1] == options[3]:
        zadanie4(sys.argv[2])
