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

- Glob expressions for topic filtering
  - https://codereview.stackexchange.com/questions/108686/compile-time-wildcard-pattern-matching
- void arguments
- catch API: accumulate variables and produce an output only if a condition is not satisfied.
  - Analagous assert API
- constexpr group checker: split and check a group word-by-word
- output
  - tabulated output (indents)

# How to use it

Just drop it into your project. 

![](./res/pussy.png)

Once you've done with it, disable the macro, throw it away, or keep it for your grandchildren.
