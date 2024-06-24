it = 5

while it>=1:
    print(it)
    it =it -1

print("While loop ends")


ret = 10

while ret>=1:
    if ret ==9:
        ret = ret -1
        continue
    if ret == 3:
        break
    print(ret)
    ret = ret - 1

