import math
import random

print(math.e,math.pi,math.log(2,2),math.log(2,10))
print(math.sqrt(4))
print((-1) ** 0.5)
for _ in range(40):
    print(random.randint(1,10))

stores = ['7-11','hi-life','ok','fami','pxmart']
for _ in range(10):
    print(random.choice(stores))

cards = ['A','Q','K','J','10']

for _ in range(10):
    random.shuffle(cards)
    print(cards)