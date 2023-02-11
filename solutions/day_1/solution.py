# opens input.txt, reads through the lines, and determines elf with the most food
from typing import TextIO

TEXT_FILE_LOCATION = "input.txt"

# DB So, the way you are using the `open_file`, you never close the file.
# This is bad practice. The prefered way to deal with files in Python is
# with a `with` clause actually. Look into using that instead. The `with`
# clause automatically closes the file once you exit the clause.
def open_file(file: str) -> TextIO:
    f = open(TEXT_FILE_LOCATION, "r")
    return f


# read the text file
# if it's new line take the sum and create that as new value using incrementing value as key
# othewise add the value in the line to the sum and keep going
def sum_elf_food(file_location: TextIO) -> dict:
    # DB: I am curios why you begin the counter at `1` and not `0`
    elf_number = 1
    calorie_sum = 0
    dict_of_cals = {}
    
    # DB: Unsure where `file` comes from. It is not defined anywhere.
    for line in file:
        # DB: For this type of structure, use a set (ie: {"\n", "\r\n"}) is faster
        # than a tuple lookup.
        # DB: I am also going to re-write this, keeping the structure you used, but
        # using dicts in a more clever manner
        """
        if line in ("\n", "\r\n"):
            dict_of_cals[elf_number] = calorie_sum
            calorie_sum = 0
            elf_number += 1
        else:
            calorie_sum += int(line)
        """
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
    file = open_file(TEXT_FILE_LOCATION)
    calorie_dict = sum_elf_food(file)
    print("Max number of calories is: " + str(get_max_calorie_value(calorie_dict)))
    print("Top three sum of calories is: " + str(first_three_calorie_sum(calorie_dict)))


if __name__ == "__main__":
    main()
