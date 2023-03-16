## Lesson 4
<!-- .slide: id="lesson2_recap" data-background="wheat"-->

- catching errors
- classes
- debugging

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

- Converting a nonnumeric string to an integer is unexpected behaviour, and a ValueError exception is thrown.

--

```python
read_my_file("imaginary_file.txt")
```

```text
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in read_my_file
FileNotFoundError: [Errno 2] No such file or directory: 'imaginary_file.txt'
```

- The file 'imaginary_file.txt' does not exist, so a FileNotFoundError exception is thrown.

--

- Python has many different exceptions.
- Their name is usually sugestive of the problem we're facing.
- Many packages define their own exceptions.
- Sometimes those are not as suggestive.

--

- When we get an exception, we get:
  - the type of the exception
  - usually, a suggestive string
  - a traceback

--

#### traceback

- The traceback is the trace of instructions from our program's origin to the point where the exception hapenned.
- If an exception was thrown inside a function:
  - the traceback includes the line where the function was called
  - and then the line inside the function where the exception was thrown.
- There may be a long list of function calls.

```text
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in read_my_file
FileNotFoundError: [Errno 2] No such file or directory: 'imaginary_file.txt'
```

--

#### traceback

It's a traceback because it allows us to trace the problem to its root.

---

## Catching exceptions

- When an exception happens, we can have a backup plan.
- In Python, we can use a try block to catch an exception and stop the program from failing.


```python
try:
    number = int("hello")
except:
    print("There was some error, but I'm not leaving")
    number = 42
```

--

- We can catch just some exceptions.

```python
try:
    number = int("hello")
except ValueError:
    print("we got an invalid number, proceeding with default 42")
    number = 42
```

--

- We can also catch more exceptions or combine them.

```python
try:
    number = int("hello")
except (ValueError, TypeError):
    print("there's something wrong with the value or the type. default 42")
    number = 42
except NotImplementedError:
    print("This feature is not implemented yet, sorry.")
```

---

## Classes

- We've already been exposed to objects, but where do they come from?

--

#### Object oriented programming (OOP)

- Python allow programming in the Object Oriented paradigm.
- This means we can define classes of objects that share attributes and behaviour
- Behaviour is implemented through methods (functions associated with a class)


```python
class Vehicle:
    def __init__(self, color):
        self.color = color
        self.acc = 0

    def accelerate(self):
        self.acc += 2

    def deaccelerate(self):
        self.acc -= 2
```

--

#### instatiating classes

- To use a class, we call it like we call functions.

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

- When we create an object, we call it instantiation.
- Classes by themselves don't do anything, but their instantiated objects do.

--

#### classes from other packages

- Remember the Pandas DataFrame?

```python
df = pandas.read_excel("prices.xlsx")
type(df)
```

```text
pandas.core.frame.DataFrame
```

- When we call .read_excel, the Pandas library reads the contents of the Excel file into a DataFrame object.

--

- When we call the methods of an object, we're calling functions that operate over that object.

```python
df["new_prices"] = df["prices"].map(lambda p: p * 1.045)
```
- We have 3 methods here:
  - `map` is a method.
  - getting a column with [], is the implementation of the special method  `__getitem__`
  - setting a column with [] is also the implementation of `__setitem__`.

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

#### What you need to know about OOP?

- classes are recipes for the creation of objects
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

- 
- Spyder debugger
- ipython and %pdb magic
  - Jupyter
  - Spyder
- 