# Programming concepts to get you going
> All languages have a `syntax`. The `syntax` is a set of rules that
> define the structure and domain of a language. The domain consists
> of `words` and their validity in a given context and the default
> interpretation within that language.

Understanding the syntax, control flow, built-in types and functions,
and structure of a simple Python program is essential to move forward.

Here is a quick overview:
- **variables:** are `named containers` for storing values of a given
`data type` in a memory location. Typically the value of a variable is
mutable (i,e. can be changed). And the mutation occurs by `assignment`.
In Python assignment is done using the `=` symbol.
- **functions:** are `store and reuse` variables. The type here is a
block of code that can be referenced and invoked - using the name of
the function or a reference to that function.
- **built-in types:** are primitive data shapes (in memory) that 
have common characteristics, such as the set of valid values and
set of valid operations allowed on those values. Python provides
a range of [built-in types](https://docs.python.org/3/library/stdtypes.html):
  - numerics
  - sequences
  - mappings
  - classes
  - instances
  - exceptions
- **flow-control:** are control structures that alter the flow of
execution. There are three fundamental structures:
  - Sequential: a sequence of statements executed one after the other.
  In the code below, the statements (two assignments and two function
  calls) are executed one after the other.
    ```python
      first = 'here'
      second = 'where'
      do_something(first)
      do_something(second)
    ```
  - Conditional: statements are those that alter the flow based on the
  truth value of an `expression` evaluating to either `true` or `false`.
  In the code below, cruise control is disabled if the speed of the car
  is below 20mph.
    ```python
    ...
      ...
    speed = get_current_speed()
    if (speed < 20):
      disable_cruise_control()
    
      ...
    ...
    ```
    Conditional statements can execute code `1-of-1-way` (see above), `1-of-2-way` (`if: ... else:`), or 
    `1-of-n-way` (`if: [elif:]+... else:`); The first
    conditional whose expression yields a `true` value is
    executed and the rest of the paths (of 2-way and n-way) are ignored!
  - Loops: allow a `block of code` to be executed repeatedly. In Python, we have `indefinite` and `deterministic` loops.
    ```python
      # an indefinite loop requires a
      # conditional to exit the loop
      temparature = get_temperature()
      alerts = []
      while True:
        ... 
          ...
        if temperature > 98:
          alerts.append('get some rest')
          break
        ...
          ...
      
      # A deterministic loop has a termination
      # condition built-in; here the loop exits
      # when all items in `alerts` have been
      # enumerated.
      for alert in alerts:
        send_alert(alert)
    ```

# Meta concepts
Programming involves more than understanding the syntax and structure
of a language. The good news is if you know the meaning of an English
word, in majority of the cases the application of that word in Python
is contextually the same. A few words require disambiguation and 
that's what we covered this week.

## What is a file?
A file in the context of programming is a container for digital data, 
i.e bits and bytes. The meaning of the contents of the file and what operations are applicable is imparted by the program that can read 
(and write) that file. The location of the file (often referred to
as its `path`) is important to know to be able to process a file.

## What is a module?
A module is a file that contains code (variables, functions, classes...). In the context of Python, our interest in a module is in its capabilites once it is made available in memory. One or more `module`s are referred to as a `package`. We organize code as modules and packages for reuse and maintainability. 

> How Python deems code to belong to a package has changed in 3.x; 
> you can read more about it in [PEP 420](https://peps.python.org/pep-0420/).

## Class vs Object?
A `class` is a `type`. The type is a template to produce instances that
have a shape (in memory) with zero or more attributes, and behaviour.
Akin to a blueprint of a house - it is plan that tells us how to
construct the house and how it looks when built. A `class` is a 
foundational concept to **OOP - Object Oriented Programming**.

An object is the result of the reification of a class. A house built 
from a blueprint is an instance of that plan. Likewise an object in
programming is the coming into existence (in memory) of a `plan` 
described by its `class`.

In Python everything is an `object`.

```python
  i_am_an_object = 5
  help(i_am_an_object)
```

Therefore all objects inherit special methods imparted to the object
from a **God** class; of interest are those methods prefixed and 
suffixed using two underscores. These are called `dunder` methods, short
for `double underscore`. These are required and are key to the elegant
syntax of Python.  A lot of decisions to facilitate writing `clean code`
is already made for us by the designers of the language.

For instance in the code below, the short and sweet **for** loop syntax
is possible because Python knows to invoke `__iter__` dunder method 
on `fruits` and invoke `__next__` dunder method on the object returned
by `__iter__` method.

```python
  fruits = ['apple', 'blueberry', 'cranberry']
  for fruit in fruits:
    print(fruit)
```

Related to class and object are its `attributes`. An `attribute` is
a bound field of a class or object that represents a trait. A trait
can be a property or a function (or method). Remember in Python
everything is an object (including a `module`; gasp!). You can obtain
a list of these attributes by using the `dir` function.

## Inheritance vs Composition
Inheritance is another fundamental concept of **OOP**. It is a 
mechanism by which a child class can derive the traits of its parent
class. For example, a cat is an animal, and so is a dog. It makes sense
to derive both cat and dog classes from an animal class. And it would 
be correct in a domain dealing with cats and dogs. The benefit of doing
so is that we could implement a `walk` method once in the  animal class and `inherit` that method in our cat and dog classes.

Inheritance is powerful feature of a language when used correctly. The 
proper use for inheritance is to express a `kind-of` relationship in
a domain of interest. In practice finding good `kind-of` relationships
is hard in many domains and doubly hard with multiple inheritance. 

> In our discussion today, I mentioned Python only supports single
> inheritance. That is incorrect; I had too much JavaScript in my head
> and had not fully context switched to Python. **Python** has full 
> support for multiple inheritance**.

A test for good inheritance modeling is the [`liskov substitution`](https://en.wikipedia.org/wiki/Liskov_substitution_principle) principle which states that objects of a superclass (i.e the parent) should be replaceable with objects of its subclasses without breaking
a function that accepts the parent type. 

In other words if a thing looks like a duck and quacks like a duck, 
[then it better be a duck](https://irian.to/blogs/liskov-substitution-principle/). 

The trouble is no language can prevent bad abstractions; programmers end up creating bad abstractions because they are seduced by the code reuse afforded by inheritance, which is an artefact and not the primary 
purpose to use inheritance.

A better mechanism for code reuse is to use `composition` which expresses
a `has-a` relationship. Obligatory classic example is: a car `has-a`
steering weheel. Note, for code reuse, the language does not prevent you from inheriting a steering wheel from a parent class; this however would
be a poor abstraction as it will break when in the not so distant future self-driving cars *may* come without a steering wheel. 

> Maintaining code that uses composition is much easier than code that
> uses inheritance, especially inheritance used for code reuse rather
> than type substitutability.

## Function vs Method
A `function` is chunk of `store-and-reuse` code to accomplish a `task`.
It typically has a name, accepts zero or more inputs and produces zero 
or more outputs. We invoke a function by its name or through reference
to it

> function: [inputs]*  -> process -> [output]*

A `method` is a chunk of code typically associated with an `object`. 
This association is made explicit when defining a method in Python by
declaring the first parameter as `self`. In some other languages
this association is implied and always available as `this`. When 
invoking a `method` the `self` or `this` is implicitly passed in as 
the first positional argument to the method call.

> The semantics of function call vs method call in Python have
> nuances; for example bound vs unbound methods. For a deeper
> understanding, you can [read PEP 579](https://peps.python.org/pep-0579/).
 
## What is an API
API (Application Programming Interface) is a glorified (documented and 
public) function that performs some useful work (operation, or task). A
function such as `sqrt` in the `math` package is an example of an 
`in-process` API. That is, it performs its work within the process space
of the caller.

APIs can also be `out-of-process` and these are typically request/response
in nature; that is, a request is made to which a response is expected. 
These `out-of-process` APIs allow work to be performed on remote and independent sources. The communication between these sources is 
structured over a protocol. Most popular `out-of-process` API 
implementation architecture is REST ([REpresentational State Transfer](https://en.wikipedia.org/wiki/Representational_state_transfer)).

## Clean code
Clean code is a set of practices and pearls of wisdom espoused by 
Robert C. Martin - lovingly called `Uncle Bob`. There are some pearls
that do shine, as evidenced by the count of highlights by the readers
of the [book](https://www.amazon.com/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882).

1. >Functions should either do something or answer something, but not
   both.
2. >The proper use of comments is to compensate for our failure to 
   express ourself in code.
3. >Functions should do one thing. They should do it well.

In a nut shell, clean code is about ensuring quality by paying attention
to documentation, naming conventions, consistency and decomposition of
large work into smaller and easier parts of code blocks so that:
- each individual part is easily understood
- and placed in context of the whole system
- and can be worked on in parallel by multiple team members
- and is easy to read, maintain, and/or enhance

All of the above is easier said than done!

# Assignment for week 2
- Your assignment is to compute and return the average closing price for
  a given stock symbol. You are provided the driver code and a shell 
  of a function named `avg` in [`finpack.py`](code/finpack.py)
  that fetches stock data for you; all you have to do is to compute
  the average.
- Read the notes and come prepared to answer the following questions:
  1. What are the signs of a `good` API?
  2. If you want to plot the `moving_avg`, what changes would you make
     to allow the `avg` function be used by `moving_avg` function?
  3. Is it better to create a new `moving_avg` function or `parameterize`
     the `avg` function to return a moving average?




