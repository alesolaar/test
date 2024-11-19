# Archivo: test_string_utils.py

import unittest
from string_utils import reverse_string, capitalize_string, is_capitalized

class TestStringUtils(unittest.TestCase):

    # Prueba para reverse_string
    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")  # Verifica que la cadena se invierta correctamente
        self.assertEqual(reverse_string("Python"), "nohtyP")  # Caso adicional

    # Prueba para capitalize_string
    def test_capitalize_string(self):
        self.assertEqual(capitalize_string("hello"), "Hello")  # Verifica que se capitalice correctamente
        self.assertEqual(capitalize_string("PYTHON"), "Python")  # Caso con todas mayúsculas

    # Prueba para is_capitalized
    def test_is_capitalized(self):
        self.assertTrue(is_capitalized("Hello"))  # Verifica que la cadena empiece con mayúscula
        self.assertFalse(is_capitalized("hello"))  # Verifica que no empiece con mayúscula
        self.assertTrue(is_capitalized("Python"))  # Otro caso válido

if __name__ == '__main__':
    unittest.main()
