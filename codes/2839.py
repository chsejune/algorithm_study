__author__ = 'Sejune Cheon'

kg = input()
kg = int(kg)

d5 = kg//5
r5 = kg%5

if r5==0:
    print(d5)
elif r5 !=0:
    d3 = r5//3
    r3 = r5%3
    if r3==0:
        print(d5+d3)
    else:
        print(-1)
