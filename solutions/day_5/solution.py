import copy
from typing import List
from functools import reduce


TEXT_FILE_LOCATION = "input.txt"
BATCH_SIZE = 3


def edit_crate_holder(size: int) -> dict:
    global CRATE_HOLDER
    CRATE_HOLDER = {list_of_crates: [] for list_of_crates in range(1, size + 2)}


def whitespace_helper(val: str) -> bool:
    return val != " "


def add_to_crate_holder(acc: None, val: List[str]) -> None:
    if whitespace_helper(val[0][1]):
        CRATE_HOLDER[1].append(val[0][1])
    if whitespace_helper(val[0][5]):
        CRATE_HOLDER[2].append(val[0][5])
    if whitespace_helper(val[0][9]):
        CRATE_HOLDER[3].append(val[0][9])
    if whitespace_helper(val[0][13]):
        CRATE_HOLDER[4].append(val[0][13])
    if whitespace_helper(val[0][17]):
        CRATE_HOLDER[5].append(val[0][17])
    if whitespace_helper(val[0][21]):
        CRATE_HOLDER[6].append(val[0][21])
    if whitespace_helper(val[0][25]):
        CRATE_HOLDER[7].append(val[0][25])
    if whitespace_helper(val[0][29]):
        CRATE_HOLDER[8].append(val[0][29])
    if whitespace_helper(val[0][33]):
        CRATE_HOLDER[9].append(val[0][33])


def process(crates: dict, moves_to_be_made: List[str]) -> dict:
    for val in moves_to_be_made:
        i = int(val[1])
        while i != 0:
            part_one_crates[int(val[5])].append(part_one_crates[int(val[3])].pop())
            i = i - 1
    return part_one_crates


def process_part_two(crates: dict, moves_to_be_made: List[str]) -> dict:
    for val in moves_to_be_made:
        i = int(val[1])
        if i > 1:
            crates_to_be_picked_up = []
            while i != 0:
                crates_to_be_picked_up.append(part_two_crates[int(val[3])].pop())
                i = i - 1
            crates_to_be_picked_up.reverse()
            part_two_crates[int(val[5])].extend(crates_to_be_picked_up)
        else:
            part_two_crates[int(val[5])].append(part_two_crates[int(val[3])].pop())
    return part_two_crates


def main():
    with open(TEXT_FILE_LOCATION) as file:
        lines = list(map(lambda s: s.rstrip("\n"), file.readlines()))
        boxes = lines[:8]
        moves = lines[10:]
        boxes.reverse()
        boxes = list(map(lambda s: [s], boxes))
        print(boxes)
        moves = list(
            map(
                lambda s: s.replace("move", "")
                .replace("from", "")
                .replace("to", "")
                .split(" "),
                moves,
            )
        )
    edit_crate_holder(len(boxes))
    reduce(add_to_crate_holder, boxes, [[]])
    global part_one_crates
    global part_two_crates
    part_one_crates, part_two_crates = CRATE_HOLDER, copy.deepcopy(CRATE_HOLDER)
    crates = process(part_one_crates, moves)
    print(f"Final crates positions are as follows for part one: {crates}")
    print(part_two_crates)
    crates_2 = process_part_two(part_two_crates, moves)
    print(f"Final crates positions are as follows for part two: {crates_2}")


if __name__ == "__main__":
    main()
