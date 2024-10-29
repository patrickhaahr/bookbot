def main():
    book_path = "path/to/your/book.txt"
    text = get_book_text(book_path)

    if text is not None:
        words_count = count_words(text)
        chars_count = count_chars(text)

        print_report(book_path, words_count, chars_count)
    else:
        print("Failed to read the book.")

def get_book_text(path):
    try:
        with open(path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: The file at {path} was not found.")
        return None

def count_words(text):
    words = text.split()
    count = len(words)
    return count

def count_chars(text):
    text = text.lower()
    char_counts = {}

    for char in text:
        if char.isalpha():
            char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts

def print_report(path, words_count, char_counts):
    # Sort character counts by the number of occurrences, in descending order
    sorted_chars = sorted(char_counts.items(), key=lambda item: item[1], reverse=True)

    print(f"--- Begin report of {path} ---")
    print(f"{words_count} words found in the document\n")

    for char, count in sorted_chars:
        print(f"The '{char}' character was found {count} times")
    print("--- End report ---")
main()