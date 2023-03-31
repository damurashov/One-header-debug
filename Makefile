CC = gcc
CLEAN = *.o ohdebug ohdebugdisable

build:
	$(CC) -c -Wall main.cpp -o main.o
	$(CC) -o ohdebug main.o -lstdc++ -fPIC

clean:
	rm -f $(CLEAN)

.PHONY: build
