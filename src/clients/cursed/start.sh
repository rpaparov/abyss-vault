#!/bin/bash
PYTHONPATH=$PYTHONPATH:../..
TERM=xterm-256color
python3 main.py $*
