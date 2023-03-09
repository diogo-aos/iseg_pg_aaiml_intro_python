<!-- .slide: id="lesson2_recap" data-background="coral"-->

## Lesson 2 Recap

--

### lists

```python
l = [1,2,3,4,5]  # creating a list
l[1] # getting an element ->2
l.append(6) # adding value 6 -> [1,2,3,4,5,6]
l.remove(1) # removing value 1 -> [2,3,4,5,6]
l.index(3)  # finding value 3 -> 1
l = l + [7,8] # appending lists -> [2,3,4,5,6,7,8]
l.extend([7,8]) # does the same thing
l.insert(0, 42) # add 42 at index 0 -> [42,2,3,4,5,6,7,8]
len(l)      # size of list 8
l[0] = 24 # change value at index 0 -> [24,2,3,4,5,6,7,8]
l[2:-2] # slice the list -> [3,4,5,6]
24 in l # -> True
```

--

### tuples

```python
t = (1,2,3,4)
t2 = 1,2,3,4
t[0]  # -> 1
t[0] = 7 # TypeError: 'tuple' object does not support item assignment
t[:-1] # -> (1,2,3)
t + (5,6) # _> (1,2,3,4,5,6)
```

--

### unpacking

```python
t = (1,2,3)
a,b,c = t  # now a=1, b=2, c=3

l = [4,5,6]
a,b,c = l  # a=4, b=5, c=6

l=[1,2,3,4,5,6]
a,b,*nums = l # a=1, b=2, nums=[3,4,5,6]
```

--

### loops > while

```python
l = [1,2,3,5,8,13]
total, i = 0, 0
while i < len(l):
    total += l[i]
    i += 1
print(total)
```

--

### loops > for

```python
l = [1,2,3,5,8,13]
total = 0
for i in range(len(l)):
    total += l[i]
print(total)
```

--

#### range

```python
l = list(range(10,15))
```

```python
 [10,11,12,13,14]
```

#### enumerate
<!-- .element: class="fragment" data-fragment-index="2"-->

```python
list(enumerate(l))
```
<!-- .element: class="fragment" data-fragment-index="2"-->
```python
[(0, 10), (1, 11), (2, 12), (3, 13), (4, 14)]
```
<!-- .element: class="fragment" data-fragment-index="2"-->

--

#### zip

```python
names = ["ten", "eleven", "twelve", "thirteen", "fourteen"]
list(zip(names, l))
```

```python
[('ten', 10),
 ('eleven', 11),
 ('twelve', 12),
 ('thirteen', 13),
 ('fourteen', 14)]
 ```


--

#### enumerate in loops

```python
for i, phrase in enumerate(phrases):
    if "Python" in phrase:
        print(i)
```

#### zip in loops
<!-- .element: class="fragment" data-fragment-index="3"-->

```python
for name, age in zip(names, ages):
    print(f"The writer {name} died with {age} years.")
```
<!-- .element: class="fragment" data-fragment-index="3"-->

--

### list comprehensions

```python
l = []
for i in range(100):
    if i % 2 == 0 and i % 4 != 0:
        l.append(i)
```

```python
l = [i for i in range(100) if i % 2 == 0 and i % 4 != 0]
```

--

### dict
```python
authors = {
    "Saramago": 87,
    "Pessoa": 47,
    "Camões": 56
    }

authors_lst = [("Saramago", 87), ("Pessoa", 47), ("Camões", 56)]
authors = dict(authors_lst)

authors = {
    "Saramago": {"died_at": 87, "first_name": "José"},
    "Pessoa": {"died_at": 47, "first_name": "Fernando"},
    "Camões": {"died_at": 56, "first_name": "Luís"},
    }

```

--

### dict > get, set, remove

```python
authors["Saramago"]  # -> 87
authors.get("Saramago")  # -> 87

authors["Vieira"] = 89
authors["Queirós"] = 54

authors.pop("Saramago") # tries to remove key "Asimov" and
                      # returns None if it does not exist
del authors["Saramago"] # just deletes key "Saramago"
```

--

### dict > loops

```python
for k in authors:
    print(f"{k} died at age {authors[k]}")

for k,v in authors.items():
    print(f"{k} died at age {v}")

for i, (k,v) in enumerate(authors.items()):
    print(f"author #{i}: {k} died at age {v}")
```

--

### dict > comprehensions

```python
authors_e = {name: age \
                for name, age in zip(names, ages) \
                if "e" in name}
# \ allows breaking a long instruction into several lines
```