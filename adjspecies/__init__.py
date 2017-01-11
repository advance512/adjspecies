# coding=utf-8
"""
Print the name of a random adjective/species, more or less…
"""

import argparse
from itertools import chain
from os import path
from random import choice
import sys


parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--sep', type=str, default='', metavar="SEPARATOR",
                    help="Separator between the adjective and species words. (default='')")
parser.add_argument('--count', type=int, default=1,
                    help="Number of adjective/species combinations to print.")
parser.add_argument('--prevent-stutter', action='store_true',
                    help="Prevent the same letter from appearing on an adjective/species boundary. "
                    "(default=True)")

_species = None
_adjectives = None

def get_file_lines(file_name):
    """Return a list of non-empty lines from `file_path`."""
    file_path = path.join(path.dirname(path.abspath(__file__)), file_name)
    with open(file_path) as file_obj:
        return [line for line in file_obj.read().splitlines() if line]

def get_adjectives():
    if _adjectives:
        return _adjectives
    else:
        return get_file_lines('adjectives.txt')

def get_species():
    if _species:
        return _species
    else:
        return get_file_lines('species.txt')

def random_species():
    """Return the name of a species at random."""
    return choice(get_species())

def random_adjective():
    """Return the name of an adjective at random."""
    return choice(get_adjectives())

def random_adjadjspecies(sep='', prevent_stutter=True):
    """
    Return a random adjective/adjective/species, separated by `sep`.
    If `prevent_stutter` is True, the last letter of the
    first item of the pair will be different from the first letter of
    the second item.
    """

    firstAdjective = random_adjective()
    secondAdjective = random_adjective()

    while firstAdjective == secondAdjective or firstAdjective[-1].upper() == secondAdjective[0]:
        secondAdjective = random_adjective()

    species = random_species()

    while secondAdjective[-1].upper() == species[0]:
        species = random_species()

    return "{}{}{}{}{}".format(firstAdjective, sep, secondAdjective, sep, species)


def main(*argv):
    args = parser.parse_args()
    for count in range(args.count):
        print(random_adjadjspecies(args.sep))


if __name__ == '__main__':
    main(sys.argv)
