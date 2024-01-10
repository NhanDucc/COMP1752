import random
import test1 as db

size = db.size
pizza_description = db.pizza_description
type_price = db.type_price

name = input("What is your name? ")
if name == "":
    print("Please enter your name")

num_list = range(0, 11)
num = random.choice(num_list)

random_fortunes_list = ["You will meet an attractive stranger.", "Be prepared for rain.", "You will be a brilliant programmer."]
random_fortunes = random.choice(random_fortunes_list)

output = f"Hello {name}. Your lucky number is {num}. {random_fortunes}"

if num != 7:
    print(output)
else:
    output += f" You have won a {size} {pizza_description} worth £{type_price:.2f}"
    print(output)
