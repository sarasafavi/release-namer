import yaml
import random
from argparse import ArgumentParser

def options():
    parser = ArgumentParser()
    parser.add_argument(
        '-l',
        '--letter',
        dest="letter",
        required=True,
        help="What letter should this release name start with?"
    )
    return parser.parse_args()

def get_sublist(names, letter):
    return [name for name in names if name.lower().startswith(letter)]

if __name__ == "__main__":
    with open("adjectives.yaml") as a:
        adjectives = yaml.load(a)
    with open("nouns.yaml") as m:
        nouns = yaml.load(m)

    options = options()
    letter = options.letter.lower()

    adjectives = get_sublist(adjectives, letter)
    nouns= get_sublist(nouns, letter)

    if adjectives and nouns:
        print("{} {}".format(random.choice(adjectives), random.choice(nouns)).title())
    else:
        print("Sorry, no names available for that letter. Try again.")
