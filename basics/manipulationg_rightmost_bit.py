#!/bin/python

reverse_mapping = {
    'x': 'x',
    '~x': '~x',
    'x + 1': 'x - 1',
    'x - 1': 'x + 1',
    '|': '&',
    '&': '|',
    '-x': '~(x + 1)'
}


def print_formula(prefix, desc, x):
    print('\n# ' + desc)
    print('x: {0:08b}, {0}'.format(x))
    result = eval(formula)
    print(prefix + ": {0:08b}".format(result))


def reverse(formula_str):
    result_formula = formula_str
    for key in reverse_mapping.keys():
        value = reverse_mapping[key]
        result_formula = result_formula.replace(key, value)
    return result_formula


x = 0b01000000
desc = "turn off the right most 1-bit, returns zero if number power of 2"
formula = 'x & (x - 1)'
print_formula(formula, desc, x)

x = 63
desc = "returns zero if number (power of 2) - 1"
formula = 'x & (x + 1)'
print_formula(formula, desc, x)

x = 0b01011000
desc = "isolate the right most 1-bit, produce zero if none"
formula = 'x & (-x)'
print_formula(formula, desc, x)

x = 0b01011000
desc = "isolate the right most 0-bit, produce zero if none reversed"
formula = reverse(formula)
print_formula(formula, desc, x)

x = 0b01011000
desc = "isolate the right most 0-bit, produce zero if none"
formula = '~x & (x + 1)'
print_formula(formula, desc, x)

x = 0b01011000
desc = "mask that identifies the trailing 0's, zero if x = 0"  # or following formulas: ~(x | -x), (x & -x) - 1
formula = '~x & (x - 1)'
print_formula(formula, desc, x)

x = 0b01011111
desc = "mask that identifies the trailing 1's, zero if x = 0 reversed the above formula"
formula = reverse(formula)
print_formula(formula, desc, x)

x = 0b01011000
desc = "mask that identifies the trailing 0's and right most 1-bit, zero if x = 0"
formula = 'x ^ (x - 1)'
print_formula(formula, desc, x)

x = 0b01011011
desc = "turn off the rightmost contiguous string of 1-bit"
formula = '((x | (x - 1)) + 1) & x'
print_formula(formula, desc, x)

# when we do this reverse_mapping conversations for given formula, we have valid formula for 0-bit version of formulas

# applying for the last two formula

x = 0b01011011
desc = 'turn on the right most 0-bit in a word'
formula = 'x | (x + 1)'
print_formula(formula, desc, x)
