#!/usr/bin/env python3
# juic3b0x 2024 - yaml_to_json.py

import sys
import json
import yaml

# Function to print error messages
def err(message):
    print(f"Error: {message}", file=sys.stderr)

# Function to load YAML data from file
def load_yaml(file_path):
    try:
        with open(file_path, 'r') as file:
            yaml_data = yaml.safe_load(file)
        return yaml_data
    except Exception as e:
        err(f"Error loading YAML file: {e}")
        sys.exit(1)

# Function to convert YAML data to JSON
def yaml_to_json(yaml_data):
    try:
        json_data = json.dumps(yaml_data, indent=4)
        return json_data
    except Exception as e:
        err(f"Error converting YAML to JSON: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] != '-i':
        err("Usage: python yaml_to_json.py -i <input_yaml_file>")
        sys.exit(1)

    input_yaml_file = sys.argv[2]

    # Load YAML data
    yaml_data = load_yaml(input_yaml_file)

    # Convert YAML to JSON
    json_data = yaml_to_json(yaml_data)

    # Print JSON data
    print(json_data)
