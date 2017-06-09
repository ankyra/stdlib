#!/bin/bash

export PYTHONPATH="`pwd`:$PYTHONPATH"
python -m unittest discover -s tests
