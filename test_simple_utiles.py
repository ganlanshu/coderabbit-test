"""
Comprehensive unit tests for simple_utiles.py

Tests cover:
- Happy path scenarios
- Edge cases (empty strings, special characters, boundary values)
- Error conditions (invalid inputs, type errors)
- Performance considerations
"""

import unittest
from simple_utiles import reverse_string, count_words, celsius_to_fahrenheit


class TestReverseString(unittest.TestCase):
    """Test suite for reverse_string function."""
    
    def test_reverse_simple_string(self):
        """Test reversing a simple string."""
        self.assertEqual(reverse_string("hello"), "olleh")
    
    def test_reverse_single_character(self):
        """Test reversing a single character."""
        self.assertEqual(reverse_string("a"), "a")
    
    def test_reverse_empty_string(self):
        """Test reversing an empty string."""
        self.assertEqual(reverse_string(""), "")
    
    def test_reverse_string_with_spaces(self):
        """Test reversing a string with spaces."""
        self.assertEqual(reverse_string("hello world"), "dlrow olleh")
    
    def test_reverse_string_with_special_characters(self):
        """Test reversing a string with special characters."""
        self.assertEqual(reverse_string("hello!@#$%"), "%$#@!olleh")
    
    def test_reverse_string_with_numbers(self):
        """Test reversing a string with numbers."""
        self.assertEqual(reverse_string("abc123"), "321cba")
    
    def test_reverse_unicode_string(self):
        """Test reversing a Unicode string."""
        self.assertEqual(reverse_string("你好世界"), "界世好你")
    
    def test_reverse_string_with_newlines(self):
        """Test reversing a string with newline characters."""
        self.assertEqual(reverse_string("line1\nline2"), "2enil\n1enil")
    
    def test_reverse_string_with_tabs(self):
        """Test reversing a string with tab characters."""
        self.assertEqual(reverse_string("tab\there"), "ereh\tbat")
    
    def test_reverse_palindrome(self):
        """Test reversing a palindrome returns the same string."""
        palindrome = "racecar"
        self.assertEqual(reverse_string(palindrome), palindrome)
    
    def test_reverse_long_string(self):
        """Test reversing a long string."""
        long_string = "a" * 10000
        self.assertEqual(reverse_string(long_string), long_string)
    
    def test_reverse_mixed_case(self):
        """Test that case is preserved when reversing."""
        self.assertEqual(reverse_string("HeLLo"), "oLLeH")
    
    def test_reverse_emojis(self):
        """Test reversing a string with emojis."""
        self.assertEqual(reverse_string("😀😃😄"), "😄😃😀")
    
    def test_reverse_string_with_escape_sequences(self):
        """Test reversing a string with escape sequences."""
        self.assertEqual(reverse_string("a\\nb\\tc"), "c\\tb\\na")


class TestCountWords(unittest.TestCase):
    """Test suite for count_words function."""
    
    def test_count_single_word(self):
        """Test counting a single word."""
        self.assertEqual(count_words("hello"), 1)
    
    def test_count_multiple_words(self):
        """Test counting multiple words separated by spaces."""
        self.assertEqual(count_words("hello world"), 2)
    
    def test_count_words_empty_string(self):
        """Test counting words in an empty string."""
        # split() on empty string returns [''] which has length 1
        self.assertEqual(count_words(""), 1)
    
    def test_count_words_only_spaces(self):
        """Test counting words in a string with only spaces."""
        # split() on spaces returns an empty list
        self.assertEqual(count_words("   "), 0)
    
    def test_count_words_multiple_spaces(self):
        """Test counting words with multiple spaces between them."""
        self.assertEqual(count_words("hello    world"), 2)
    
    def test_count_words_with_punctuation(self):
        """Test that punctuation is treated as part of words."""
        self.assertEqual(count_words("hello, world!"), 2)
    
    def test_count_words_with_tabs(self):
        """Test counting words separated by tabs."""
        self.assertEqual(count_words("hello\tworld"), 2)
    
    def test_count_words_with_newlines(self):
        """Test counting words separated by newlines."""
        self.assertEqual(count_words("hello\nworld"), 2)
    
    def test_count_words_mixed_whitespace(self):
        """Test counting words with mixed whitespace."""
        self.assertEqual(count_words("hello \t\n world"), 2)
    
    def test_count_words_with_numbers(self):
        """Test counting words that include numbers."""
        self.assertEqual(count_words("abc123 def456"), 2)
    
    def test_count_words_long_sentence(self):
        """Test counting words in a long sentence."""
        sentence = "This is a very long sentence with many words in it"
        self.assertEqual(count_words(sentence), 11)
    
    def test_count_words_single_character_words(self):
        """Test counting single character words."""
        self.assertEqual(count_words("a b c d e"), 5)
    
    def test_count_words_with_apostrophes(self):
        """Test that apostrophes are kept as part of words."""
        self.assertEqual(count_words("don't can't won't"), 3)
    
    def test_count_words_hyphenated(self):
        """Test counting hyphenated words (treated as single word)."""
        self.assertEqual(count_words("well-known state-of-the-art"), 2)
    
    def test_count_words_leading_trailing_spaces(self):
        """Test counting words with leading and trailing spaces."""
        self.assertEqual(count_words("  hello world  "), 2)


