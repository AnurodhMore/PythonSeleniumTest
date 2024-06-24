#Datatype -> List []

values = [1, 3, 53, "Pyth", 4.5, "sky"]

print(values[0] ) #starts with index zero

print(values[3])

print(values[-1])  # prints last value of the list

print(values[-2]) #second last value

print(values[1:4]) # prints values from indexes 1 to 3

values.insert(4,"on")
print(values)

values.insert(1,"two")
print(values)

values.append("last word") # adds value in the end
print(values)

values[6] = "SKY"

print(values)

del values[4]

print(values)




#Tuples -> Once created cannot be updated  ()

val = (1, 67, 37, "TestPy" )

#val[2] = "New"

print(val[1])

print(val)

#val[1] = "Quiet"

print(val)



# Dicitory -> Key value pair {}


dic = {"a": 2, 4: "four", "c": "helloc"}

print(dic)

print(dic[4])   # it should be printed based on key and not index

print(dic["c"])


dicton = {}

dicton["firstname"] = "Arush"
dicton["lastname"]  = "Test"

print(dicton)

print(dicton["firstname"])
