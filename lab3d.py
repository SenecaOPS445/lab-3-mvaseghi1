#!/usr/bin/env python3
# Author: Mohammad Vaseghi
# Author ID: 130349228
# Date Created: 2025/01/31

import os

def free_space():
    output = os.popen("df -h | grep '/$' | awk '{print $4}'").read() # This function executes the following Linux command
    return output.strip() #strip() is a Python string method that removes leading and trailing whitespace characters

# Example usage
if __name__ == "__main__":
    print("Free disk space on root directory:", free_space())