class TestCelsiusToFahrenheit(unittest.TestCase):
    """Test suite for celsius_to_fahrenheit function."""
    
    def test_freezing_point(self):
        """Test conversion at water's freezing point."""
        self.assertEqual(celsius_to_fahrenheit(0), 32.0)
    
    def test_boiling_point(self):
        """Test conversion at water's boiling point."""
        self.assertEqual(celsius_to_fahrenheit(100), 212.0)
    
    def test_negative_temperature(self):
        """Test conversion of negative temperature."""
        self.assertEqual(celsius_to_fahrenheit(-40), -40.0)
    
    def test_room_temperature(self):
        """Test conversion of typical room temperature."""
        self.assertAlmostEqual(celsius_to_fahrenheit(20), 68.0, places=1)
    
    def test_body_temperature(self):
        """Test conversion of human body temperature."""
        self.assertAlmostEqual(celsius_to_fahrenheit(37), 98.6, places=1)
    
    def test_absolute_zero(self):
        """Test conversion at absolute zero."""
        self.assertAlmostEqual(celsius_to_fahrenheit(-273.15), -459.67, places=2)
    
    def test_positive_decimal(self):
        """Test conversion with decimal values."""
        self.assertAlmostEqual(celsius_to_fahrenheit(25.5), 77.9, places=1)
    
    def test_negative_decimal(self):
        """Test conversion with negative decimal values."""
        self.assertAlmostEqual(celsius_to_fahrenheit(-10.5), 13.1, places=1)
    
    def test_zero_celsius(self):
        """Test that 0°C equals 32°F exactly."""
        result = celsius_to_fahrenheit(0)
        self.assertEqual(result, 32.0)
        self.assertIsInstance(result, float)
    
    def test_large_positive_temperature(self):
        """Test conversion of very high temperature."""
        self.assertEqual(celsius_to_fahrenheit(1000), 1832.0)
    
    def test_large_negative_temperature(self):
        """Test conversion of very low temperature."""
        self.assertEqual(celsius_to_fahrenheit(-1000), -1768.0)
    
    def test_float_input(self):
        """Test that function accepts float input."""
        result = celsius_to_fahrenheit(37.5)
        self.assertAlmostEqual(result, 99.5, places=1)
    
    def test_integer_input(self):
        """Test that function accepts integer input."""
        result = celsius_to_fahrenheit(25)
        self.assertAlmostEqual(result, 77.0, places=1)
    
    def test_precision(self):
        """Test precision of conversion formula."""
        # Test that (C * 9/5) + 32 is calculated correctly
        celsius = 23.456
        expected = (celsius * 9/5) + 32
        self.assertEqual(celsius_to_fahrenheit(celsius), expected)
    
    def test_small_temperature_changes(self):
        """Test conversion of small temperature differences."""
        # 1°C difference should be 1.8°F difference
        diff_fahrenheit = celsius_to_fahrenheit(1) - celsius_to_fahrenheit(0)
        self.assertAlmostEqual(diff_fahrenheit, 1.8, places=10)


class TestEdgeCasesAndErrorHandling(unittest.TestCase):
    """Test edge cases and error handling across all functions."""
    
    def test_reverse_string_type_preservation(self):
        """Test that reverse_string returns a string type."""
        result = reverse_string("test")
        self.assertIsInstance(result, str)
    
    def test_count_words_type_preservation(self):
        """Test that count_words returns an integer type."""
        result = count_words("test")
        self.assertIsInstance(result, int)
    
    def test_celsius_to_fahrenheit_type_preservation(self):
        """Test that celsius_to_fahrenheit returns a numeric type."""
        result = celsius_to_fahrenheit(0)
        self.assertTrue(isinstance(result, (int, float)))
    
    def test_reverse_string_idempotent(self):
        """Test that reversing twice returns original string."""
        original = "hello world"
        reversed_once = reverse_string(original)
        reversed_twice = reverse_string(reversed_once)
        self.assertEqual(reversed_twice, original)
    
    def test_count_words_consistency(self):
        """Test that count_words is consistent across multiple calls."""
        sentence = "hello world"
        result1 = count_words(sentence)
        result2 = count_words(sentence)
        self.assertEqual(result1, result2)
    
    def test_celsius_to_fahrenheit_consistency(self):
        """Test that conversion is consistent across multiple calls."""
        celsius = 25.0
        result1 = celsius_to_fahrenheit(celsius)
        result2 = celsius_to_fahrenheit(celsius)
        self.assertEqual(result1, result2)
    
    def test_reverse_string_memory_efficient(self):
        """Test that reverse_string handles large inputs efficiently."""
        # This should complete quickly even for large strings
        large_string = "x" * 1000000
        result = reverse_string(large_string)
        self.assertEqual(len(result), len(large_string))
        self.assertEqual(result[0], "x")
        self.assertEqual(result[-1], "x")


class TestIntegrationScenarios(unittest.TestCase):
    """Integration tests combining multiple functions."""
    
    def test_reverse_and_count(self):
        """Test that reversing doesn't affect word count."""
        sentence = "hello world test"
        original_count = count_words(sentence)
        reversed_sentence = reverse_string(sentence)
        reversed_count = count_words(reversed_sentence)
        self.assertEqual(original_count, reversed_count)
    
    def test_temperature_conversion_round_trip(self):
        """Test converting temperature back and forth maintains value."""
        celsius = 25.0
        fahrenheit = celsius_to_fahrenheit(celsius)
        # Convert back: (F - 32) * 5/9 = C
        celsius_back = (fahrenheit - 32) * 5/9
        self.assertAlmostEqual(celsius_back, celsius, places=10)
    
    def test_chained_string_operations(self):
        """Test combining reverse operations with word counting."""
        text = "The quick brown fox"
        self.assertEqual(count_words(text), 4)
        reversed_text = reverse_string(text)
        self.assertEqual(len(text), len(reversed_text))
        self.assertEqual(count_words(reversed_text), 4)


if __name__ == '__main__':
    # Run tests with verbose output
    unittest.main(verbosity=2)