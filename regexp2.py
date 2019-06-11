#!/usr/bin/env python

import re

input1 = ["foo----foo--fo-fo-foo-foo"]
input2 = ["foo", "bar", "foofoo"]

line = ""
search_words = []
for i in range(len(input1)):
    line += "*{}*".format(input1[i])
for i in range(len(input2)):
    search_words.append(input2[i])
c = "\w"
for word in search_words:
    count = 0
    count1 = len(re.findall(r"[^\w]({word})[^\w]".format(word=word, c=c), line))
    count2 = len(re.findall(r"(?<=[\W]){word}(?=[\W])".format(word=word), line))
    if count1 != count2:
        print(count1)
        print(count2)
        print(line)
