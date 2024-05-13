import sys
import argparse
import json

from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline, TextIteratorStreamer
# from exllama 
from auto_gptq import exllama_set_max_input_length
from threading import Thread

# Create an argument parser
parser = argparse.ArgumentParser(description='Tokeniser')

# Add optional arguments
parser.add_argument('-if','--input', help='Text file to use as a prompt')
parser.add_argument('-p','--prompt', help='String prompt')
parser.add_argument('-c','--count-tokens', action='store_true', help='Print the amount of tokens, then exit')
parser.add_argument('-of','--output', help='Text file to write tokens to, if not provided, tokens will be printed to the console')

# Parse the command line arguments
args = parser.parse_args()

# exit if both --input and --prompt are provided
if args.input and args.prompt:
  print('Please provide only one of --input or --prompt argument')
  sys.exit(1)

# Check if --input argument is provided
if args.input:
  # Read the prompt from the file
  with open(args.input, 'r') as input:
    prompt = input.read().replace('\n', '')
    print('Prompt length:', len(prompt))
elif args.prompt:
  # Use the provided string prompt
  prompt = args.prompt
else:
  print('Please provide either --file or --prompt argument')
  sys.exit(1)

# Define and load the model
model_name_or_path = "TheBloke/CapybaraHermes-2.5-Mistral-7B-GPTQ"
model = AutoModelForCausalLM.from_pretrained(model_name_or_path,
                                             device_map="auto",
                                             trust_remote_code=False,
                                             revision="main")

# Load the tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name_or_path)
# Increase the max input length
model = exllama_set_max_input_length(model, 30000)

# Tokenize the prompt
tokens = tokenizer(prompt, return_tensors='pt')

# Convert the token IDs to tokens
labels = [tokenizer.convert_ids_to_tokens(id) for id in tokens.input_ids[0].tolist()]


filtered_labels = [label for label in labels if not (label.startswith('<') and label.endswith('>'))]
block_removed_list = [label.replace('▁', '') for label in filtered_labels]

print('\n---\n')
print('Number of tokens: ' + str(len(block_removed_list)))
print('\n---\n')

# Check if --count-tokens argument is provided
if args.count_tokens:
  sys.exit(0)

# Check if --output argument is provided
if args.output:
  if ".json" in args.output:
    # Write the tokens to the file in JSON format
    with open(args.output, 'w') as output:
      output.write(json.dumps(block_removed_list))
      print('Tokens written to:', args.output)
  else:
    # Write the tokens to the file
    with open(args.output, 'w') as output:
      output.write('\n'.join(block_removed_list))
      print('Tokens written to:', args.output)
else:
  # Print the tokens to the console
  print('\n'.join(block_removed_list))