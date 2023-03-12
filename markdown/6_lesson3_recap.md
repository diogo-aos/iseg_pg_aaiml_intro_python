
<!-- .slide: id="lesson2_recap" data-background="coral"-->


## Lesson 3 Recap

- functions
  - first order functions
  - variable scope
  - lambda
- map, filter
- filters in pandas: masks
- modules & packages
- files
- pathlib: swiss army knife for files

--

#### functions

```python
def sum_2(a):
    b = a + 2
    return b
    # return a, b
```

- the function exits when it reaches the end of the instructions
- or when the instruction ``return`` is used
- functions can return multiple values


--

#### variable scope in functions

- Local and global variables

```python
x = 3

def sum_2(a):
    b = a + 2
    print(x) # -> 3, x is global variable
    return b

print(sum_2(x))  # -> 5
print(x) # -> 3
print(a)  # a is local variable of function 
          # -> NameError: name 'a' is not defined
```

--

#### first class functions

- functions are also objects that can be given to variables and functions

```python
def sum_2(a):
    b = a + 2
    return b

f = sum_2
f(2) # -> 4
```

--

#### lambda

```python
f = lambda a: a + 2
f(2) # -> 4

g = lambda a,b: a+b**2
g(2,3) # -> 11
```

⚠️⚠️ keep your lambdas short, simple and clear ⚠️⚠️

--

#### map

- apply a function to a "list" of values

```python
percent = 4.5
new_prices = list(map(lambda p: p * (1 + percent / 100), prices))
```

--

#### pandas and map

```python
df = pandas.read_excel("prices.xlsx")
df["new_prices"] = df["prices"].map(lambda p: p * 1.045)
```

--

#### filter

```python
vegetables_prices = list(filter(lambda p,c: c == 'vegetables',
                                zip(prices, categories)))
```

--

#### filers in pandas

```python
df = pandas.read_excel("prices.xlsx")
vegetables = df[df["category"] == "vegetable"]
```

- We use masks, not the filter function.

--

#### modules and packages

- Python (.py) files in the same folder as our program can be directly imported.
- We can organize our modules in packages (don't forget those `__init__.py` files)

```text
retailxy/
 |- __init__.py
 |- products.py
 |
 |- marketing/
 |    |- __init__.py
 |    |- discounts.py
 |    |- promotions.py
```

```python
import retailxy.marketing as mark
from products import *
```

--

--

#### files

```python
f = open("test_file.txt", "w+")  # open a file
data = f.read()
f.write("\njust one more line")
f.close() # don't forget to close your files
```

--

#### context manager

```python
with open("test_file.txt", "r") as f:
    data = f.read()
print(data)
```

- The file is closed for us at the end of the context (with block)

--

#### binary pickle

- We can store (almost) any Python object in a binary file with Pickle


```python
import pickle

with open("test.pkl", "wb") as f:
    pickle.dump(test_dict, f)

with open("test.pkl", "rb") as f:
    loaded_dict = pickle.load(f)
print(loaded_dict)
```

--

#### pathlib - Path

```python
from pathlib import Path
test_path = Path("test_file.txt")
test_path.exists() # returns True if the file exists
```

--

#### pathlib - open, read, write

```python
test_path = Path("test_file.txt")
with test_path.open("a") as f:
    f.write("line 3\n")

with test_path.open("a") as f:
    data = f.readlines()
print(data)
```

--

#### pathlib - many utilities

```python
p.is_dir()  # is this path a directory?
list(p.iterdir())  # lists all files in directory
list(p.glob("*.py"))  # lists all .py files in the directory
```




