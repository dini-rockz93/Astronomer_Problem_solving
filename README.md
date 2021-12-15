# Astronomer_Problem_solving

### Problem Statement
Acme Widget Co are the leading provider of made up widgets and they’ve contracted you to
create a proof of concept for their new sales system.

They sell three products:

```
+--------------+------+--------+
|   Product    | Code | Price  |
+--------------+------+--------+
| Red_Widget   | R01  | $32.95 |
| Green_Widget | G01  | $24.95 |
| Blue_Widget  | B01  | $7.95  |
+--------------+------+--------+
```

To incentivise customers to spend more, delivery costs are reduced based on the amount
spent. Orders under $50 cost $4.95. For orders under $90, delivery costs $2.95. Orders of
$90 or more have free delivery.

They are also experimenting with special offers. The initial offer will be “buy one red widget,
get the second half price”.
Your job is to implement the basket which needs to have the following interface –
- It is initialised with the product catalogue, delivery charge rules, and offers (the format
of how these are passed is up to you)
- It has an add method that takes the product code as a parameter.
- It has a total method that returns the total cost of the basket, taking into account the
delivery and offer rules.

Here are some example baskets and expected totals to help you check your implementation.

```
+---------------------+--------+
|      Products       | Total  |
+---------------------+--------+
| B01,G01             | $37.85 |
| R01,R01             | $54.37 |
| R01,G01             | $60.85 |
| B01,B01,R01,R01,R01 | $98.27 |
+---------------------+--------+
```

### Expectsions 

What we expect to see

- A solution written in easy to understand and up-to-date Python
- A README file explaining how it works and any assumptions you’ve made
- Pushed to a public Github repo, or a copy of the git history (using the `git bundle
create` subcommand and send the resulting file back to us)
Don't worry about writing "the most efficient code possible" - we are more interested to see
how you design the system, but feel free to comment anything that you know is going to be
inefficient and could be improved.

### Solution 


- To run the script `python3 app.py`

---
**NOTE**

Python version used 3.8.0

Once the script, you will be prompted for input to enter the product list
---

### Assumptions:

1. There will be atleas one input, Input values are comma separated
2. product catalogue, delivery charge rules, and offers are initialized in the class `models.py`
3. Solution is implemented using python standard libary, no external packages are used.

