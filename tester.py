#!/usr/bin/env python

import requests

result = requests.get("https://www.cs.utexas.edu/~scottm/cs307/codingSamples.htm").text
f = open("java_page", "w+")
f.write(result)
