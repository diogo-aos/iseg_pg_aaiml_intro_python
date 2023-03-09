## Lesson 3
<!-- .slide: id="lesson2_recap" data-background="wheat"-->

- functions
- map, filter
- modules, packages
- files


---

## Functions

How to reuse the same logic for different things?


--

We can think of a function as a black box that receives inputs and gives outputs.

What functions have we seen before?

`enumerate()`, `zip()`, `range()`, `int()`, `float()`, `str()`
<!-- .element: class="fragment" -->

--

- we define a function with the `def` keyword
- followed by the name of the function `sum_2` and ()
- inside the () we write the names of the inputs the function should receive.

```python
def sum_2(a):
    b = a + 2
    return b
```

- the function exits when it reaches the end of the instructions
- or when the instruction ``return`` is used

<!-- .element: class="fragment" -->

--

```python
def sum_2(a):
    b = a + 2
    return a, b
```

`return` can receive multiple values - which means the function will output multiple values

Remember tuples? When we return multiple values like this `a, b`, we're actually returning a tuple.

<!-- .element: class="fragment" -->

--

Let's use our function.

```python
x = 3

def sum_2(a):
    b = a + 2
    return b

print(sum_2(x))  # -> 5
```

We call a function but writing its name, followed by ().
Inside the () we give the arguments (inputs).

We call ``sum_2`` with input ``x``. The value of ``x`` is copied to the argument a of ``sum_2``.

<!-- .element: class="fragment" -->

---

## Functions
### variable scope

**local** and **global** variables

--

```python
x = 3

def sum_2(a):
    b = a + 2
    print(x) # -> 3
    return b

print(sum_2(x))  # -> 5
print(x) # -> 3
print(a)  # -> NameError: name 'a' is not defined
```

``a`` and ``b`` exist only inside function ``sum_2``.

But ``x`` exists inside the function.

``x`` is unchanged by calling ``sum_2``

--

- a and b are said to be local variables, within the scope of the function
- x is a global variable, because it exists outside any scope within our program

```python [1,5,6,9,10]
x = 3

def sum_2(a):
    b = a + 2
    x = 4
    print(x) # -> ?
    return b

print(sum_2(x))  # -> 5
print(x) # -> ?
```

<!-- .element: class="fragment" data-fragment-index="2" -->

Now what?

<!-- .element: class="fragment" data-fragment-index="2" -->

--

```python [1,6,10]
x = 3

def sum_2(a):
    b = a + 2
    x = 4
    print(x) # -> 4
    return b

print(sum_2(x))  # -> 5
print(x) # -> 3
```

- ``x=4`` inside the function creates a new variable `x` within the scope of the function that has the same name as the global variable ``x``
- every use of `x` inside the function expects a variable named `x` within the scope of that function 

--

If we wanted to change (and not only read) the global variable, we need to declare it.

```python [1,4,7,11]
x = 3

def sum_2(a):
    global x
    b = a + 2
    x = 4
    print(x) # -> 4
    return b

print(sum_2(x))  # -> 5
print(x) # -> 4
```

All global variables are stored inside a dictionary that can be accessed by calling ``globals()``.

<!-- .element: class="fragment" -->

---

## Functions
### first class citizens

--

In Python, functions are just like any other object that can be passed around.

```text
In [65]: sum_2
Out[65]: <function __main__.sum_2(a)>
```

We can even attribute a function to a variable and then call the same function with the name of the new variable.

<!-- .element: class="fragment" data-fragment-index="2"-->

```python
def sum_2(a):
    b = a + 2
    return b

f = sum_2
f(2) # -> 4
```

<!-- .element: class="fragment" data-fragment-index="2"-->

--

We may also pass a function as an argument to another function.

```python
def apply_function(func, arg):
    y = func(arg)
    return y

apply_function(sum_2, 2) # -> 4
```

--

#### lambda

