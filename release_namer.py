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

    parser.add_argument(
        '-a',
        '--adjectives',
        dest="adjectives",
        default="adjectives.txt",
        help="Path to text file containing adjectives"
    )

    parser.add_argument(
        '-n',
        '--nouns',
        dest="nouns",
        default="nouns.txt",
        help="Path to text file containing nouns"
    )
    return parser.parse_args()


def get_sublist(names, letter):
    return [name for name in names if name.lower().startswith(letter)]

if __name__ == "__main__":
    options = options()
    letter = options.letter.lower()

    with open(options.adjectives) as a:
        adjectives = [line.rstrip() for line in a]
    with open(options.nouns) as n:
        nouns = [line.rstrip() for line in n]

    adjectives = get_sublist(adjectives, letter)
    nouns = get_sublist(nouns, letter)

    if adjectives and nouns:
        print("{} {}".format(random.choice(adjectives),
                             random.choice(nouns)).title())
    else:
        print("Sorry, no names available for that letter. Try again.")
