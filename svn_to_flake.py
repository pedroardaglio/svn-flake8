#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

PYTHON_FILE_EXTENSIONS = [
    '.py'
]

svn_lines = sys.stdin.readlines()

python_files = []

for line in svn_lines:
    for file_ext in PYTHON_FILE_EXTENSIONS:
        if file_ext in line:
            # We need to remove all junk from this line.
            # From SVN, the seven first characters/column of each line are
            # the file statuses, plus one to separate them from the path file,
            # so we take them off
            line_clean = line[8:]

            # We also remove '\n' if it is at the end of the line
            line_clean = line.replace('\n', '')

            python_files.append(line_clean)

print python_files
