#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from flake8.main import application

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
            # the file statuses, plus one to separate them from the path file
            line_clean = line[8:]

            # We also remove '\n' if it is at the end of the line
            line_clean = line_clean.replace('\n', '')

            python_files.append(line_clean)

app = application.Application()
app.run(python_files)
app.exit()
