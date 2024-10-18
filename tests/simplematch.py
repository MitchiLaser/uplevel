#!/usr/bin/env python3

import re
from uplevel import upset


def simplematch(regex, string):
    results = re.match(regex, string)
    upset(1, 'match', results)
    return results


if simplematch(r"[abc]+", "abc123"):
    print(f"Matched: {match.group(0)}")
