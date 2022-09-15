CC = gcc
CLEAN = *.o ohdebug ohdebugdisable

build: header
	$(CC) -c -Wall main.cpp -DOHDEBUG_DISABLE -o maindisable.o
	$(CC) -o ohdebugdisable maindisable.o -lstdc++ -fPIC
	$(CC) -c -Wall main.cpp -o main.o
	$(CC) -o ohdebug main.o -lstdc++ -fPIC

header:
	rm -f Ohdebug.hpp
	cd tools && ./ohdebuggen.py
	mv tools/OhDebug.hpp .

clean:
	rm -f $(CLEAN)

.PHONY: build header
