#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Project Title: Password-Generator (https://github.com/KafetzisThomas/Password-Generator)
# Author / Project Owner: KafetzisThomas (https://github.com/KafetzisThomas)

import secrets, string

# Define the alphabet
letters, digits, special_chars = string.ascii_letters, string.digits, string.punctuation
alphabet = letters + digits + special_chars

# Set password length
pwd_length = int(input("\nEnter password length: "))

# Generate a password string
password = ''
for i in range(pwd_length):
  password += ''.join(secrets.choice(alphabet))

print(f"Generated password: {password}")
