from stats import word_count, charachter_count, sort_dict
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path = sys.argv[1]
    text = get_book_text(path)
    num_words = word_count(text)
    num_char = charachter_count(text)
    sorted_dict = sort_dict(num_char)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in sorted_dict:
        if i.isalpha():
            print(f"{i}: {sorted_dict[i]}")

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents


main()