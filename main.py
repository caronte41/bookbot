from stats import count_words
from stats import count_chars
from stats import char_stats_sorted

def get_book_text(filepath):
    with open(filepath, "r", encoding="utf-8") as file:  # Open the file properly
        return file.read()


def main():
    content = get_book_text("books/frankenstein.txt")
    num = count_words(content)  # Remove the leading "/"
    num_char = count_chars(content)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num} total words") 
    print("--------- Character Count -------")
    sort_dict = char_stats_sorted(num_char)
    for key, value in sort_dict:
        if key.isalpha():  
            print(f"{key}: {value}") 
    print("============= END ===============")      

main()
