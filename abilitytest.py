#!/usr/bin/env python3

from random import Random
import sys

abilities = 'Str', 'Dex', 'Con', 'Int', 'Wis', 'Cha'


def abilityScore(rng):
    return sum(sorted(rng.randrange(6) + 1 for _ in range(4))[1:])


def character(rng):
    return sorted((abilityScore(rng) for _ in range(6)), reverse=True)


def printCharacter(c):
    for ability, score in zip(abilities, c):
        print(f'{ability} {score:2d}')


def main(n):
    bestCharacter = [0] * 6
    rng = Random(1)
    for i in range(int(n)):
        c = character(rng)
        # score = sum(c)
        if c > bestCharacter:
            bestCharacter = c
            print(f'Trial {i:3d}')
            print(c)


if __name__ == '__main__':
    main(sys.argv[1])
