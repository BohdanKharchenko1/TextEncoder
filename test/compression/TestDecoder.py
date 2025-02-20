import unittest
from src.compression.logic.Decoder import Decoder


class TestDecoder(unittest.TestCase):
    def test_decode_empty_data(self):
        # Test decoding an empty list should return an empty string
        decoder = Decoder()
        decoded_result = decoder.decode([])
        self.assertEqual(decoded_result, "")

    def test_decode_single_character(self):
        # Test decoding a list with a single ASCII code
        decoder = Decoder()
        decoded_result = decoder.decode([65])
        self.assertEqual(decoded_result, "A")

    def test_decode_error_handling(self):
        # Test if the decoder gracefully handles errors during decoding
        decoder = Decoder()
        # Providing a non-list input should return an empty string
        decoded_result = decoder.decode("ABC")
        self.assertEqual(decoded_result, "")
