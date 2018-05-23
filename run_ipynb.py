#!/usr/bin/env python
#-*-coding:utf-8-*-
import sys
import os
import nbformat
from nbconvert.preprocessors.execute import ExecutePreprocessor

input_fn = sys.argv[1]
output_fn = sys.argv[2]

timeout = 60 * 20

notebook = nbformat.read(input_fn, as_version = 4)

executor = ExecutePreprocessor(timeout=timeout)
notebook, resources = executor.preprocess(notebook, resources={})

nbformat.write(notebook, output_fn)


