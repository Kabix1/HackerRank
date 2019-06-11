#!usr/bin/env python

import re
import requests
import os
import sys

base = "https://www.cs.utexas.edu/~scottm/cs307"

def get_all_matches(pattern, text):
    regexp = re.compile(pattern)
    matches = regexp.findall(text)
    return matches

def is_java(text):
    pattern1 = ";$"
    if re.search(pattern1, text, re.M):
        return True

def is_c(text):
    pattern_include = "^#include <.*>"
    if re.search(pattern_include, text, re.M):
        return True

def is_python(text):
    pattern1 = ":$"
    if re.search(pattern1, text, re.M):
        return True

def check_files(path):
    files = os.listdir(path)
    count = {"c": 0, "java": 0, "python": 0}
    total = len(files)
    for f in files:
        try:
            code = open("{}/{}".format(path,f), "r").read()
        except:
            total -= 1
            continue
        if is_c(code):
            count["c"] += 1
        if is_python(code):
            count["python"] += 1
        # if is_java(code):
        #     count["java"] += 1
    for key, value in count.items():
        print("{}: {}/{}".format(key, count[key], total))


# links_pattern = r"<a [^>]*href=\"([^>\"]*).*?>([^\"<>]*)</"
links_pattern = r"<a [^>]*href=\"([^>\"]*/([^/]*\.java))"
tags_pattern = r"<([^<> \t/]+)"


print("Testing c code")
check_files("tests/c_code")
print("Testing java code")
check_files("tests/java_code")
print("Testing python code")
check_files("tests/python_code")
# example = open("java_page", "r").read()
# links = get_all_matches(links_pattern, example)
# links = get_all_matches(links_pattern, example)
