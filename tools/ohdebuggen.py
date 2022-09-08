#!/usr/bin/python3

ARG_NUM = 20

def gen():
	for i in range(1, ARG_NUM):
		yield """\
# define ohdebug%d__(context, a, ...) OhDebug::ohdebugImpl<static_cast<unsigned>(context)>(#a, a); \\
	ohdebug%d__(static_cast<unsigned>(context), ## __VA_ARGS__);
""" % (i, i + 1)

	yield """\
# define ohdebug%d__(context, a, ...) OhDebug::ohdebugImpl<static_cast<unsigned>(context)>(#a, a); \\
	ohdebugend__(static_cast<unsigned>(context), ## __VA_ARGS__);
""" % (ARG_NUM)

	yield f" # define ohdebug(context, ...) ohdebug0__(context, ##__VA_ARGS__, %s)\n" % ', '.join(["OhDebug::Stub{}"] * ARG_NUM)


def main():
	with open("generated", 'w') as f:
		for g in gen():
			f.write(g)


if __name__ == "__main__":
	main()