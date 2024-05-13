# from escpos.printer import Serial

# p = Serial(devfile='/dev/ttyUSB0',
#                baudrate=19200,
#                bytesize=8,
#                parity='N',
#                stopbits=1,
#                timeout=500.00,
#                dsrdtr=True,
#                profile='TM-T88III')

# p.text('The line below this should have no gap\n')

import sys
import json
import argparse
import numpy as np

# Create the argument parser
parser = argparse.ArgumentParser(description='Tokeniser')

# Add the required input file argument
parser.add_argument('-i', '--input', help='Path to the input file', required=True)

# Parse the command-line arguments
args = parser.parse_args()


with open(args.input, 'r') as file:
  content = file.readlines()
  data = [line.strip() for line in content]

print(data[:5])
print(len(data))

# Split the list into 10 equal sections
sections = np.array_split(data, 10)


# # Save each section to a txt file
# for i, section in enumerate(sections):
#   with open(f'sections/section-{i+1}.txt', 'w') as file:
#     file.write('\n'.join(map(str, section)))

counted = {}

for item in data:
  item = item.strip()
  if item in counted:
    counted[item] += 1
  else:
    counted[item] = 1

counted_sorted = dict(sorted(counted.items(), key=lambda item: item[1], reverse=True))

print(len(counted_sorted))


with open('counted.json', 'w') as file:
  file.write(json.dumps(counted_sorted))
  # for key, value in counted.items():
    # file.write(f'"{key}": {value}\n')