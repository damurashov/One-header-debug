#define OHDEBUG_ENABLE_ALL_BY_DEFAULT 0  // Only print those groups which we explicitly allow. Remove it to restore to the original configuration (allow all by default)
#include "OhDebug.hpp"

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
	ohdebug(arbitrary, 42, b, ohdebugfvoid(voidfn()), a, a, a, a, a, a, "plain string", a);
	ohdebugstr(string test, "just a string");
	ohdebugstr(string test, voidfn());

	for (int i = 0; i < 20; ++i) {
		ohdebugeveryn(10, {ohdebug(arbitrary, i);});
		ohdebugeveryn(-1, {ohdebug(arbitrary, i);});  // One can temporarily disable this without commenting the entire chunk
	}
}
