# opens input.txt, reads through the lines, and determines elf with the most food
from typing import TextIO

TEXT_FILE_LOCATION = "input.txt"


# read the text file
# if it's new line take the sum and create that as new value using incrementing value as key
# othewise add the value in the line to the sum and keep going
# start with elf 1 because that's what the example started with
def sum_elf_food(file: TextIO) -> dict:
    elf_number = 1
    dict_of_cals = {}
    for line in file:
        if line in {"\n", "\r\n"}:
            # Move on to the next elf
            elf_number += 1
        else:
            # The `get` does a query, but can supply a default value if the key does not exist
            dict_of_cals[elf_number] = dict_of_cals.get(elf_number, 0) + int(line)
    return dict_of_cals


# find the max value in the dict's values
def get_max_calorie_value(dictionary_of_calories: dict) -> int:
    return max(dictionary_of_calories.values())


def first_three_calorie_sum(dictionary_of_calories: dict) -> int:
    calories_list = list(dictionary_of_calories.values())
    calories_list.sort(reverse=True)
    sum_of_top_three_elves = sum(calories_list[:3])
    return sum_of_top_three_elves


# do it all
def main():
    with open(TEXT_FILE_LOCATION) as file:
        calorie_dict = sum_elf_food(file)
        print("Max number of calories is: " + str(get_max_calorie_value(calorie_dict)))
        print(
            "Top three sum of calories is: "
            + str(first_three_calorie_sum(calorie_dict))
        )


if __name__ == "__main__":
    main()
