<!-- .slide: id="lesson2" data-background="white"-->

## Lesson 2

---

## Basic data structures
### List

--

So far we've stored only single values in variables.

The ``list`` allows us to store multiple values.

--

#### Create empty list

We create a list with the list function or simply [].

```python
l1 = list()
l2 = []
```

--

#### Create list with content

We can create a list initialized with some elements.

```python
lst_ints = [1,2,3,4,5]
lst_floats = [3.14, 9.8, 6.64e-34]
lst_str = ["cobra", "anaconda", "python"]
lst_mixed = [1, 3.14, "cobra"]
```

--

#### Size of the list

```python
lst_ints = [1,2,3,4,5]
len(lst_ints)  # this function gives the size of the list
               # and many other data structures -> 5
```

--

#### Adding elements

Like strings, lists have several methods that help with their interaction.

```python
lst_floats = [3.14, 9.8, 6.64e-34]
lst_floats.append(1.61)  # add golden ratio
lst_floats += [2.7]  # add euler's constant, less efficient
```

--

```python
lst_floats += [2.7]  # add euler's constant
```

What is `+=`?

It is equivalent to having

```python
lst_floats = lst_floats + [2.7]
```

Lists support the `+` operator: the list on the right is concatenated to the list on the left.

--

We can also add elements at specific positions with the .insert method.

```python
# add the double of pi at index 0
lst_floats.insert(0, 3.14*2)
```

--

#### Getting an element

It works like we saw for strings.

```python
l = [1,2,3,4,5,6]
l[0]  # gives the 1st element -> 1
l[1]  # gives the 2nd element -> 2
l[-1] # gives the last element -> 6
```

--

#### Slicing

We may get a slice of the list.

```python
l = [1,2,3,4,5,6]
l[0:3]  # returns a list with all elements
        # from the 1st to the 3rd elements
        # -> [1,2,3]
```

--


#### Slicing rule

- list[A:B] or list[A:B:C] or list[A:B:C]
- A is the starting index of the slice
  - if not supplied, it's assumed to be the beginning
- B is the last index of the slice, but is not included
  - if not supplied, it's assumed to be the end
- C is the jump between consecutive elements
  - if not supplied, it's assumed to be 1
  - if it is negative, we get elements in the reverse order


--

#### Slicing examples

```python
l = [1,2,3,4,5,6]
l[0:3]  # returns a list with all elements starting 
        # on index 0 and ending on 2 -> [1,2,3]
l[0:1]  # returns a list with just the 1st element -> [1]
l[1:1]  # returns an empty list -> []
l[:]    # returns all elements of the list -> [1,2,3,4,5,6]
l[:-2]  # returns all elements except the last 2 -> [1,2,3,4]
```

--

#### More Slicing

```python
l = [1,2,3,4,5,6]
l[-3:-1]  # returns all elements starting on the 3rd last #
          # and finishing on the 2nd last -> [4,5]
l[-3:]  # list with all elements from the 3rd last onwards -> [4,5,6]
l[::2]  # returns every other element, starting on index 0 -> [1,3,5]
l[1::2]  # returns every other element, starting on index 1 -> [2,4,6]
l[1::3]  # returns every 3rd element, starting on index 1 -> [2,5]
```

--

#### Even more slicing

```python
l = [1,2,3,4,5,6]
l[::-1]  # returns all elements in reverse order -> [6,5,4,3,2,1]
l[::-2]  # returns every other element in reverse order -> [6,4,2]
l[4:0:-1]  # all elements from the 5th to the 2st in reverse
           # -> [5,4,3,2]
l[-2:0:-1]  # all elements from the 2th last to the 1st in reverse 
            # -> [5,4,3,2]
```

--

#### Removing an element: remove

The remove method deletes a given value from the list.
It it exists more than once in the list, the 1st occurrence is removed. 

```python
lst_floats.remove(9.8)  # removes the value
```

--

If the value does not exist in the list, an error is thrown.

![](img/l2/list_valuerror.png)

--

#### Extend an existing list

```python
l.extend(lst_floats)  # adds to list l all elements from lst_floats
l += lst_floats  # alternative
```

--

####  Counting

```python
lst_floats.count(3.14)  # how many times 3.14 occurs in the list
                        # -> 1
```

--

#### check existence

```python
if 3.14 in lst_floats:
    print("we have a Pi")
```

The ``in`` operator checks if the value on the left exists in the data structure on the right.

--

#### where is waldo?

```python
pi_pos = lst_floats.index(3.14)
print(f"I found Pi at index {pi_pos}")
```

The `.index` method returns the position where the given value is in the list.
If the value is not in the list, a ``ValueError`` is thrown.

--

#### Other methods

