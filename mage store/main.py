store = {"apple": 20, "banana": 10,"milk": 50,"bread": 40,"eggs": 30,"cheese": 60, "juice": 45, "chips": 25, "cookies": 35,"chocolate": 15}

cart = []

print("welcome to the Mega store!")
print("Here is what we sell:")
for item in store:
    print(f"{item:>10} --> {store[item]:<10}")

running = True
while running:
    choice = input("Type buy, add, view, cart, or finish:   ")
    choice = choice.lower().strip()

    if choice == "buy":

        while True:
            item = input("what would you like to buy? type quit to close ")
            if item in store:
                cart.append (item)
                print(f"{item} has been succsesfully added to cart...")
            elif item =="quit":
                break
            else:
                print("please write available products correctly..")



    elif choice == "add":
        p = input("enter new product name  ")
        prc = float ( input("enter new product price:  ") )
        store[p] = prc
    elif choice == "view":
        print("in our store we have:  ")
        for item in store:
            print(item , store[item])
    elif choice == "cart":
        print("Your cart has:",end=" ")
        for c in cart:
            print(c,end=", ")
        print()
    elif choice == "finish":     
        total_cost = 0
        for item in cart:
            print(item," - ", store[item])
            total_cost = total_cost + store[item]
        print("total bill is ",total_cost)
        print("your slip has",end=" ")
        for c in cart:
            print("------------------------------")
            print(c,end=", ")
        print()
        leave = input("Are you sure you want to leave? Yes or no:  ")
        print("------------------------------")
        if leave == "yes":
            print("Bye")
            print("come again!")
            running = False
    else:
        print("please write from options")
            