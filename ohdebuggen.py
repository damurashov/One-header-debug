#!/usr/bin/python3

ARG_NUM = 20

def main():
	for i in range(1, ARG_NUM):
		print("""\
# define ohdebug%d__(context, a, ...) OhDebug::ohdebugImpl<static_cast<unsigned>(context)>(#a, a);
	ohdebug%d__(static_cast<unsigned>(context), ## __VA_ARGS__);""" % (i, i + 1))

	print("""\
# define ohdebug%d__(context, a, ...) OhDebug::ohdebugImpl<static_cast<unsigned>(context)>(#a, a);
	ohdebugend__(static_cast<unsigned>(context), ## __VA_ARGS__);""" % (ARG_NUM))

	print(f" # define ohdebug(context, ...) ohdebug0__(context, ##__VA_ARGS__, %s)" % ', '.join(["OhDebug::Stub{}"] * ARG_NUM))

if __name__ == "__main__":
	main()
