#!/usr/bin/python3

import pathlib
import os
import sys

ARG_NUM = 7
FILEIN = "OhDebug.in"
FILEOUT = "OhDebug.hpp"


def append_file(appendix, fname, erase=True):

	if not os.path.exists(fname):
		mode = 0o774
		path = pathlib.Path(str(fname)).parent.resolve()

		if pathlib.Path(__file__).parent.resolve() != path and not os.path.exists(path):
			os.makedirs(str(path), mode)

		with open(fname, 'w') as f:
			pass

	if erase:
		with open(fname, 'w') as f:
			pass

	with open(fname, "a") as f:
		f.write(appendix)



def file_configure_append(filein, markermap: dict, fileout=None):
	with open(str(pathlib.Path(filein).resolve()), 'r') as f:
		content = f.read()

	for k, v in markermap.items():
		content = content.replace(k, v)

	if fileout is not None:
		append_file(content, pathlib.Path(fileout).resolve())

	return content


def generate_stubs():
	def generate_stubs_iter():
		yield f"\n// Debug stubs \n"

		map_args = map(lambda i: "arg%d" % i, range(ARG_NUM))
		map_args_void = map(lambda i: "(void)arg%d" % i, range(ARG_NUM))

		yield "#define ohdebugstubimpl_(%s, ...) \\\n\tdo {%s;} while(0)\n" % (", ".join(map_args), "; ".join(map_args_void))
		yield "#define ohdebugstub_(...) ohdebugstubimpl_( __VA_ARGS__, %s)\n" % (', '.join(["OhDebug::Stub{}"] * (ARG_NUM + 1)))

	return ''.join(generate_stubs_iter())


def generate_ohdebugimpls():
	def generate_ohdebugimpls_iter():
		for i in range(1, ARG_NUM):
			yield """\
# define ohdebug%d__(context, a, ...) OhDebug::ohdebugImpl<static_cast<unsigned>(context)>(#a, a); \\
	ohdebug%d__(static_cast<unsigned>(context), ## __VA_ARGS__);
""" % (i, i + 1)

		yield """\
# define ohdebug%d__(context, a, ...) OhDebug::ohdebugImpl<static_cast<unsigned>(context)>(#a, a); \\
	ohdebugend__(static_cast<unsigned>(context), ## __VA_ARGS__);
""" % (ARG_NUM)

		yield "#define ohdebug(...) ohdebug0__(__VA_ARGS__, %s)\n" % (', '.join(["OhDebug::Stub{}"] * (ARG_NUM + 1)))

	return ''.join(generate_ohdebugimpls_iter())


def configure():
	markermap = {
		"@OHDEBUG_STUBS@": generate_stubs(),
		"@OHDEBUG_IMPLS@": generate_ohdebugimpls(),
	}
	file_configure_append(FILEIN, markermap, FILEOUT)


def main():
	configure()


if __name__ == "__main__":
	main()