```python
l.reverse()  # reverses the order of all values
l = l[::-1]  # equivalent to l.reverse()
l.sort()  # sorts all values
l.pop(0)  # removes and returns the element at index 0
l.pop()  # removes and returns the last element
```

---

## Basic data structures
### tuple

A tuple works exactly like a list, but doesn't support assignment. It is an imutable data structure.

```python
t = (1,2,3,4)
t2 = 1,2,3,4
t[0]  # -> 1
t[0] = 7 # TypeError: 'tuple' object does not support item assignment
t[:-1] # -> (1,2,3)
t + (5,6) # _> (1,2,3,4,5,6)
```

--

#### tuple <-> list

We can easily convert between lists and tuples.

```python
t = (1,2,3,4)
l = list(t)
t2 = tuple([5,6,7,8])
```

---

## Basic data structures
### unpacking lists and tuples

```python
t = (1,2,3)
a,b,c = t  # now a=1, b=2, c=3

l = [4,5,6]
a,b,c = l  # a=4, b=5, c=6

l=[1,2,3,4,5,6]
a,b,*nums = l # a=1, b=2, nums=[3,4,5,6]
```

---

## Loops

They execute a set of instructions while a given condition is true:

```python
is_coffee_ready = False
while is_coffee_ready != True:
    print("continue groggy")
    is_coffee_ready = check_coffee_status()
```

What is being used for the condition must change, otherwise we might have an infinite loop.
<!-- .element: class="fragment" -->

--

Let's sum a list of numbers:

```python
l = [1,2,3,5,8,13]
total, i = 0, 0
while i < len(l):
    total += l[i]
    i += 1
print(total)
```

Actually, Python has the sum function, so don't do that -> `sum(l)`
<!-- .element: class="fragment" -->

--

We needed to declare a variable just for increasing the position of the list element, but we also have the ``for`` loop which makes this kind of logic easier.

```python
l = [1,2,3,5,8,13]
total = 0
for i in range(len(l)):
    total += l[i]
print(total)
```

Here the ``range`` function returns a list from 0 to the size of the list l:

`[0,1,2,3,4,5]`

--

Actually, ``range`` returns an **iterable** that goes from a number to another higher number.

```python
# we can convert this iterable to a list easily
list(range(3))       # -> [0,1,2]
list(range(2,6))     # -> [2,3,4,5] 
list(range(0,10,2))  # -> [0,2,4,6,8] 
list(range(10,0,-2)) # -> [10,8,6,4,2] 
```

We can convert this iterable to a list, but we don't have to do it in the context of the for loop.

--

Lists have another property: they're also iterables. That means we don't even need the range function in the last example.

```python
l = [1,2,3,5,8,13]
total = 0
for num in l:
    total += num
print(total)
```

---

## Loops
### enumerate

Let's now say we are given a list of phrases and want to print the position of the phrases that include the word "Python".

```python
phrases = [
    "The last patient was bitten by a Python.",
    "The number of bites of last year is the highest ever.",
    "The number of Pythons in the wild must have increased.",
    "We must implement some policy to help us."
]
```

--

One way to solve this would be to use the range function.

```python
for i in range(len(phrases)):
    if "Python" in phrases[i]:
        print(i)
```

--

The enumerate function can help us here.

```python
for i, phrase in enumerate(phrases):
    if "Python" in phrase:
        print(i)
```


``enumerate`` receives a list and returns a list of tuples
- 1st element of the tuple is a number that goes from 0 to the size of the original list
- 2nd element is the value on that position.

--

```python
l = [2,4,6,8]
list(enumerate(l)) # -> [(0,2), (1,4), (2,6), (3,8)]
```

Actually, enumerate returns an iterable, that's why we convert it here to a list.

It also can receive any iterable, not just a list.
<!-- .element: class="fragment" -->

--

`enumerate` can also start on any number we want.

```python
l = [2,4,6,8]
list(enumerate(l))           # -> [(0,2), (1,4), (2,6), (3,8)]
list(enumerate(l, start=-1)) # -> [(-1,2), (0,4), (1,6), (2,8)]
```

---

## Loops
### zip

Let's now say we have a list of names and ages and want to print them.

```python
names = ["Saramago", "Pessoa", "Camões"]
ages = [87, 47, 56]
```

--

Using what we know, we can implement it like this.

```python
for i in range(len(names)):
    print(f"The writer {names[i]} died with {ages[i]} years.")
```

--

But the ``zip`` function can simplify this.


```python
for name, age in zip(names, ages):
    print(f"The writer {name} died with {age} years.")
```

--

``zip`` receives 2 or more lists and creates a new list where each element is a tuple with the values of the original 2 lists.

