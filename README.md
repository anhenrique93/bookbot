# BookBot

**BookBot** is a simple Python command-line program that analyzes a text file (like a book) and reports useful statistics about it.  
It counts the total number of words and displays how many times each character appears in the text.

---

## Features

- Reads and analyzes any `.txt` file.
- Counts the total number of words.
- Counts how many times each character appears (case-insensitive).
- Displays results sorted by character frequency.
- Simple command-line interface.

---

## How It Works

1. **Input:**  
   You run the program and pass the path to a text file as an argument:
   ```bash
   python3 main.py books/frankenstein.txt