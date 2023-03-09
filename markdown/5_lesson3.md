## Lesson 3
<!-- .slide: id="lesson2_recap" data-background="white"-->



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


```python
df = pandas.read_excel("prices.xlsx")
```

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

<!-- .element: class="fragment" data-fragment-index="2"-->


```text
In [46]: df.shape
Out[46]: (50, 2)
```

<!-- .element: class="fragment" data-fragment-index="2"-->


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