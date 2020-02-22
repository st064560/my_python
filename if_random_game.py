
import random
var_1 = int(input("число от 1 до 4:"))
var_2 = random.randint(1,4)
if var_1 > var_2:
    print("введите число меньше")
elif var_1 == var_2:
    print("Win")
else:
    print("lose")