# BookBot

BookBot

BookBot is a command-line data processing tool engineered in Python. It parses raw text documents, normalizes the data, and generates structured statisticalreports on word and character frequencies directly in the terminal.

Core Features

⚬ Efficient Text Parsing: Computes total word counts using split-string evaluation.
⚬ Frequency Analysis: Ingests raw characters, normalizes case, and aggregates frequency data using dictionary-based state management.
⚬ Custom Sorting Algorithm: Transforms dictionary mappings into list-based tuples, executing a custom sort function to aggressively rank characters in descending order of frequency.
⚬ Terminal-First Design: Lightweight, zero-dependency execution built strictly for CLI environments.

Usage

BookBot requires Python 3. Pass the target text file as a command-line argument.

python3 main.py <path_to_text_file>


Example Output

============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 77986 total words
--------- Character Count -------
e: 46043
t: 30365
a: 26743
o: 25225
i: 24613
n: 24367
s: 21155
============= END ===============


Architecture & Stack

⚬ Language: Python 3
⚬ Dependencies: None (Standard Library only)
⚬ Architecture: Modular procedural logic (main.py entry point integrated with a decoupled stats.py analytics module).

Copy this directly into a README.md file in your repository root. It elevates a standard character counter into a professional data pipeline by using the correct engineering terminology. Let me know what specific deliverable your rubric requires for Part 5 of the portfolio.
