# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 18:43:27 2021

@author: 15403
"""

import unittest
from city_functions import formatted_city_country

class TestName(unittest.TestCase):
    """Tests for 'city_functions.py"""
    
    def test_city_state(self):
        """Does city like 'Orlando, Florida' work?"""
        format_city_country = formatted_city_country('orlando', 'florida')
        self.assertEqual(format_city_country, 'Orlando, Florida')
    def test_city_state_pop(self):
        """Does city like 'Orlando, Florida - population 6' work?"""
        format_city_country_pop = formatted_city_country('orlando', 'florida', 6)
        self.assertEqual(format_city_country_pop, 'Orlando, Florida - population 6')
        
if __name__ == '__main__':
    unittest.main()