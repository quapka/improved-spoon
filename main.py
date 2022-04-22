#!/usr/bin/env python3

import argparse
import pathlib
import os

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding


parser = argparse.ArgumentParser()
parser.add_argument("filepath", type=pathlib.Path, help="The file to be encrypted")
args = parser.parse_args()

key = os.urandom(32)
iv = os.urandom(16)
cipher = Cipher(algorithms.AES(key), modes.CBC(iv))


with open(args.filepath, "rb") as handle:
    data = handle.read()

padder = padding.PKCS7(128).padder()
padded_data = padder.update(data) + padder.finalize()

encryptor = cipher.encryptor()
ct = encryptor.update(padded_data) + encryptor.finalize()