There is a shortcut for defining short and simple functions:

 
```python
f = lambda a: a + 2
f(2) # -> 4

g = lambda a,b: a+b**2
g(2,3) # -> 11
```

- We write lambda followed by the arguments we want to receive.
- After the `:`, we write the expression that will be returned (no need to write return).

<!-- .element: class="fragment" data-fragment-index="2"-->

--

Why is this useful? Because we can pass custom operations to other functions and apply them elsewhere.

We can also import other functions and apply them in our codebase.

Let's look at 2 particularly useful example of using functions in this way.

<!-- .element: class="fragment" data-fragment-index="2"-->

---

## map

Let's suppose we have a list of prices:

```python
prices = [1.92, 46.4, 30.56, 11.63, 8.35,
          6.32, 28.21, 8.21, 12.86, 6.95]
```

These prices will suffer an update of 4.5%. How can we update them?

--

With what we've learned so far, we could write a loop.

```python
new_prices = []
percent = 4.5
for p in prices:
    new_prices.append(p * (1 + percent/100))
```

--

We can also use `map`, which apply a function to all elements of a list.

```python
percent = 4.5
def update(price):
    return price * (1 + percent/100)

new_prices = list(map(update, prices))
```

--

Or using lambda...

```python
percent = 4.5
new_prices = list(map(lambda p: p * (1 + percent / 100), prices))
```

⚠️⚠️ Keep your lambdas short. ⚠️⚠️
<!-- .element: class="fragment" data-fragment-index="2"-->


If you have complex logic, transfer it to a "normal" function where the logic will be clearer.
<!-- .element: class="fragment" data-fragment-index="2"-->

--

Why are we converting the result of map to a list?

map actually returns an iterable, not a list.

```text
In [11]: map(lambda p: p * (1 + percent / 100), prices)
Out[11]: <map at 0x15a9b31cb80>
```

And it can also receive any iterable (tuple, dict, ...), not just a list.

--

```python
authors = dict(zip(names, ages))
output = list(map(lambda n, a: f"Author {n} died at age {a}.",
                  authors.items()))
# equivalent to 
output = [f"Author {n} died at age {a}." for n,a in authors.items()]
```

--

Are you really going to use this?

Often people don't directly use Python's default map, but map is often implemented in other data structures, such as...

<!-- .element: class="fragment" data-fragment-index="2"-->

```python
df = pandas.read_excel("prices.xlsx")
```

<!-- .element: class="fragment" data-fragment-index="2"-->

```text
In [45]: df.head()
Out[45]: 
   prices    category
0   22.25  vegetables
1   10.22  vegetables
2    2.19  vegetables
3   14.63        pets
4   31.21       fruit
```

<!-- .element: class="fragment" data-fragment-index="3"-->


```text
In [46]: df.shape
Out[46]: (50, 2)
```

<!-- .element: class="fragment" data-fragment-index="3"-->


--

```python
df["new_prices"] = df["prices"].map(lambda p: p * 1.045)
```

```text
In [51]: df.head()
Out[51]: 
   prices    category  new_prices
0   22.25  vegetables    23.25125
1   10.22  vegetables    10.67990
2    2.19  vegetables     2.28855
3   14.63        pets    15.28835
4   31.21       fruit    32.61445
```

<!-- .element: class="fragment" data-fragment-index="2"-->


```text
In [52]: df.shape
Out[52]: (50, 3)
```

<!-- .element: class="fragment" data-fragment-index="2"-->



---

## filter

``filter`` works just like ``map``

but instead of applying a function to every value, we're picking which values we want to keep.
<!-- .element: class="fragment" data-fragment-index="2"-->


--

Because we're choosing which values to keep, the function that we give to ``filter`` must return a boolean.


```python
prices = [9.56, 23.82, 17.39, 5.11, 8.28]
categories = ['fruit', 'hygiene', 'fruit', 'vegetables', 'vegetables']

vegetables_prices = [p for p,c in zip(prices, categories) \
                     if c == 'vegetables']
```

