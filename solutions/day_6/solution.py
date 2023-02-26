from typing import List

TEXT_FILE_LOCATION = "input.txt"
ORD_VAL_SET = set()


def read_stream_part1(list_of_ord_chars: List[int]) -> int:

    for ord_val_index in range(0, len(list_of_ord_chars)):
        next_group_of_ords = list_of_ord_chars[ord_val_index : ord_val_index + 4]
        set_of_next_set_of_ords = set(
            list_of_ord_chars[ord_val_index : ord_val_index + 4]
        )
        if sorted(next_group_of_ords) == sorted(list(set_of_next_set_of_ords)):
            return ord_val_index + 4


def read_stream_part2(list_of_ord_chars: List[int]) -> int:

    for ord_val_index in range(0, len(list_of_ord_chars)):
        next_group_of_ords = list_of_ord_chars[ord_val_index : ord_val_index + 14]
        set_of_next_set_of_ords = set(
            list_of_ord_chars[ord_val_index : ord_val_index + 14]
        )
        if sorted(next_group_of_ords) == sorted(list(set_of_next_set_of_ords)):
            return ord_val_index + 14


def main():
    with open(TEXT_FILE_LOCATION) as file:
        lines = file.read()
    lines = list(map(lambda x: ord(x), [*lines]))
    print(lines)
    chars_processed = read_stream_part1(lines)
    print(f"chars processed for part one is {chars_processed}")
    chars_processed_p2 = read_stream_part2(lines)
    print(f"chars processed for part two is {chars_processed_p2}")


if __name__ == "__main__":
    main()
