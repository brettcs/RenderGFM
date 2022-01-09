#!/usr/bin/env python3

import json
import sys

import requests

from pathlib import Path

try:
    in_path = Path(sys.argv[1])
except IndexError:
    in_file = sys.stdin
else:
    in_file = in_path.open()
with in_file:
    md_src = in_file.read()
response = requests.post(
    'https://api.github.com/markdown',
    headers={
        'Accept': 'application/vnd.github.v3+json',
    },
    json={
        'text': md_src,
        'mode': 'gfm',
    },
)
response.raise_for_status()
print(response.text)
