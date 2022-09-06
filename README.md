The ...

```c++
#if 1 
# include <iostream>
# define debug(a) std::cout << (a) << std::endl
#else
# define debug(...) 
#endif
```

... is no more. Just drop it into your project. Once you've done with it, disable the macro, throw it away, or keep it for your grandchildren.
