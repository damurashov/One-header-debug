#define OHDEBUG_PORT_ENABLE
#define OHDEBUG_TAGS_ENABLE "Echo2", "Echo3"

#include "OhDebug.hpp"

OHDEBUG_TAG_ENABLE("Echo")
// OHDEBUG_TAG_ENABLE("Echo2")

int main(void)
{
	OHDEBUG("Echo", 1, "some string", 42U);
	OHDEBUG("Echo2", 1, "some string", 42U);
	OHDEBUG("Echo3", 1, "some string", 42U);
}
