import sys
from stats import get_num_words, count_characters, sort_characters

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")

    book_text = get_book_text(sys.argv[1])

    num_words = get_num_words(book_text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    
    character_count = count_characters(book_text)
    sorted_chars = sort_characters(character_count)
    

    print("--------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['count']}")

    print("============= END ===============")
main()