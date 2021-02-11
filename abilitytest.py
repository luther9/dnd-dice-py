#!/usr/bin/env python3

# Copyright 2019, 2021 Luther Thompson

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License (GPL3) as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# You have the following additional permission: You may convey the program in
# object code form under the terms of sections 4 and 5 of GPL3 without being
# bound by section 6 of GPL3.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

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
    bestCharacter = []
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
