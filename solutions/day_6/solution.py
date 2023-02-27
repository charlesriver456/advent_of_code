from typing import List

TEXT_FILE_LOCATION = "input.txt"


def read_stream(list_of_ord_chars: List[int], size_of_message: int) -> int:

    for ord_val_index in range(len(list_of_ord_chars)):
        next_group_of_ords = list_of_ord_chars[
            ord_val_index : ord_val_index + size_of_message
        ]
        set_of_next_set_of_ords = set(next_group_of_ords)
        if sorted(next_group_of_ords) == sorted(list(set_of_next_set_of_ords)):
            return ord_val_index + size_of_message


def main():
    with open(TEXT_FILE_LOCATION) as file:
        lines = file.read()
    lines = list(map(lambda x: x, [*lines]))
    chars_processed = read_stream(lines, 4)
    print(f"chars processed for part one is {chars_processed}")
    chars_processed_p2 = read_stream(lines, 14)
    print(f"chars processed for part two is {chars_processed_p2}")


if __name__ == "__main__":
    main()