```python
vegetables_prices = list(filter(lambda p,c: c == 'vegetables',
                                zip(prices, categories)))
```

<!-- .element: class="fragment" data-fragment-index="2"-->

--

Wil you use this?

Probably not! In Pandas, we actually filter in different ways, like:

<!-- .element: class="fragment" data-fragment-index="2"-->

```python
df = pandas.read_excel("prices.xlsx")
vegetables = df[df["category"] == "vegetable"]
```

<!-- .element: class="fragment" data-fragment-index="2"-->

```text
In [61]: vegetables.head()
Out[61]: 
    prices    category  new_prices
0    22.25  vegetables    23.25125
1    10.22  vegetables    10.67990
2     2.19  vegetables     2.28855
13    1.59  vegetables     1.66155
22   14.17  vegetables    14.80765
```

<!-- .element: class="fragment" data-fragment-index="3"-->

```text
In [62]: vegetables.shape
Out[62]: (13, 3)
```

<!-- .element: class="fragment" data-fragment-index="3"-->

```text
In [46]: df.shape
Out[46]: (50, 2)
```
<!-- .element: class="fragment" data-fragment-index="3"-->

--

Why does that work?

When we compare the column "category" with the value "vegetables", we get another column of the same size indicating where that comparisson was True or False.

```text
In [64]: df["category"] == "vegetables"
Out[64]: 
0      True
1      True
2      True
3     False
4     False
5     False
```

<!-- .element: class="fragment" data-fragment-index="1"-->

This column is the **mask** that will select the rows of the original dataframe where the comparisson is True.

<!-- .element: class="fragment" data-fragment-index="2"-->


---

## External code
### Python modules

In Python, we can create our own modules to store code and import that code to other programs.

Why do this? Reusability and modularity.
<!-- .element: class="fragment" data-fragment-index="2"-    ->

Let's create our own Python module.
<!-- .element: class="fragment" data-fragment-index="3"-->

You can download the notebook [here](code/lesson3/modules.ipynb)
<!-- .element: class="fragment" data-fragment-index="3"-->

---

## Files
### text

- open, read, write, close
- modes r, w, a
- context manager
- pathlib, swiss army knife for files

--

### open

```python
f = open("test_file.txt")  # open a file
```

This gives an error, because this file does not exist.

```text
In [66]: f = open("test_file.txt")  # open a file
---------------------------------------------------------------------------
FileNotFoundError                         Traceback (most recent call last)
<ipython-input-66-a7d550966829> in <module>
----> 1 f = open("test_file.txt")  # open a file

FileNotFoundError: [Errno 2] No such file or directory: 'test_file.txt'
```

--

There are 3 ways of opening a file:
- "r" for reading only, the file must exist exist
- "a" for writing, creates the file if it doesn't exist or overwrites, starts writing at the end
- "w" for writing, creates the file if it doesn't exist or overwrites, starts writing at the end

If a mode is not speficied when opening a file, the default is "r". That is why we got an error.

<!-- .element: class="fragment" data-fragment-index="1"-->

--

Let's create our file first.

```python
f = open("test_file.txt", "w")  # open a file in write mode
f.write("line 1\n") # \n write a newline sequence to the file
f.write("line 2\n")
f.close()  # we must close the file for the changes to take effect
```

--

Let's create our file first.

```python
f = open("test_file.txt", "r")  # open a file in write mode
data = f.read()
print(data)
f.close()
```

```text
line 1
line 2

```

--

We can add a "+" modifier to any mode, and it allows the modes to both read and write.

"r+" still doesn't create a file if it doesn't exist though.

--

It's easier to forget closing files, specially when there are many operations between opening and closing.

The recommended way of opening and closing files is to use a context manager.

<!-- .element: class="fragment" data-fragment-index="1"-->

```python
with open("test_file.txt", "r") as f:
    data = f.read()
print(data)
```
<!-- .element: class="fragment" data-fragment-index="1"-->

