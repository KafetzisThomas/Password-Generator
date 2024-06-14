#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Project Title: Pass-Generator (https://github.com/KafetzisThomas/Pass-Generator)
# Author / Project Owner: KafetzisThomas (https://github.com/KafetzisThomas)

import string
import secrets


def generate_password(length, include_letters, include_digits, include_special_chars):
    """Return a random password string based on the provided options"""
    letters, digits, special_chars = (
        string.ascii_letters,
        string.digits,
        string.punctuation,
    )

    selected_chars = []
    if include_letters:
        selected_chars.append(letters)
    if include_digits:
        selected_chars.append(digits)
    if include_special_chars:
        selected_chars.append(special_chars)
    alphabet = "".join(selected_chars)

    password = ""
    for _ in range(int(length)):
        password += "".join(secrets.choice(alphabet))
    return password


if __name__ == "__main__":
    length = input("Enter password length: ")
    include_letters = input("Include letters(y/N)? ")
    include_digits = input("Include digits(y/N): ")
    include_special_chars = input("Include special chars(y/N): ")

    if length.upper() == "N":
        length = False
    if include_letters.upper() == "N":
        include_letters = False
    if include_digits.upper() == "N":
        include_digits = False
    if include_special_chars.upper() == "N":
        include_special_chars = False

    print(
        f"Generated password: {generate_password(length, include_letters, include_digits, include_special_chars)}"
    )
