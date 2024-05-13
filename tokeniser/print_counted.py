import argparse
import json

parser = argparse.ArgumentParser(description='Tokeniser')

parser.add_argument('-i', '--input', help='Path to the input file', required=True)

args = parser.parse_args()

with open(args.input, 'r') as file:
  data = json.load(file)

def create_ascii_table():
  table_string = ''
  col_one_width = max(len(x) for x in data)
  table_string += '┌' + '─' * int(col_one_width + 2) + '┬' + '─' * 5 + '┐\n'

  for key, value in data.items():
    table_string += '│ ' + key + ' ' * (col_one_width - len(key)) + ' │ ' + str(value) + ' ' * (3 - len(str(value))) + ' │\n'
    if key != list(data.keys())[-1]:
      table_string += '├' + '─' * int(col_one_width + 2) + '┼' + '─' * 5 + '┤\n'
  
  table_string += '└' + '─' * int(col_one_width + 2) + '┴' + '─' * 5 + '┘\n'

  return table_string

ascii_table = create_ascii_table()

# print(create_ascii_table())

from escpos.printer import Serial, Dummy

p = Serial(devfile='/dev/ttyUSB0',
                baudrate=19200,
                bytesize=8,
                parity='N',
                stopbits=1,
                timeout=500.00,
                dsrdtr=True,
                profile='TM-T88III')

# p = Dummy(profile='TM-T88III')

p.set(align='center')
p.text(ascii_table)
p.cut()

import sys

# print(sys.getsizeof(p.output)/8)
