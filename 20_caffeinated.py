class CoffeeMenu:
    def __init__(self):
        self.menu = {
            'espresso': 2.50,
            'latte': 2.75,
            'cappuccino': 3.20,
            'americano': 2.70
        }

    def get_price(self, item):
        """Devuelve el precio de un ítem, o None si no está en el menú."""
        return self.menu.get(item)

    def add_item(self, item, price):
        """Añade un nuevo ítem al menú con su precio."""
        if item in self.menu:
            raise ValueError(f"{item} ya está en el menú.")
        if price <= 0:
            raise ValueError("El precio debe ser positivo.")
        self.menu[item] = price

import unittest

class TestCoffeeMenu(unittest.TestCase):
    def setUp(self):
        """Crea una nueva instancia de CoffeeMenu antes de cada prueba."""
        self.menu = CoffeeMenu()

    def tearDown(self):
        """Limpia los recursos después de cada prueba."""
        self.menu = None

    def test_get_price_existing_item(self):
        """Prueba que get_price devuelva el precio correcto para un ítem existente."""
        self.assertEqual(self.menu.get_price('latte'), 2.75)

    def test_get_price_non_existing_item(self):
        """Prueba que get_price devuelva None para un ítem que no está en el menú."""
        self.assertIsNone(self.menu.get_price('mocha'))

    def test_add_item(self):
        """Prueba que se pueda añadir un nuevo ítem al menú."""
        self.menu.add_item('mocha', 3.50)
        self.assertEqual(self.menu.get_price('mocha'), 3.50)

    def test_add_existing_item(self):
        """Prueba que añadir un ítem existente lanza un ValueError."""
        with self.assertRaises(ValueError):
            self.menu.add_item('latte', 3.00)

    def test_add_item_with_invalid_price(self):
        """Prueba que añadir un ítem con precio inválido lanza un ValueError."""
        with self.assertRaises(ValueError):
            self.menu.add_item('mocha', -1.00)

if __name__ == '__main__':
    unittest.main()
