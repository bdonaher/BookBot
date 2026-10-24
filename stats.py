def get_word_count(file_contents: str) -> int:
    words = file_contents.split()

    return len(words)


def get_character_count(file_contents: str) -> dict[str, int]:
    contents = {}

    for char in file_contents:
        char = char.lower()

        if char in contents:
            contents[char] += 1
        else:
            contents[char] = 1

    return contents


def sort_on(char: tuple[str, int]) -> int:
    return char[1]


def chars_dict_to_sorted_list(contents: dict[str, int]) -> list[tuple[str, int]]:
    contents_list = []

    for char in contents:
        contents_list.append((char, contents[char]))

    return sorted(contents_list, reverse=True, key=sort_on)


