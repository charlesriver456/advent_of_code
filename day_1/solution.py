# opens input.txt, reads through the lines, and determines elf with the most food
from typing import TextIO

TEXT_FILE_LOCATION = "input.txt"


def open_file(file: str) -> TextIO:
    f = open(TEXT_FILE_LOCATION, "r")
    return f


# read the text file
# if it's new line take the sum and create that as new value using incrementing value as key
# othewise add the value in the line to the sum and keep going
def sum_elf_food(file: TextIO) -> dict:
    elf_number = 1
    calorie_sum = 0
    dict_of_cals = {}
    for line in file:
        if line in ("\n", "\r\n"):
            dict_of_cals[elf_number] = calorie_sum
            calorie_sum = 0
            elf_number += 1
        else:
            calorie_sum += int(line)
    return dict_of_cals


# find the max value in the dict's values
def get_max_calorie_value(dictionary_of_calories: dict) -> int:
    return max(dictionary_of_calories.values())


# do it all
def main():
    file = open_file(TEXT_FILE_LOCATION)
    calorie_dict = sum_elf_food(file)
    print("Max number of calories is: " + str(get_max_calorie_value(calorie_dict)))


if __name__ == "__main__":
    main()
