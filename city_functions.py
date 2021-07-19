# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 18:08:17 2021

@author: 15403
"""

def formatted_city_country(city, country, population= ''):
    """Return a string like 'Orlando, Florida'."""
    if population:
        return f"{city.title()}, {country.title()} - population {population}"
    else:
        return f"{city.title()}, {country.title()}"
    

