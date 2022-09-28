# One Header Debug

The ...

```c++
#if 1 
# include <iostream>
# define debug(a) std::cout << (a) << std::endl
#else
# define debug(...) 
#endif
```

... is no more.

# TODO

- Project, README
  - Features
    - Filtering
  - API description
  - Use cases: what it is for
  - The core mechanism
  - Limitations
  - Synchronized output
- Glob expressions for topic filtering
  - (OR) constexpr group checker: split and check a group word-by-word
  - https://codereview.stackexchange.com/questions/108686/compile-time-wildcard-pattern-matching
- API
  - catch API: accumulate variables and produce an output only if a condition is not satisfied.
    - Analagous assert API
  - enabling: `ohdebug1`, `ohdebug0` instead of `ohdebuggroup`
    - explicit enable/disable
    - enable/disable override chains using compile-time counters (if compatible w/ msvs and gcc)
- output
  - (?) tabulated output (indents)
  - shorten filename (absolute paths may be quite lengthy)

# How to use it

Just drop it into your project. 

![](./res/pussy.png)

Once you've done with it, disable the macro, throw it away, or keep it for your grandchildren.
