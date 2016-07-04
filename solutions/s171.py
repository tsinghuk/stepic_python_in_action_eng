"""
You should write a program that can transform some units of measurement into
others.

The following transformations should be supported:

    miles (1 mile = 1609 m),
    yards (1 yard = 0.9144 m),
    feet (1 foot = 30.48 cm),
    inches (1 inch = 2.54 cm),
    kilometres (1 km = 1000 m),
    meters (m),
    centimetres (1 cm = 0.01 m)
    millimetres (1 mm = 0.001 m)

Use the units of measurement specified in the problem description with the
exact specified accuracy.

Input format:
Single line in the following format:
<number> <unit_from> in <unit_to>
For example: if you get the line "15.5 mile in km", then you should transform
15.5 miles into kilometers.

Output format:
Real number in scientific format (exponential), with an accuracy of exactly
two digits after decimal point.
"""


TO_METERS = {
    'mile': 1609,
    'yard': 0.9144,
    'foot': 0.3048,
    'inch': 0.0254,
    'km': 1000,
    'm': 1,
    'cm': 0.01,
    'mm': 0.001
}


def solve(command: str) -> str:
    value, base, _, goal = command.split()
    return '%.2e' % (float(value)*TO_METERS[base]/TO_METERS[goal])


def main():
    command = input().rstrip()
    print(solve(command))

if __name__ == '__main__':
    main()
