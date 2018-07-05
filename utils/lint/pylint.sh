#!/usr/bin/env bash

dir=$(dirname $0)

echo -e "### SHOW WARNINGS AND RECOMMENDATIONS ###\n"
find . -iname "*.py" | xargs pylint --rcfile=$dir/.pylintrc --disable=E

echo -e "### DETECT ERRORS ###\n"
find . -iname "*.py" | xargs pylint --rcfile=$dir/.pylintrc --disable=R,C,W
