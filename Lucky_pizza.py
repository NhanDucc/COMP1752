from random import randint

def get_random_index(items):
    return randint(0, len(items) - 1)

types = ["margherita", "napoletana", "marinara", "veggie"]
types_price = [6.0, 6.5, 7.0, 7.5]
toppings = ["mushrooms", "cheese", "anchovies", "sausage", "pineapple"]
toppings_price = [0.5, 1.0, 1.5, 1.8, 2.0]
sizes = ["8 inch", "10 inch", "12 inch"]
sizes_price = [0.0, 2.0, 4.0]



random_1 = get_random_index(types)
type = types[random_1]
type_price = types_price[random_1]

pizza_description = type

random_extras = randint(1, 3)
for i in range(random_extras):
    random_2 = get_random_index(toppings)
    topping = toppings[random_2]
    random_3 = get_random_index(sizes)
    size = sizes[random_3]
    if i == 0:
        pizza_description += f" with extra {topping}"
    else:
        pizza_description += f", {topping}"
    extra_price = toppings_price[random_2] + sizes_price[random_3]
    type_price += extra_price

if __name__ == "__main__":
    print()
    print(f"You have won a {size} {pizza_description} worth £{type_price:.2f}")
    print()
