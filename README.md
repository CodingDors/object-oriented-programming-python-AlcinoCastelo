# Simple Library System

Welcome to the "Simple Library System" exercise. This is designed to test your understanding of object-oriented programming, dictionaries, and basic regular expression validation in Python.

## Problem Description

You are to design and implement a simple library system that consists of `Book` objects and a `Library` class to manage these books.

### Requirements

1. **Book Class**:
    - Each book has the following attributes: `title`, `author`, and `id`.
    - The `id` of the book should follow a specific format: "B####", where "#" is a digit.

2. **Library Class**:
    - The library class will maintain a collection of books stored in a dictionary, using the book's `id` as the key.
    - Implement the following methods:
        - `add_book`: To add a book to the library.
        - `remove_book`: To remove a book from the library by its `id`. Ensure that the book ID is validated before attempting to remove the book.
        - `find_book`: To find and retrieve a book using its `id`.
        - `validate_book_id`: Validates the book's ID format using a regular expression.

## Getting Started

1. **Setting up**:
    - Ensure you have Python installed on your machine.
    - Clone this repository or download the files.
    - Navigate to the project directory in your terminal.

2. **Files**:
    - `library_system.py`: This file contains the initial stubs for the `Book` and `Library` classes.
    - `test_library_system.py`: This file contains unit tests to validate your implementation.

3. **Implementation**:
    - Open `library_system.py` in your preferred text editor or IDE.
    - Implement the methods in the `Library` class.
    - Ensure that the book ID is validated in both the `add_book` and `remove_book` methods.

4. **Testing**:
    - Run the tests using the command: `python test_library_system.py`
    - Ensure all tests pass to validate your solution.

5. **Submission**:
    - Once you've completed the implementation and all tests pass, follow the submission guidelines provided by your instructor.

## Tips

- Pay close attention to the requirements and ensure your `

