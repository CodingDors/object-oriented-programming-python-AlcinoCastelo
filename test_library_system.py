import unittest

class TestLibrary(unittest.TestCase):
    
    def setUp(self):
        self.library = Library()
        self.valid_book = Book("Harry Potter", "J.K. Rowling", "B1234")
        self.invalid_id_book = Book("Sample Book", "Author Name", "BK123")

    def test_add_book_valid_id(self):
        self.assertTrue(self.library.add_book(self.valid_book))
        self.assertIn(self.valid_book.book_id, self.library.books)

    def test_add_book_invalid_id(self):
        self.assertFalse(self.library.add_book(self.invalid_id_book))
        self.assertNotIn(self.invalid_id_book.book_id, self.library.books)

    def test_remove_book_valid_id(self):
        self.library.add_book(self.valid_book)
        self.assertTrue(self.library.remove_book(self.valid_book.book_id))
        self.assertNotIn(self.valid_book.book_id, self.library.books)

    def test_remove_book_invalid_id(self):
        self.library.add_book(self.valid_book)
        self.assertFalse(self.library.remove_book(self.invalid_id_book.book_id))
        self.assertIn(self.valid_book.book_id, self.library.books)

    def test_find_book(self):
        self.library.add_book(self.valid_book)
        found_book = self.library.find_book(self.valid_book.book_id)
        self.assertEqual(found_book, self.valid_book)

    def test_validate_book_id(self):
        self.assertTrue(self.library.validate_book_id("B1234"))
        self.assertFalse(self.library.validate_book_id("1234"))
        self.assertFalse(self.library.validate_book_id("BK123"))
        self.assertFalse(self.library.validate_book_id("B12A3"))

if __name__ == '__main__':
    unittest.main()
