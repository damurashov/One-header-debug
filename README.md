# One Header Debug

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

And above all, it has no fool protection, meaning that it does not treat you as a fool.

# How to use it

1. Copy it
2. Include it

# Limitations

- C++11 is required;
- It is not yet tested on MSVC;
