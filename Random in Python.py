import random

random_0_to_1 = random.random()*10
print(random_0_to_1)

random_float = random.uniform(1,10)
print(random_float)


random_coin =random.randint(0,1)

if random_coin == 1:
    print("Heads")
else:
    print("Tails")
