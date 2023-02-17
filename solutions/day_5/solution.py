from typing import List
from functools import reduce


TEXT_FILE_LOCATION = "input.txt"
BATCH_SIZE = 3

CRATE_HOLDER = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}


def whitespace_helper(val: str) -> bool:
    if val != " ":
        return True


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
            CRATE_HOLDER[int(val[5])].append(CRATE_HOLDER[int(val[3])].pop())
            i = i - 1
    return CRATE_HOLDER


def main():
    with open(TEXT_FILE_LOCATION) as file:
        lines = list(map(lambda s: s.rstrip("\n"), file.readlines()))
        boxes = lines[:8]
        moves = lines[10:]
        boxes.reverse()
        boxes = list(map(lambda s: [s], boxes))
        moves = list(
            map(
                lambda s: s.replace("move", "")
                .replace("from", "")
                .replace("to", "")
                .split(" "),
                moves,
            )
        )
    reduce(add_to_crate_holder, boxes, [[]])
    crates = process(CRATE_HOLDER, moves)
    print(f"Final crates positions are as follows: {crates}")


if __name__ == "__main__":
    main()
