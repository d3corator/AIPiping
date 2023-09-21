from typing import Tuple, Union
import json


def load_all_countries() -> Tuple[list]:
    country_list = []
    abv = []
    ab = []
    with open ("countries.json", "r") as json_file:
        data = json.load(json_file)
        for country in data:
            country_list.append(country['name'])
            abv.append(country['iso3'])
            ab.append(country['iso2'])
    return country_list, abv, ab


def get_validation_and_country(country_name: str) -> Tuple[bool, Union[str, None]]:
    countries = load_all_countries()
    is_valid = False
    country = None
    if country_name.capitalize() in countries[0]:
        is_valid = True
        country = country_name.capitalize()
    elif country_name.upper() in countries[1] or country_name.upper() in countries[-1]:
        is_valid = True
        country = country_name.upper()
    return is_valid, country


def get_validation_and_season(season_name: str) -> Tuple[bool, Union[str, None]]:
    season_list = ['Summer', 'Winter', 'Autumn', 'Spring']
    is_valid = False
    season = None
    if season_name.capitalize() in season_list:
        is_valid =  True
        season = season_name.capitalize()
    return is_valid, season
