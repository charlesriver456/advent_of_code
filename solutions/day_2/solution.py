# read in txt

from typing import TextIO

TEXT_FILE_LOCATION = "input.txt"

GAME_TABLE = {
    "A": {
        "X": 3 + 1,  # draw + rock
        "Y": 6 + 2,  # win + paper
        "Z": 0 + 3,  # loss + scissors
    },
    "B": {
        "X": 0 + 1,  # loss + rock
        "Y": 3 + 2,  # draw + paper
        "Z": 6 + 3,  # win + scissors
    },
    "C": {
        "X": 6 + 1,  # win + rock
        "Y": 0 + 2,  # loss + paper
        "Z": 3 + 3,  # draw + scissors
    },
}


def open_file(file: str) -> TextIO:
    f = open(TEXT_FILE_LOCATION, "r")
    return f
