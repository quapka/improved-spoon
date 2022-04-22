#!/usr/bin/env python3

import argparse
import pathlib
import os

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

parser = argparse.ArgumentParser()
parser.add_argument(
    "-p", "--filepath", type=pathlib.Path, help="The file to be encrypted"
)
args = parser.parse_args()

key = os.urandom(32)
iv = os.urandom(16)
cipher = Cipher(algorithms.AES(key), modes.CBC(iv))


with open(args.filepath, "rb") as handle:
    encryptor = cipher.encryptor()
    ct = encryptor.update(handle.read()) + encryptor.finalize()
