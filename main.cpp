#define OHDEBUG_ENABLE_ALL_BY_DEFAULT 0  // Only print those groups which we explicitly allow. Remove it to restore to the original configuration (allow all by default)
#include "OhDebug.hpp"

ohdebuggroup(1)  // Explicitly allow printing group 1 (or disallow, if OHDEBUG_ENABLE_ALL_BY_DEFAULT=1)

int main(void)
{
	int a = 0;
	int b = 1;
	ohdebug(0, 777, a, b);  // ...
	ohdebug(1, 42, a, b);  // 42=42  a=0  b=1
}
