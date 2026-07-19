store = {"apple": 20, "banana": 10,"milk": 50,"bread": 40,"eggs": 30,"cheese": 60, "juice": 45, "chips": 25, "cookies": 35,"chocolate": 15}

cart = []
total_cost = 0

def greet():
    print("welcome to the Mega store!")
    print("Here is what we sell:")
greet()
for item in store:
    price = store[item]
    print(item, "-" , price ,"rs")

while True:
    choice = input("Type buy or Quit:   ")

    if choice == "quit":
        break
    if choice == "buy":
        item = input("what would you like to buy?")
        if item in store:
            cart.append (item)