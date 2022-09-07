CC = gcc
CLEAN = *.o ohdebug

build:
	$(CC) -c -Wall main.cpp
	$(CC) -o ohdebug main.cpp -lstdc++ -fPIC

clean:
	rm -f $(CLEAN)
