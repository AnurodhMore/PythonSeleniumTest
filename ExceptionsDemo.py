ItemsCart = 0

#if ItemsCart!=2:
#    raise Exception("Items not found")

#if ItemsCart!=4:
#    pass

#assert(ItemsCart==4)

try:
    with open('edeft.txt','r') as reader:
        reader.read()
except Exception as e:
    print(e)

finally:
    print("Reached finally block")
#except:
    #print("Reached here a try block failed")