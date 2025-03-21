## Lesson 4
<!-- .slide: id="lesson4" data-background="wheat"-->

- catching errors
- classes
- debugging
- demo & exercise


---

## Learning outcomes - you'll be able to

- read tracebacks to find and fix errors
- catch exceptions to prevent program crashes
- understand the basic concepts of Object Oriented Programming
- create basic classes
- use classes from other packages
- use the debugger to find and fix errors

---

## Exceptions

- Unexpected behaviour can manifest itself as an exception.
- If not dealt with, exceptions break our programs.

--

```python
int("hello world")
```

```text
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'hello'
```

- Converting a nonnumeric string to an integer is unexpected behaviour, and a <span style="color:salmon">`ValueError`</span> exception is thrown.

--

```python
read_my_file("imaginary_file.txt")
```

```text
FileNotFoundError: [Errno 2] No such file or directory: 'imaginary_file.txt'
```

- The file <span style="color:gold">`imaginary_file.txt`</span> does not exist, so a <span style="color:salmon">`FileNotFoundError`</span> exception is thrown.

--

* Python has many different exceptions.
* Their name is usually sugestive of the problem we're facing.
* Many packages define their own exceptions. <!-- .element: class="fragment"-->
* Sometimes those are not as suggestive. <!-- .element: class="fragment"-->

--

When we get an exception, we get:

1. the type of the exception, e.g. <span style="color:salmon">`FileNotFoundError`</span>
2. usually, a suggestive string, e.g. <small> <span style="color:white"> ```No such file or directory: 'imaginary_file.txt'``` </span> </small>
3. a traceback

--

#### traceback

- The traceback is the trace of instructions from our program's origin to the point where the exception happened.
- If an exception was thrown inside a function:
  - the traceback includes the line where the function was called
  - and then the line inside the function where the exception was thrown.
  - recursively


--

There may be a long list of function calls.

```text
Traceback (most recent call last):
  File "script.py", line 8, in <module>
    avs = averages(data_fn)
  File "mypackage/stats.py", line 17, in averages
    data = read_csv(filename)
  File "mypackage/file_utils.py", line 7, in read_csv
    with open(fn) as f:
FileNotFoundError: [Errno 2] No such file or directory: 'imaginary_file.txt'
```

--

#### traceback

It's a traceback because it allows us to  <span style="color:gold">trace</span> the problem <span style="color:cyan">back</span> to its root.

---

## Catching exceptions

- When an exception happens, we can have a backup plan.
- In Python, we can use a `try` block to catch an exception and stop the program from failing.


```python
try:
    number = int("hello")
except:
    print("There was some error, but I'm not leaving")
    number = 42
```

--

We can catch just some kinds of exceptions too.

```python
try:
    number = int("hello")
except ValueError:
    print("we got an invalid number, proceeding with default 42")
    number = 42
```

--

We can also catch more exceptions or combine them.

```python
try:
    number = int("hello")
except (ValueError, TypeError):
    print("there's something wrong with the value or the type. default 42")
    number = 42
except NotImplementedError:
    print("This feature is not implemented yet, sorry.")
except:
    print("I'm catching every other kind of exception :)")
```

---

## Classes

- We've already been exposed to objects, but where do they come from?

--

#### Object Oriented Programming (OOP)

- Python allows programming in the Object Oriented paradigm.
- This means we can define classes of objects that share attributes and behaviour <!-- .element: class="fragment"-->
- Behaviour is implemented through methods (functions associated with a class) <!-- .element: class="fragment"-->

--

```python
class Vehicle:
    def __init__(self, color): # special method, the constructor
        self.color = color  # this is an attribute
        self.acc = 0        # another attribute

    def accelerate(self):   # this is a method
        self.acc += 2       # fetching a predefined
                            # attribute and modifying it

    def deaccelerate(self): # another method
        self.acc -= 2
```

--

#### instatiating classes

To use a class, we call it like we call functions.

```python
v = Vehicle("red")
print(v.color)
v.accelerate()
print(v.acc) # -> 2
v.deaccelerate()
print(type(v))
```


```text
red
2
<class '__main__.Vehicle'>
```

--

- When we create an object of a certain class, we call it instantiation.
- Classes by themselves don't do anything, but their instantiated objects do.
  - The <span style="color:gold">concept</span> of a Car doesn't take us anywhere, but a specific (<span style="color:gold">instantiated</span>) car can.

--

#### classes from other packages

Remember the Pandas DataFrame?

```python
df = pandas.read_excel("prices.xlsx")
type(df)
```

```text
pandas.core.frame.DataFrame
```


It's a class! 

--

- The `read_excel` function reads the contents of the Excel file into a newly created DataFrame object.
- When we call the methods of an object, we're calling the methods of that object's class!

```python
df["new_prices"] = df["prices"].map(lambda p: p * 1.045)
```

--

```python
df["new_prices"] = df["prices"].map(lambda p: p * 1.045)
```

- We have 3 methods here:
  - `map` is a method.
  - getting a column with `[ ]`, is the implementation of the special method  `__getitem__`
  - setting a column with `[ ]` is also the implementation of `__setitem__`.

--

#### inheritance

- It's also possible for classes to inherit attributes and behaviour from other classes.
- They can modify only part of the behaviour of the parent classes.

```python
class Motorcycle(Vehicle):
    def accelerate(self):
        self.acc += 10

m = Motorcycle("red")
print(m.color)
m.accelerate()
print(m.acc)
```


```text
red
10
```

--

- You'll implicintly use this when using Python's packages.
  - In SciKit-Learn, the <span style="color:gold">`LinearRegression`</span> class inherits from <span style="color:coral">`MultiOutputMixin`</span>, <span style="color:coral">`RegressorMixin`</span> and <span style="color:coral">`LinearModel`</span>.
  - In the same package, the <span style="color:gold">`DecisionTreeClassifier`</span> inherits from <span style="color:coral">`ClassifierMixin`</span> and <span style="color:coral">`BaseDecisionTree`</span>.

--

- And also explicitly:
  - In PyTorch, it's common to build models by creating classes that inherit from <span style="color:coral">`torch.nn.Module`</span>.


--

#### What you need to know about OOP?

- Classes are recipes for the creation of objects: they specify structure and behaviour.
- Data libraries will often return objects, e.g. Pandas DataFrame
- The classes of these objects usually have useful methods, e.g. .map() of DataFrame

--

#### What you need to know about OOP?

- Sometimes libraries expect values that can have the type of any child from a particular class (inheritance).

```python
sklearn.linear_model.LinearRegression.__bases__
```

```text
(sklearn.base.MultiOutputMixin,
 sklearn.base.RegressorMixin,
 sklearn.linear_model._base.LinearModel)
```

- The LinearRegression class from SciKit-Learn inherits from 3 classes.
- Some SciKit-Learn functions can receive any object from a class that inherits from `RegressorMixin`.

---

## debugging

- Jupyter
- `pdb.set_trace()`
- `-m pdb`
- Built-in debuggers

--

#### pdb cheatsheet

```python
import pdb
pdb.set_trace()
```

```python
python3 -m pdb my_script.py
```


```text
(c)ontinue - continues the execution
(n)ext     - execute the next line
(s)tep     - step into a function
(w)here    - print traceback and show current frame
(u)p       - go up one frame in traceback
(d)own     - go down one frame in traceback
(p)rint    - evaluate expression
(b)reak    - set breakpoint (write line)
```