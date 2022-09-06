#if !defined(ONE_HEADER_DEBUG_HPP_)
#define ONE_HEADER_DEBUG_HPP_

#if 1 || OH_DEBUG

#if !defined(OHDEBUG_ENABLE_ALL_BY_DEFAULT)
# define OHDEBUG_ENABLE_ALL_BY_DEFAULT 1
#endif  // OHDEBUG_ENABLE_ALL_BY_DEFAULT

# include <iostream>
#include <tuple>
#include <type_traits>

namespace OhDebug {

#if OHDEBUG_ENABLE_ALL_BY_DEFAULT

template <int G>
struct Enabled : std::true_type {
};

# define ohdebuggroup(g) \
	namespace OhDebug { \
	template <> \
	struct Enabled<g> : std::false_type { \
	}; \
	}  // namespace OhDebug
#else

template <int G>
struct Enabled : std::false_type {
};

# define ohdebuggroup(g) \
	namespace OhDebug { \
	template <> \
	struct Enabled<g> : std::true_type { \
	}; \
	}  // namespace OhDebug

#endif  // OHDEBUG_ENABLE_ALL_BY_DEFAULT

template <int G, class ...Ts>
void debug(Ts &&...aArgs)
{
	if (!OhDebug::Enabled<G>::value) {
		return;
	}

	using List = int[];
	List{(void(std::cout << (aArgs) << ", "), 0)...};
}

}  // namespace OhDebug

# define ohdebug(context, ...) OhDebug::debug<context>(#__VA_ARGS__, ##__VA_ARGS__)
# define ohdebugstr(a) std::cout << (a) << std::endl;
#else
# define ohdebug(...)
# define ohdebugstr(...)
# define ohdebuggroup(...)
#endif

#if defined(OHDEBUG_ENABLE_ALL_BY_DEFAULT)
# undef OHDEBUG_ENABLE_ALL_BY_DEFAULT
#endif

#endif

