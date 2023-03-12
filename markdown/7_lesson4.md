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



---


---

# NEXT TOPICS

---



---

## debugging