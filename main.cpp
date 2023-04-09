// Please note that those defines must go before `#include <OhDebug>`
#define OHDEBUG_PORT_ENABLE
#define OHDEBUG_TAGS_ENABLE "Echo2", "Echo3"

#include <OhDebug.hpp>
#include <cassert>
#include <cstring>

OHDEBUG_TEST("Some test")
{
	OHDEBUG("Echo1", "This will not be printed");
	OHDEBUG("Echo2", "This is echo");
	assert(strcmp("Someone who uses OHDEBUG", "Someone who needs a wrapper over standard C assert") != 0);
	assert(strcmp("Do not forget to compile it with -g flag",
		"So it will show the exact place of where an assert has been triggered") != 0);
	// assert(strcmp("Keep it simple", "Continue tests after an assert is triggered") == 0);
}

OHDEBUG_TEST("Some other test")
{
	OHDEBUG("Echo2", "This is echo");
}

int main(void)
{
	OHDEBUG("Echo", 1, "some string", 42U);
	OHDEBUG("Echo2", 1, "some string", 42U);
	OHDEBUG("Echo3", 1, "some string", 42U);
	OHDEBUG_RUN_TESTS();
}
