import sys
from stats import get_word_count, get_character_count, chars_dict_to_sorted_list

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(file_path: str) -> str:
    with open(file_path) as f:
        file_contents = f.read()

    return file_contents


def print_report(file_path: str, word_count: int, character_list: list) -> str:
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    for char in character_list:
        if char[0].isalpha():
            print(f"{char[0]}: {char[1]}")
    print("============= END ===============")


def main() -> None:
    book_text = get_book_text(sys.argv[1])
    word_count = get_word_count(book_text)
    character_count = get_character_count(book_text)
    sorted_character_count = chars_dict_to_sorted_list(character_count)

    print_report(sys.argv[1], word_count, sorted_character_count)

main()
