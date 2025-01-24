import unittest
from city_functions import city_country

#Tests city_country function
class test_city_country(unittest.TestCase):
    def test_city_country(self):
        formatted_city = city_country("Indianapolis", "United States")
        self.assertEqual(formatted_city, "Indianapolis, United States")

        formatted_city = city_country("Berlin", "Germany")
        self.assertEqual(formatted_city, "Berlin, Germany")

        formatted_city = city_country("Tokyo", "Japan")
        self.assertEqual(formatted_city, "Tokyo, Japan")

if __name__ == '__main__':
    unittest.main()