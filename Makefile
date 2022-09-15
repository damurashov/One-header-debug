CC = gcc
CLEAN = *.o ohdebug

build:
	$(CC) -c -Wall main.cpp
	$(CC) -o ohdebug main.cpp -lstdc++ -fPIC

header:
	rm -f Ohdebug.hpp
	cd tools && ./ohdebuggen.py
	mv tools/OhDebug.hpp .

clean:
	rm -f $(CLEAN)

.PHONY: build header
