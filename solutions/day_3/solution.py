from typing import List
from functools import reduce

TEXT_FILE_LOCATION = "input.txt"
LOWER_CASE_ORD_DIFFERENCE = 96
UPPER_CASE_ORD_DIFFERENCE = 38


def ord_calculate_helper(char: str) -> int:
    if char.islower():
        return ord(char) - LOWER_CASE_ORD_DIFFERENCE
    else:
        return ord(char) - UPPER_CASE_ORD_DIFFERENCE


def find_intersection(acc: List[int], val: List[str]) -> List[int]:
    if val != "":
        midpoint = len(val) // 2
        char_to_add = set(val[:midpoint]).intersection(set(val[midpoint:])).pop()
        acc.append(ord_calculate_helper(char_to_add))
    return acc


def calculate_letter_value(acc: List[int], val: List[str]) -> List[int]:
    char_to_add = set(val[0]).intersection(set(val[1]).intersection(set(val[2]))).pop()
    if char_to_add.islower():
        acc.append(ord(char_to_add) - LOWER_CASE_ORD_DIFFERENCE)
    else:
        acc.append(ord(char_to_add) - UPPER_CASE_ORD_DIFFERENCE)
    return acc


def main():
    with open(TEXT_FILE_LOCATION) as file:
        lines = list(map(lambda s: s.rstrip("\n"), file.readlines()))
    elf_item_list = reduce(find_intersection, lines, [])
    # creates iter object and copies it twice over (3 total elements)
    final = list(zip(*[iter(lines)] * 3))
    group_list = reduce(calculate_letter_value, final, [])
    print(f"Sum for part one is: {sum(elf_item_list)}")
    print(f"Sum for part two is: {sum(group_list)}")


if __name__ == "__main__":
    main()
