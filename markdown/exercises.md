## After lesson 1

- Create variables
- Get data from users: ``input``
- Numeric types: basics, int vs float, operations
- Strings: basics
- Type conversion, e.g. ``float("3.14")``
- Making decisions: ``if / elif / else``
- Conditions: basics, boolean logic
- ``and   or`` vs. ``&   |``
- ``import`` packages to our programs, e.g. ``import pandas``
- Practical example
  - Load tabular data from Excel file
  - Learn about relative vs. absolute paths
  - Create masks with boolean logic to filter table

--

#### 1.1 loan evolution

--





---

## after lesson 2

- list, tuple, dict
- unpacking
- loops: while, for
- range, enumerate, zip
- list, dict comprehensions

--

#### 2.1. loan all months

--

#### 2.2. IRS calculator

O imposto cobrado sobre o rendimento é feito de forma progressiva por escalões.

Escreva um programa que recebe o rendimento anual bruto e indica o imposto total sobre o rendimento e o rendimento líquido final.


Os escalões estão definidos em 3 listas:

```python
escalao_min = [0, 7479, 11284, 15992, 20700, 26355, 38632, 50483, 78834]
escalao_max = [7479, 11284, 15992, 20700, 26355, 38632, 50483, 78834, float("inf")]
taxa = [14.5, 21, 26.5, 28.5, 35, 37, 43.5, 45, 48]
```

Imposto progressivo significa que o mesmo rendimento vai ser tributado em escalões diferentes, e.g.

```text
Rendimento: 20000€
Tributaçao no escalão 1: (7479 - 0) * 14.5%
Tributaçao no escalão 2: (11284 - 7479) * 21%
Tributaçao no escalão 3: (15992 - 11284) * 26.5%
Tributaçao no escalão 4: (20000 - 15992) * 28.5%
Tributação nos escalões acima do 4 não existe porque o rendimento não é alto o suficiente.
```

--

#### 2.3. data analysis

The code snippet at the bottom, contains 2 lists:
1. the IDs of the products that were transacted in a given day
2. a list of the price of the products

Copy these lists and write code to answer the following questions.


1. Which product was most transacted?
2. What is the ID of the cheapest product?
3. What is the ID of the most expensive product?
4. What is the average product price?
5. What is the total revenue for the day?
6. How many times was product with ID 1 transactioned? And ID 2?
7. Create a dictionary where the keys are IDs of the products transactioned and the values are the counts of the times that product was transactioned in the day.
8. Change the values of the dictionary so that now we have a tuple, where the first element is the number of transactions (as before) and the second is the total revenue of that product, e.g. (1, 1013.73) -> not a the real value.
9. The products with an ID less than 10 are for pet products. How many transactions for pet products?
10. How much revenue for pet products?



```python
products_ids_day1 = [33, 28, 37, 25, 18, 4, 0, 14, 42, 6, 24, 20, 44, 14, 49, 10, 4, 32, 11, 49, 48, 25, 11, 10, 43, 28, 2, 2, 26, 9, 9, 39, 20, 43, 37, 15, 26, 18, 37, 38, 40, 32, 2, 19, 48, 38, 33, 17, 47, 24, 19, 12, 43, 50, 5, 41, 30, 44, 44, 44, 13, 5, 50, 23, 36, 37, 49, 28, 44, 26, 45, 39, 30, 34, 17, 44, 47, 13, 23, 2, 10, 39, 34, 44, 28, 33, 6, 41, 31, 10, 48, 0, 31, 13, 15, 23, 30, 50, 48, 27, 29, 25, 41, 44, 3, 49, 14, 13, 4, 21, 47, 15, 28, 44, 29, 20, 14, 17, 50, 45, 17, 38, 45, 20, 34, 11, 49, 17, 1, 22, 31, 41, 31, 0, 12, 48, 49, 7, 48, 40, 38, 6, 36, 37, 27, 10, 26, 41, 21, 26, 3, 12, 31, 36, 48, 15, 41, 49, 38, 3, 32, 47, 39, 28, 35, 5, 17, 10, 14, 5, 27, 5, 18, 35, 2, 8, 40, 41, 30, 26, 2, 34, 23, 21, 30, 45, 9, 41, 27, 35, 47, 24, 37, 17, 16, 35, 14, 4, 7, 28]

# value at index 0 has the price of product with ID 1, index 1 -> ID 2, ...
ids_price = [37.73, 615.92, 789.51, 362.33, 159.15, 482.15, 332.99, 264.94, 110.41, 917.21, 3.99, 358.15, 6.37, 15.0, 495.94, 26.12, 202.62, 438.0, 672.33, 369.49, 79.68, 703.73, 93.0, 89.97, 3.34, 101.3, 151.12, 807.89, 2.45, 117.8, 426.9, 33.87, 260.01, 341.21, 74.43, 709.64, 218.8, 851.58, 100.12, 217.5, 35.91, 534.81, 114.68, 189.61, 441.05, 65.25, 172.97, 494.9, 87.64, 524.5]
```



---

## after lesson 3

- functions
  - first order functions
  - variable scope
  - lambda
- map, filter
- filter in pandas
- modules & packages
- files
- pathlib





---

## after lesson 4


---

## after course

--

#### A.1. rosbags and interpolaion TODO