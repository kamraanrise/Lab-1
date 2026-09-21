# Lab 1 Reflection

### What did you like or dislike about Python?
Working through this lab highlighted how concise and expressive Python's syntax is compared to C or C++. Writing functions like `factorial` and `fibonacci` took only a few lines without needing boilerplate like `#include` headers, strict type definitions, or a rigid `main()` function structure. Multiple assignment (`prev, curr = curr, prev + curr`) also made sequential state tracking very readable without needing an explicit swap variable.

On the other hand, the mandatory indentation rules take adjustment coming from C/C++. In brace-based languages, spacing is mostly stylistic, but in Python an extra or missing space immediately shifts execution blocks or triggers an `IndentationError`. 

### Was there anything that behaved differently than you expected in Python?
One significant difference is how Python handles arbitrarily large integers. In C/C++, calculating factorials causes integer overflows very quickly once $n > 12$ on standard 32-bit types, requiring specialized libraries or custom big-integer logic. Python automatically scales integer capacity, letting factorials run without manual overflow management.

Another structural difference was class design. Explicitly defining `self` as the first parameter of every instance method felt redundant at first compared to C++, where the `this` pointer is implicit.

### Similarities and Differences: Python vs. C/C++
* **Typing System:** C/C++ uses static typing checked at compile time, catching errors before execution. Python is dynamically typed and evaluated at runtime, which speeds up development but requires disciplined testing to prevent type-related runtime exceptions.
* **Memory Management:** C/C++ requires manual memory management or smart pointers for resource tracking. Python handles memory automatically through reference counting and a built-in garbage collector.
* **Object-Oriented Design:** Python classes use explicit `self` references and inheritance syntax like `class DownCounter(UpCounter):`, whereas C++ uses access specifiers (`public`, `protected`, `private`) and initializer lists.
* **Impact on Programming Approach:** In C++, significant design time goes toward memory allocation and type correctness upfront. In Python, focus shifts straight to algorithm logic and data manipulation.