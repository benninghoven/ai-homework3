#!/bin/bash

# Define the Python script and output file
python_script="main.py"
output_file="answer.txt"

# Run the Python script and capture its output
python_output=$(python3 "$python_script")

# Compare the Python output to the contents of the text file
if [ "$python_output" = "$(cat "$output_file")" ]; then
    echo "test passed"
else
    echo "test failed"
fi

