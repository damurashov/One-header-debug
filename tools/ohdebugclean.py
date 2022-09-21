#!/usr/bin/python3

"""
Scans for cpp-related files and `purges` ohdebug sentences.

Limitations.

TL;DR. (1) Start each `ohdebug` sentence on a new line. (2) split `ohdebug`
sentences between lines, if you need to - it is safe. (3) everything residing on
the same line with an `ohdebug` sentence will be purged from the file.

- It only scans files listed in `CPP_FILES_EXTENSIONS`
- It expects that `ohdebug` statements are placed at the line beginnings and
prepended with 0 or more space / tab characters (code chunks like `int a = 42;
ohdebug(context, a)`) will be skipped.
- It scans for multiline `ohdebug` statements through counting the balance
between '(' and ')' symbols.
- If an `ohdebug` sentence (including multilined ones) is appended with another
sentence which does not pertain to the `ohdebug`, this last one will be removed
from the file as well.
"""

import argparse
import pathlib
import os
import re
import functools


CPP_FILES_EXTENSIONS = [".cpp", ".c", ".hpp", ".h", ".cc", ".cxx"]


def line_ohdebug_beginning_match(line):
	return re.match(r"^\s*ohdebug\w*\(", line) and \
		not re.match(r"^\s*ohdebugstr\(", line)

def _arg_parse():

	def path_type(s):
		return pathlib.Path(s)

	parser = argparse.ArgumentParser()
	parser.add_argument("path", type=path_type, help="Working directory")
	args = parser.parse_args()

	return args


def find_cpp_files_iter(root):
	for dirname, subdirs, files in os.walk(root):
		for fname in files:
			path = pathlib.Path(os.path.join(dirname, fname))

			if path.suffix in CPP_FILES_EXTENSIONS:
				yield path


def __test_find_cpp_files_iter(args_path):
	l = list(map(str, find_cpp_files_iter(args_path)))
	print(l)
	exit(0)


def file_lines_iter(file):
	with open(file, 'r') as f:
		return f.readlines()


def str_round_braces_balance(s, lb_prev=0, rb_prev=0):
	lb = functools.reduce(lambda counter, character: counter + int(character == '('), s, 0)
	rb = functools.reduce(lambda counter, character: counter + int(character == ')'), s, 0)

	return lb + lb_prev, rb + rb_prev


def file_lines_filter(file):
	state_search = 0
	state_balance = 1
	state = state_search
	lb, rb = 0, 0

	def state_check_reset():
		nonlocal lb, rb, state, state_search

		if lb == rb:
			lb = 0
			rb = 0
			state = state_search

	for line in file_lines_iter(str(file)):
		if state == state_search:
			if line_ohdebug_beginning_match(line):
				state = state_balance
			else:
				yield line

			lb, rb = str_round_braces_balance(line, lb, rb)
			state_check_reset()
		elif state == state_balance:
			lb, rb = str_round_braces_balance(line, lb, rb)
			state_check_reset()

		# print(line)
		# print(lb, rb, state)
		# print()


def file_rewrite(file):
	accumulated = list(file_lines_filter(file))

	with open(file, 'w') as f:
		f.write(''.join(accumulated))


def dir_rewrite_cpp_files(root_dir):
	for file in find_cpp_files_iter(root_dir):
		file_rewrite(str(file))


def main():
	args = _arg_parse()
	dir_rewrite_cpp_files(args.path)


if __name__ == "__main__":
	main()
