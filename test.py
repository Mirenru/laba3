import unittest
from search import validate_snils, find_snils_in_text
class TestSnilsValidator(unittest.TestCase):

    def test_valid_snils(self):
        self.assertTrue(validate_snils("123-456-789 12"))
        self.assertTrue(validate_snils("987-654-321 34"))

    def test_invalid_snils(self):
        self.assertFalse(validate_snils("123-456-789 123"))   # Слишком много цифр в последнем блоке
        self.assertFalse(validate_snils("123-456-78 12"))     # Недостаточно цифр в третьем блоке
        self.assertFalse(validate_snils("12345678912"))       # Отсутствуют дефисы
        self.assertFalse(validate_snils("123-abc-789 12"))    # Присутствуют буквы вместо цифр

    def test_find_snils_in_text(self):
        text = "Мой СНИЛС: 123-456-789 12, а ваш? 987-654-321 34"
        self.assertEqual(find_snils_in_text(text), ["123-456-789 12", "987-654-321 34"])

    def test_find_snils_in_empty_text(self):
        self.assertEqual(find_snils_in_text(""), [])

if __name__ == "__main__":
    unittest.main()
