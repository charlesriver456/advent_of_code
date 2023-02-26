from typing import List

TEXT_FILE_LOCATION = "input.txt"
ORD_VAL_SET = set()


def read_stream(list_of_ord_chars: List[int]) -> int:

    for ord_val_index in range(0, len(list_of_ord_chars)):
        next_group_of_ords = list_of_ord_chars[ord_val_index : ord_val_index + 4]
        set_of_next_set_of_ords = set(
            list_of_ord_chars[ord_val_index : ord_val_index + 4]
        )
        if sorted(next_group_of_ords) == sorted(list(set_of_next_set_of_ords)):
            return ord_val_index + 4


def main():
    with open(TEXT_FILE_LOCATION) as file:
        lines = file.read()
    lines = list(map(lambda x: ord(x), [*lines]))
    print(lines)
    chars_processed = read_stream(lines)
    print(f"chars processed for part one is {chars_processed}")


if __name__ == "__main__":
    main()
