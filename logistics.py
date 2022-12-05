import sys
from time import sleep


def sprint(s):
    """
    Displaying the game in "live writing" style
    :param s: str
        A string to display
    :return: None
    """
    for letter in s:
        sys.stdout.write(letter)
        sys.stdout.flush()
        sleep(0.04)
    print()


def check_input(input_value, options):
    """
    Checks if the input is valid
    :param input_value: str
        The input value to check
    :param options: list
        A list of the valid options
    :return: str
        A valid input
    """
    while input_value not in options:
        sprint(f'{input_value} is not an option')
        input_value = input('Please try again: ')
    return input_value


def types_effect():
    """
    Define a dictionary for all the attack types and the types that are immune, resistant or super effective
    :return: dict
        The types dictionary
    """
    types_dict = {'Grass': {'resist': ('Fire', 'Grass', 'Poison', 'Flying', 'Bug', 'Dragon', 'Steel'),
                            'effective': ('Water', 'Ground', 'Rock'), 'immune': ('',)},
                  'Fire': {'resist': ('Fire', 'Water', 'Rock', 'Dragon'),
                           'effective': ('Grass', 'Ice', 'Bug', 'Steel'), 'immune':  ('',)},
                  'Water': {'resist': ('Water', 'Grass', 'Dragon'),
                            'effective': ('Fire', 'Ground', 'Rock'), 'immune': ('',)},
                  'Electric': {'resist': ('Electric', 'Grass', 'Dragon'),
                               'effective': ('Water', 'Flying'), 'immune': ('Ground',)},
                  'Normal': {'resist': ('Rock', 'Steel'), 'effective': ('',), 'immune': ('Ghost',)},
                  'Ice': {'resist': ('Fire', 'Water', 'Ice', 'Steel'),
                          'effective': ('Grass', 'Ground', 'Flying', 'Dragon'), 'immune': ('',)},
                  'Fighting': {'resist': ('Poison', 'Flying', 'Psychic', 'Bug', 'Fairy'),
                               'effective': ('Normal', 'Ice', 'Rock', 'Dark', 'Steel'), 'immune':  ('Ghost',)},
                  'Poison': {'resist': ('Poison', 'Ground', 'Rock', 'Ghost'),
                             'effective': ('Grass', 'Fairy'), 'immune': ('Steel',)},
                  'Ground': {'resist': ('Grass', 'Bug'),
                             'effective': ('Fire', 'Electric', 'Poison', 'Rock', 'Steel'), 'immune': ('Flying',)},
                  'Flying': {'resist': ('Electric', 'Rock', 'Steel'),
                             'effective': ('Grass', 'Fighting', 'Bug'), 'immune': ('',)},
                  'Psychic': {'resist': ('Psychic', 'Steel'), 'effective': ('Fighting', 'Poison'), 'immune': ('Dark',)},
                  'Bug': {'resist': ('Fire', 'Fighting', 'Poison', 'Flying', 'Ghost', 'Steel', 'Fairy'),
                          'effective': ('Grass', 'Psychic', 'Dark'), 'immune': ('',)},
                  'Rock': {'resist': ('Fighting', 'Ground', 'Steel'),
                           'effective': ('Fire', 'Ice', 'Flying', 'Bug'), 'immune': ('',)},
                  'Ghost': {'resist': ('Dark',), 'effective': ('Psychic', 'Ghost'), 'immune': ('Normal',)},
                  'Dragon': {'resist': ('Steel',), 'effective': ('Dragon',), 'immune': ('Fairy',)},
                  'Dark': {'resist': ('Fighting', 'Dark', 'Fairy'), 'effective': ('Psychic', 'Ghost'), 'immune': ('',)},
                  'Steel': {'resist': ('Fire', 'Water', 'Electric', 'Steel'),
                            'effective': ('Ice', 'Rock', 'Fairy'), 'immune': ('',)},
                  'Fairy': {'resist': ('Fire', 'Poison', 'Steel'),
                            'effective': ('Fighting', 'Dragon', 'Dark'), 'immune': ('',)}}
    return types_dict
