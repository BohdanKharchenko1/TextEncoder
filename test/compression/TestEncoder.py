import unittest
from src.compression.logic.Encoder import Encoder

class TestEncoder(unittest.TestCase):
    def test_encode_empty_text(self):
        # Test encoding an empty string should return an empty list
        encoder = Encoder()
        encoded_result = encoder.encode("")
        self.assertEqual(encoded_result, [])

    def test_encode_single_character(self):
        # Test encoding a single character should return its ASCII code
        encoder = Encoder()
        encoded_result = encoder.encode("A")
        self.assertEqual(encoded_result, [65])

    def test_encode_error_handling(self):
        # Test if the encoder gracefully handles errors during encoding
        encoder = Encoder()
        # Passing a non-string input (e.g., a number) should return an empty list
        encoded_result = encoder.encode(123)
        self.assertEqual(encoded_result, [])

