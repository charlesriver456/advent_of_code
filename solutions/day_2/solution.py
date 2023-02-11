# read in txt

from typing import TextIO

TEXT_FILE_LOCATION = "input.txt"

GAME_TABLE_PART_1 = {
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

GAME_TABLE_PART_2 = {
    "A": {
        "X": 0 + 3,  # loss + scissors
        "Y": 3 + 1,  # draw + rock
        "Z": 6 + 2,  # win + paper
    },
    "B": {
        "X": 0 + 1,  # loss + rock
        "Y": 3 + 2,  # draw + paper
        "Z": 6 + 3,  # win + scissors
    },
    "C": {
        "X": 0 + 2,  # loss + paper
        "Y": 3 + 3,  # draw + scissors
        "Z": 6 + 1,  # win + rock
    },
}

# DB: Again be mindful of the closing of the file. Use a `with` clause
def open_file(file_location: str) -> TextIO:
    f = open(TEXT_FILE_LOCATION, "r")
    return f


def calculate_points(file: TextIO) -> int:
    file_data_in_list = file.read().split("\n")
    score_part_one = 0
    score_part_two = 0
    
    # DB: Clean up `debug` at the end
    debug = 0
    for line in file_data_in_list:
        # I would have written this as:
        """
        if line != "":
            # Do ths stuff
        """
        if line == "":
            pass
        else:
            score_part_one += GAME_TABLE_PART_1[line[0]][line[2]]
            score_part_two += GAME_TABLE_PART_2[line[0]][line[2]]
            debug += 1
    return score_part_one, score_part_two


# do it all
def main():
    file = open_file(TEXT_FILE_LOCATION)
    score_part_one, score_part_two = calculate_points(file)
    
    # I would have used an f-string. ie: f"Your score for part1 is: {score_part_one}"
    print("Your score for part1 is: " + str(score_part_one))
    print("Your score for part2 is: " + str(score_part_two))


if __name__ == "__main__":
    main()
