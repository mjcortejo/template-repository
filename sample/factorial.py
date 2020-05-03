# Copyright (C) 2020  Mark Jethro Cortejo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""Computes the factorial of a number."""

import math

__author__ = "Mark Jethro Cortejo"
__version__ = "0.0.1"

batch_size = 16
random_seed = 42


class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"hello {self.name}"


def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * math.factorial(num - 1)


if __name__ == "__main__":
    print(factorial(3))
    person = Person("jet")
    print(person.greet())
