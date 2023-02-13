from typing import List
from functools import reduce

TEXT_FILE_LOCATION = "input.txt"
LOWER_CASE_ORD_DIFFERENCE = 96
UPPER_CASE_ORD_DIFFERENCE = 38


def find_intersection(acc: List, val: map) -> List[int]:
    if val != "":
        midpoint = len(val) // 2
        char_to_add = set(val[:midpoint]).intersection(set(val[midpoint:])).pop()
        if char_to_add.islower():
            acc.append(ord(char_to_add) - LOWER_CASE_ORD_DIFFERENCE)
        else:
            acc.append(ord(char_to_add) - UPPER_CASE_ORD_DIFFERENCE)
    else:
        acc += []
    return acc


def create_groups(acc: List[List], val: map) -> List[List]:
    print("reached")
    iterator = 0
    if val != "" and iterator % 3 != 0 and iterator > 0:
        acc.append(val)
        iterator += 1
    else:
        acc += [[]]
        acc.append(val)
        iterator += 1
    return acc


def main():
    with open(TEXT_FILE_LOCATION) as file:
        lines = map(lambda s: s.rstrip("\n"), file.readlines())
    elf_item_list = reduce(find_intersection, lines, [])
    group_list = reduce(create_groups, lines, [[]])
    print(group_list)
    print(f"Sum for part one is: {sum(elf_item_list)}")


if __name__ == "__main__":
    main()
