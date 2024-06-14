#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Project Title: pass-generator (https://github.com/KafetzisThomas/pass-generator)
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
