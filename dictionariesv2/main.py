# Do not modify these lines
from helpers import get_countries

__winc_id__ = "00a4ab32f1024f5da525307a1959958e"
__human_name__ = "dictionariesv2"

#1 Part 1: Create Passport
def create_passport(name, date_of_birth, place_of_birth, height, nationality):
    passport = {
            'name': name,
            'date_of_birth': date_of_birth,
            'place_of_birth': place_of_birth,
            'height': height,
            'nationality': nationality,
        }
    return passport

#2 Part 2: Add Stamp
def add_stamp(passport, country):
    if country != passport['nationality']:
        if 'stamps' in passport:
            if country not in passport['stamps']:
                passport['stamps'] += [country]
        else:
            passport['stamps'] = [country]
    return passport

#3 Part 3: Add biometric data
def add_biometric_data(passport, name, value, date):
    if 'biometric' not in passport:
        x = {
            'biometric': {
                name: {
                    'value': value,
                    'date': date
                    }
                }
            }
        passport.update(x)
    else:
        passport['biometric'][name] = {
                'value': value,
                'date': date
                 }
    return passport