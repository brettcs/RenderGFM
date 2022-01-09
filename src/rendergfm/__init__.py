# This file is part of RenderGFM
#   <https://brettcsmith.org/RenderGFM>
# Copyright © 2022 Brett Smith <brettcsmith@brettcsmith.org>
# You may use, share, and modify this software under the terms of the
# Apache License 2.0
#   <https://opensource.org/licenses/Apache-2.0>

import logging

import requests

from urllib import parse as urlparse

from typing import (
    NamedTuple,
    Optional,
)

logger = logging.getLogger('RenderGFM')

class _Version(NamedTuple):
    major: int
    minor: int
    micro: int = 0

    def __str__(self) -> str:
        return '.'.join(str(n) for n in self)
VERSION = _Version(0, 1)


class GitHubV3MarkdownRenderer:
    API_ROOT = 'https://api.github.com/'
    API_PATH = 'markdown'

    def __init__(self, url: Optional[str]=None) -> None:
        if url is None:
            url = urlparse.urljoin(self.API_ROOT, self.API_PATH)
        self.url = url
        self.headers = requests.utils.default_headers()
        self.headers['Accept'] = 'application/vnd.github.v3+json'
        self.headers['User-Agent'] = f"RenderGFM/{VERSION} ({self.headers['User-Agent']})"

    def render(self, markdown: str) -> requests.Response:
        return requests.post(
            self.url, headers=self.headers, json={
                'mode': 'gfm',
                'text': markdown,
            },
        )
