# pylint: disable=invalid-name

"""Floor-space of the room

Residents of the Malevia country often experiment with the plan of their rooms.
Rooms can be triangular, rectangular and round. To quickly calculate the
floorage it is required to write a program, which gets the type of the room
shape and the relevant parameters as input - the program should output the area
of the resulting room.

The value of 3.14 is used instead of the number π in Malevia.

Input format used by the Malevians:
    triangle
    a
    b
    c
where a, b and c — lengths of the triangle sides.

    rectangle
    a
    b
where a and b —lengths of the rectangle sides.

    circle
    r
where r — circle radius.

Sample Input 1:
    rectangle
    4
    10
Sample Output 1:
    40.0

Sample Input 2:
    circle
    5
Sample Output 2:
    78.5

Sample Input 3:
    triangle
    3
    4
    5
Sample Output 3:
    6.0
"""

import math
import sys


def square(room_type, data):
    if room_type == 'triangle':
        a, b, c = data
        p = (a + b + c)/2
        s = math.sqrt(p*(p - a)*(p - b)*(p - c))
    elif room_type == 'circle':
        r = data[0]
        s = 3.14*r**2
    elif room_type == 'rectangle':
        a, b = data
        s = a*b
    else:
        s = 0
    if s % 1 == 0:
        return '%0.1f' % s if s else '0'
    else:
        return str(s)


def main():
    room_type = input().rstrip()
    data = []

    for arg in sys.stdin:
        data.append(float(arg.rstrip()))

    result = square(room_type, data)
    print(result)

if __name__ == '__main__':
    main()
