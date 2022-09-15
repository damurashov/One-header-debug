#define OHDEBUG_ENABLE_ALL_BY_DEFAULT 0  // Only print those groups which we explicitly allow. Remove it to restore to the original configuration (allow all by default)
#include "OhDebug.hpp"
#include <iostream>

ohdebuggroup(1)  // Explicitly allow printing group 1 (or disallow, if OHDEBUG_ENABLE_ALL_BY_DEFAULT=1)
ohdebuggroup(arbitrary)
ohdebuggroup(string test)

void voidfn() {
	std::cout << "echo" << std::endl;
}

int main(void)
{
	int a = 0;
	int b = 1;
	ohdebug(0, 777, a, b);  // ...
	ohdebug(1, 42, a, b);  // 42=42  a=0  b=1
	ohdebug(arbitrary, 42, b, a, a, a, a, a, a, "plain string", a);
	ohdebugstr(string test, "just a string");
	ohdebugstr(string test, voidfn());
	ohdebugsect(sect, { std::cout << "This will only be printed if debug enabled" << std::endl; });

	for (int i = 0; i < 21; ++i) {
		ohdebugeveryn(arbitrary, 5, "every 5", i);
		ohdebugsecteveryn(arbitrary, 10, {ohdebug(arbitrary, i);});
		ohdebugsecteveryn(arbitrary, -1, {ohdebug(arbitrary, i);});  // One can temporarily disable this without commenting the entire chunk
		ohdebugsectonce(arbitrary, 13, ohdebug(arbitrary, "once", i)); // Will only get triggered on 13-th (14-th) attempt
		ohdebugonce(arbitrary, 12, "just once, when i = 12", i);
		ohdebugsectif(arbitrary, i % 2 == 0, {
			ohdebug(arbitrary, "conditional", i);
		});
		ohdebugif(arbitrary, i % 3 == 0, "when i is a multiple of 3", i);
		ohdebugassert(arbitrary, i < 20, i);
	}
}
