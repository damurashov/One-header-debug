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
  - API description
  - Use cases: what it is for
  - The core mechanism
  - Limitations
- Glob expressions for topic filtering
  - (OR) constexpr group checker: split and check a group word-by-word
  - https://codereview.stackexchange.com/questions/108686/compile-time-wildcard-pattern-matching
- API
  - catch API: accumulate variables and produce an output only if a condition is not satisfied.
    - Analagous assert API
- output
  - (?) tabulated output (indents)

# How to use it

Just drop it into your project. 

![](./res/pussy.png)

Once you've done with it, disable the macro, throw it away, or keep it for your grandchildren.
