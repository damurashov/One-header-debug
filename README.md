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
- naming: ohdebugsectionif, ohdebugif, ohdebugsectiononce, ohdebugsectionevery

# How to use it

Just drop it into your project. 

![](./res/pussy.png)

Once you've done with it, disable the macro, throw it away, or keep it for your grandchildren.
