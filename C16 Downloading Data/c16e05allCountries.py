#!python3
# c16e05allCountries - adds the countries that were omitted by first version
# of this function

from pygal.maps.world import COUNTRIES


def get_country_code(countryName):
    """Return the Pygal 2-digit country code for the given country."""

    for code, name in COUNTRIES.items():
        if name == countryName:
            return code
        # checks if first part of the country name is in a list created by
        # splitting the name variable. It adds f.e. Yemen, Re
        elif countryName.split(',')[0] in name.split(','):
            return code
    # If the country wasn't found, return None.
    return None