When we use with, the file is automatically closed when the block of instructions inside with is finished.

<!-- .element: class="fragment" data-fragment-index="2"-->

---

## Files
### binary

Binary files store data in a format that is not human readably.

They're very useful to store numeric data because we can fit more numbers within the same memory.

<!-- .element: class="fragment" data-fragment-index="1"-->

--

To use files in binary mode, we simply add a "b" to the modes we've already seen so far.

```python
with open("test.pkl", "rb") as f:
    # do something...
```

--

They will be particularly useful to store trained data science models to be used in a future date or by other people.

In Python, we can store almost any object in a binary format with the ``pickle`` module.

<!-- .element: class="fragment" data-fragment-index="1"-->

--


```python
test_dict = {x: y for x,y in zip(range(0,5), range(100,5))}
```

```python
{0: 100,
 1: 101,
 2: 102,
 3: 103,
 4: 104}
```

--

#### store an object with pickle

```python
import pickle
with open("test.pkl", "wb") as f:
    pickle.dump(test_dict, f)
```

#### load an object from a pickle file

<!-- .element: class="fragment" data-fragment-index="1"-->

```python
with open("test.pkl", "rb") as f:
    loaded_dict = pickle.load(f)
print(loaded_dict)
```

<!-- .element: class="fragment" data-fragment-index="1"-->

```python
{0: 100,
 1: 101,
 2: 102,
 3: 103,
 4: 104}
```

<!-- .element: class="fragment" data-fragment-index="1"-->

--

---

## files
### pathlib

I recommend the use of the `pathlib` library anytime you need to deal with files.


--

### pathlib

It makes working with files much easier, since there are things that change when our code executes in Windows, MacOS, Linux, etc.
<!-- .element: class="fragment" data-fragment-index="1"-->


By using ``pathlib``, many of these changes are abstracted away.

<!-- .element: class="fragment" data-fragment-index="2"-->

We also have many utilities that make life easier.
<!-- .element: class="fragment" data-fragment-index="3"-->


--

#### create a Path

`Path` is the main object to use, and it provides the method that make life easier.

```python
from pathlib import Path
test_path = Path("test_file.txt")
test_path.exists() # returns True if the file exists
```

--

#### open, write, read

```python
test_path = Path("test_file.txt")
with test_path.open("a") as f:
    f.write("line 3\n")

with test_path.open("a") as f:
    data = f.readlines()
print(data)
```

```text
['line 1\n', 'line 2\n', 'line 3\n']
```

.readlines() is a new method, that reads the whole file and splits the content by lines in a list.

<!-- .element: class="fragment" data-fragment-index="1"-->

--

```python
print(test_path.read_text())

# we can't pass a mode to .write_text
test_path.write_text("overwrites everything")

print(test_path.read_text())
```

```text
line 1
line 2
line 3
```

```text
overwrites everything
```

--

They also work with paths that are directories and it becomes easier to list all files inside.

```python
p=Path("code")
p.is_dir()
```

```python
True
```

--

List all files and folders inside `code/`

```python
list(p.iterdir())
```

```python
[WindowsPath('code/.ipynb_checkpoints'),
 WindowsPath('code/conditionals1.py'),
 WindowsPath('code/conditionals2.py'),
 WindowsPath('code/io_terminal.py'),
 WindowsPath('code/lesson3'),
 WindowsPath('code/types.py'),
 WindowsPath('code/variables.py')]
```

--

List all ``.py`` files inside  `code/`


```python
list(p.glob("*.py"))
```

```python
[WindowsPath('code/conditionals1.py'),
 WindowsPath('code/conditionals2.py'),
 WindowsPath('code/io_terminal.py'),
 WindowsPath('code/types.py'),
 WindowsPath('code/variables.py')]
```


--

`Path` objects have many more useful methods, but we won't explore them in this course:
- creating and deleting files/folders
- retrieving parent folders
- retrieving absolute and relative paths
- ...

