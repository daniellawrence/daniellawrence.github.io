#!/usr/bin/env python
"""
   Validate HTML

   $ sudo apt-get install python-tidylib
   $ ./test.py

"""
from tidylib import tidy_document


def validate_html(page):
    " Show any html errors "
    print("page: %s" % page)
    with open(page) as f:
        document, errors = tidy_document(f.read())
    if errors:
        print(errors)
    else:
        print("No Errors")

if __name__ == '__main__':
    validate_html("./index.html")
    validate_html("./things/index.html")
