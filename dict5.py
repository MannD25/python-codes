grocery_items = {
    "apple": 0.50,
    "banana": 0.30,
    "milk": 1.20,
    "bread": 2.00,
    "eggs": 2.50,
    "cheese": 3.00,
    "chicken": 5.00,
    "rice": 1.00,
    "pasta": 1.50,
    "tomato": 0.80
}
grocery_items2= {
    "apple": 10,
    "banana": 5,
    "milk": 12,
    "bread": 2,
    "eggs": 7,
    "cheese": 3,
    "chicken": 5,
    "rice": 1,
    "pasta": 9,
    "tomato": 9
}
bill=dict()
for v in grocery_items2:
    bill[v]=grocery_items[v]*grocery_items2[v]
print(bill)