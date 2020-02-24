water = 1200
milk = 540
beans = 120
cups = 9
money = 550


def state():
    print("The coffee machine has:")
    print(water, " of water")
    print(milk, "of milk")
    print(beans, "of coffee beans")
    print(cups, "of disposable cups")
    print(money, "of money")
    return


def fill():
    fill_1 = int(input("Write how many ml of water do you want to add:"))
    fill_2 = int(input("Write how many ml of milk do you want to add:"))
    fill_3 = int(input("Write how many grams of coffee beans do you want to add:"))
    fill_4 = int(input("Write how many disposable cups of coffee do you want to add:"))
    global water
    water = water + fill_1
    global milk
    milk = milk + fill_2
    global beans
    beans = beans + fill_3
    global cups
    cups = cups + fill_4
    return state()



def take():
    global money
    print("I gave you $ ", money)
    money = money - money
    return state()


def buy():
    want = int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:"))
    if want == 1:
        global water
        water = water - 250
        global beans
        beans = beans - 16
        global money
        money = money + 4
        global cups
        cups = cups - 1
    elif want == 2:
        water = water - 350
        global milk
        milk = milk - 75
        beans = beans - 20
        money = money + 7
        cups = cups - 1
    elif want == 3:
        water = water - 200
        milk = milk - 100
        beans = beans - 12
        money = money + 6
        cups = cups - 1
    return state()

var_1 = str(input("Write action (buy, fill, take):"))
state()
if var_1 == "buy":
    buy()
elif var_1 == "fill":
    fill()
elif var_1 == "take":
    take()