# Book Analysis Tool

A Python script that reads a book from a text file, counts the words, and generates a report of character frequencies in descending order.

## Features

-   **Word Count**: Counts the total number of words in the document.
-   **Character Frequency**: Counts the occurrences of each alphabetical character, case-insensitive.
-   **Report Generation**: Prints a report with the word count and sorted character frequencies.

## Getting Started

### Prerequisites

-   Python 3.x installed on your system.

### Setup

1.  Clone the repository or download the files.
2.  Add your book text file(s) in the `books` directory. The default file path in the code is `path/to/your/book.txt`.

### Running the Script

1.  Open a terminal.
2.  Navigate to the project directory.
3.  Run the script with:

    ```
    python main.py
    ```

    or, if using `python3`:
    ```
    python3 main.py
    ```

## Sample Output

```
--- Begin report of books/frankenstein.txt --- 
77986 words found in the document  
The 'e' character was found 46043 times 
The 't' character was found 30365 times 
... 
--- End report ---
```

## Customization

-   **Changing the Book File**: Update the `book_path` variable in `main.py` to analyze a different text file.
