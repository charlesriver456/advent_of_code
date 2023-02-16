from typing import List
from functools import reduce

TEXT_FILE_LOCATION = "input.txt"


def calculate(acc: List, val: List[str]) -> List[int]:
    # if first pair covers second pair
    if int(val[0]) <= int(val[2]) and int(val[1]) >= int(val[3]):
        acc.append(1)
    # if second pair covers first pair
    elif int(val[2]) <= int(val[0]) and int(val[3]) >= int(val[1]):
        acc.append(1)
    else:
        acc.append(0)
    return acc


def main():
    with open(TEXT_FILE_LOCATION) as file:
        lines = map(lambda s: s.rstrip("\n"), file.readlines())
        lines = list(map(lambda s: s.replace(",", "-").split("-"), lines))
    number_list = reduce(calculate, lines, [])
    print(f"Sum for part one is: {sum(number_list)}")


if __name__ == "__main__":
    main()
