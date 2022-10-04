from collections import namedtuple

# construct a namedtuple, so we can access data like customer.name, customer.age
# see https://docs.python.org/3/library/collections.html#collections.namedtuple

Customer = namedtuple('Customer', 'name, age, money')

# create John and James as a Customer
john = Customer('John', 17, 20)
james = Customer('James', 18, 16)
jackson = Customer('Jackson', 35, 50)

wine_price = 20
 

def sell_wine(customer, item_price):
    # only sell wine to customer who is not under 18 and has enough money.
    # Please construct the if conditions
    if customer.age >= 18:
        if customer.money >= wine_price:
            print(f'sell red wine to {customer.name}')
        else:
            print(f'Sorry, {customer.name}, you are too broke to purchase this item.')

    else:
        print(f'Sorry, {customer.name}, you are not old enough to purchase this item.')


sell_wine(john, wine_price)
sell_wine(james, wine_price)
sell_wine(jackson, wine_price)