```python
names = ["Saramago", "Pessoa", "Camões"]
ages = [87, 47, 56]
print(list(zip(names, ages)))
# -> [('Saramago', 87), ('Pessoa', 47), ('Camões', 56)]
```

--

```python [3]
names = ["Saramago", "Pessoa", "Camões"]
ages = [87, 47, 56]
print(list(zip(names, ages)))
# -> [('Saramago', 87), ('Pessoa', 47), ('Camões', 56)]
```

`zip`, like `enumerate`, actually returns an iterable - that's why we converted it to a list before printing.

`zip` can receive any iterable, not just lists.
<!-- .element: class="fragment" -->

`zip` can receive any number of iterables as input, e.g. `zip(l1, l2, l3, ...)`
<!-- .element: class="fragment" -->

--

When the size of the input iterables is different, ``zip`` will return an iterable with the size of the shorter input.

```python [3]
names = ["Saramago", "Pessoa", "Camões"]
numbers = [1,2,3,4,5,6]
print(list(zip(names, numbers)))
# -> [('Saramago', 1), ('Pessoa', 2), ('Camões', 3)]
```

---

## Comprehensions
### list

Let's say we would like to create a list with all even numbers from 0 to 99, that are not divisible by 4.

--

A possible implementation would be

```python
l = []
for i in range(100):
    if i % 2 == 0 and i % 4 != 0:
        l.append(i)
```

--

List comprehensions are a way to concisely create lists.

```python
l = [i for i in range(100) if i % 2 == 0 and i % 4 != 0]
```

```python
l2 = [f"Author {n} died at age {a}." for n,a in zip(names, ages)]
```
<!-- .element: class="fragment" -->

---

## Exercise
### Redo the loan exercise

Redo the loan execise, but simulate the amount owed each month until the loan is totally repayed.

---

## Basic data structures
### dict

- A dictionary (``dict``) is like a key/value database.
- We can store any value we want and connect it to a key, which we will use to retrieve it.

--

#### creating a dict

```python
authors = {}  # empty dict
authors = dict() # empty dict
authors = {"Saramago": 87}
country_codes = {351: "Portugal"}
```

The types of both keys and values can be anything.

--

We can initialize a dict with many values.

```python
authors = {
    "Saramago": 87,
    "Pessoa": 47,
    "Camões": 56
    }
```

--

We can initialize a dict from a list of 2 element tuples.

```python
authors_lst = [("Saramago", 87), ("Pessoa", 47), ("Camões", 56)]
authors = dict(authors_lst)
```

--

Actually, we can initialize it from an iterable, so we could have done something like this.

```python
names = ["Saramago", "Pessoa", "Camões"]
ages = [87, 47, 56]
authors = dict(zip(names, ages))
```

--

We can have nested dicts too.

```python
authors = {
    "Saramago": {"died_at": 87, "first_name": "José"},
    "Pessoa": {"died_at": 47, "first_name": "Fernando"},
    "Camões": {"died_at": 56, "first_name": "Luís"},
    }
```

--

#### getting a value

```python
authors["Saramago"]  # -> 87
authors.get("Saramago")  # -> 87

authors["Asimov"]  # KeyError: 'Asimov'
authors.get("Asimov")  # -> None
authors.get("Asimov", default=-1) # -> -1
```

--

#### inserting a value

```python
authors["Vieira"] = 89
authors["Queirós"] = 54
```

--

#### removing a value


```python
authors.pop("Vieira") # removes key "Vieira" and returns its value
                      # -> 89
authors.pop("Asimov") # tries to remove key "Asimov" and
                      # returns None if it does not exist
authors.pop("Asimov", default=-1) # tries to remove key "Asimov" and
                                  # returns -1 if it does not exist
del authors["Saramago"] # just deletes key "Saramago"
del authors["Asimov"] # KeyError: 'Asimov'
```

--

#### useful methods

```python
list(authors) # returns list of keys
list(authors.keys()) # same thing
list(authors.values()) # list of dict's values
list(authors.items()) # list of (key, value) tuples
```

--

#### dicts and loops

Print the age at which each author died:

```python
for k in authors:
    print(f"{k} died at age {authors[k]}")
```

```python
for k,v in authors.items():
    print(f"{k} died at age {v}")
```
<!-- .element: class="fragment" -->

```python
for i, (k,v) in enumerate(authors.items()):
    print(f"author #{i}: {k} died at age {v}")
```
<!-- .element: class="fragment" -->

#### 

---

## Comprehensions
### dict

Create a dictionary with the authors that have the letter 'e' on their name.

```python
authors_e = {name: age \
                for name, age in zip(names, ages) \
                if "e" in name}
# \ allows breaking a long instruction into several lines
```
<!-- .element: class="fragment" -->




