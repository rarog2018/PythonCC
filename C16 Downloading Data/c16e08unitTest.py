#! python3
# c16e08unitTest - tests get_country_code() from exercise 05

import unittest
from c16e05allCountries import get_country_code


class CodesTestCase(unittest.TestCase):
    """ Tests for c16e05allCountries.py """

    def test_get_country_code(self):
        # check if the function correctly "extracts" compound country name (,)
        countryCode = get_country_code("Yemen, Republic of")
        self.assertEqual(countryCode, "ye")

        # check if the function deals with one word country names
        countryCode = get_country_code("Poland")
        self.assertEqual(countryCode, "pl")

        # check if the function deals with two word country names
        countryCode = get_country_code("United Kingdom")
        self.assertEqual(countryCode, "gb")


unittest.main()
