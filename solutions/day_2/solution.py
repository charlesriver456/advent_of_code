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


def open_file(file_location: str) -> TextIO:
    f = open(TEXT_FILE_LOCATION, "r")
    return f


def calculate_points(file: TextIO) -> int:
    file_data_in_list = file.read().split("\n")
    print(file_data_in_list)
    score = 0
    debug = 0
    for line in file_data_in_list:
        score += GAME_TABLE[line[0]][line[2]]
        debug += 1
        if line == "":
            print("passed")
            pass
    return score


# do it all
def main():
    file = open_file(TEXT_FILE_LOCATION)
    print("Your score is: " + str(calculate_points(file)))


if __name__ == "__main__":
    main()
