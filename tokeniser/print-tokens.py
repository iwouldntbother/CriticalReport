import sys
import argparse
from escpos.printer import Serial, Dummy

# Create the argument parser
parser = argparse.ArgumentParser(description='Tokeniser')

# Add the required input file argument
parser.add_argument('-i', '--input', help='Path to the input file', required=True)

# Add the optional flag to print to console
parser.add_argument('-p', '--print-to-console', action='store_true', help='Print tokens to console')

parser.add_argument('-l', '--list', action='store_true', help='Print list')

parser.add_argument('-d', '--debug', help='Debug mode, dummy printer will be used', action='store_true')

# Parse the command-line arguments
args = parser.parse_args()

title = '"What moral issues stem from excessive integration of Artificial Intelligence into creative tools?"'

explanatory_text = "In AI, tokenization is the process of dividing text into smaller parts, called 'tokens.' Think of it as slicing a sentence into words and even subwords. This helps AI, especially language models, to digest and understand language efficiently. It’s a bit like organizing a jigsaw puzzle by sorting the pieces. For AI, these tokens are clues to the rules of language, aiding in tasks like translation and conversation."

# Read the input file
with open(args.input, 'r') as file:
  content = file.readlines()
  tokens = [line for line in content]

def debug_print_separator():
   print('')
   print('------------------------------------------')
   print('')

def debug_print_header(text):
    print('\033[1m')
    debug_print_paragraph(text)
    print('\033[0m')

def debug_print_paragraph(text):
    words = text.split(' ')
    line = ''
    for word in words:
        if word == '\n':
            print(line.strip())
            print('')
            line = ''
        elif len(line) + len(word) <= 42:
            line += word + ' '
        else:
            print(line.strip())
            line = word + ' '
    print(line.strip())

def debug_print_tokens(tokens):
    if args.list:
        for token in tokens:
            print(token.rstrip())
    else:
        debug_print_paragraph(', '.join([token.rstrip() for token in tokens]))

def debug_print_footer():
    print('An essay by William Westwood')
    print('https://willwestwood.me/')


# Print tokens to console if the flag is set
if args.print_to_console:
  debug_print_separator()
  debug_print_header(title)
  debug_print_separator()
  debug_print_paragraph(explanatory_text)
  debug_print_separator()
  debug_print_header('Tokens')
  debug_print_tokens(content)
  # debug_print_paragraph(str(len(tokens))+' tokens will be here')
  debug_print_separator()
  debug_print_footer()
  debug_print_separator()

  sys.exit(0)

if args.debug:
    p = Dummy(profile='TM-T88III')
else:
    p = Serial(devfile='/dev/ttyUSB0',
                baudrate=19200,
                bytesize=8,
                parity='N',
                stopbits=1,
                timeout=500.00,
                dsrdtr=True,
                profile='TM-T88III')


def print_blank_line():
    p.text('\n')

def print_separator():
   p.text('------------------------------------------\n')

def print_header(text):
    p.set(align='center', bold=True)
    print_paragraph(text)
    p.set(align='left', bold=False)

def print_paragraph(text):
    words = text.split(' ')
    line = ''
    for word in words:
        if word == '\n':
            p.text(line.strip()+'\n')
            p.text('\n')
            line = ''
        elif len(line) + len(word) <= 42:
            line += word + ' '
        else:
            p.text(line.strip() + '\n')
            line = word + ' '
    p.text(line.strip() + '\n')

def print_tokens(tokens):
    if args.list:
        for token in tokens:
            p.text(token)
    else:
        print_paragraph(', '.join([token.rstrip() for token in tokens]))

def print_footer():
    p.set(align='center')
    p.text('An essay by ')
    p.set(bold=True)
    p.text('William Westwood\n')
    p.set(bold=False)
    p.text('https://willwestwood.me/\n')

print_separator()
print_blank_line()
p.set(double_width=True, double_height=True)
print_header('A tokenised essay')
p.set(normal_textsize=True, double_width=False, double_height=False)
print_blank_line()
print_separator()
print_blank_line()
print_header('Question')
print_separator()
# print_blank_line()
print_header(title)
print_blank_line()
print_header('Explanation')
print_separator()
print_blank_line()
print_paragraph(explanatory_text)
print_blank_line()
print_header('Tokens')
print_separator()
# print_blank_line()
print_blank_line()
print_tokens(content)
# print_paragraph(str(len(tokens))+' tokens will be here')
print_blank_line()
print_separator()
print_blank_line()
print_footer()
print_blank_line()
print_separator()

p.cut()

if args.debug:
    print(p.output)
    print('Size: '+str(sys.getsizeof(p.output)))