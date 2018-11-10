import unittest
from city_functions import city_country
class CitiesTestCase(unittest.TestCase):
    def test_cities(self):
        message=city_country('santiago','chile')
        self.assertEqual(message,'Santiago,Chile')
    def test_city_country_population(self):
        message=city_country('santiago','chile',5000000)
        self.assertEqual(message,'Santiago,Chile - population 5000000')
unittest.main()