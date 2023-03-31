#define OHDEBUG_PORT_ENABLE

#include "OhDebug.hpp"

OHDEBUG_TAG_ENABLE("Echo")

int main(void)
{
	OHDEBUG("Echo", 1);
}
