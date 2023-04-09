# One Header Debug

Meet one of the world's smallest tracing+testing.

The ...

```c++
#if 1
# include <iostream>
# define debug(a) std::cout << (a) << std::endl
#else
# define debug(...)
#endif
``` ,

and

```c++
void testFunction1 {
  assert(true == 1);
}

using TestFunctionCallable = void(*)();

static TestFunctionCallable sTests[] = {
  testFunction1,
};

int main()
{
  for (auto test : tests) {
    test();
  }
}
```
... are no more.

# Why use it

- It is only 239 lines of well documented source code;
- It's simple: you can hack it all you want;
- It's easy to use: just drop it with your files, no need to modify your build scripts;

# How to use it

1. Copy it
2. Include it
3. Define `OHDEBUG_PORT_ENABLE` and `OHDEBUG_TAGS_ENABLE` in your tracing / testing source

# When to use it

- You want to trace your program, while modifying as little code as possible when there is a need to shut down particularly verbose chunks in a fast way (compile-time tags);
- You only want to test a small piece of your project;

# Limitations

- C++11 is required;
- It is not yet tested on MSVC;
