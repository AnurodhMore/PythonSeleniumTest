file = open('test.txt')


#print(file.read(3))  #reads in byte
#file.readline() # reads a specific line


#print all the contents of the file line by line

#line1 = file.readline()  #first line
#while (line1!=""):
 #   print(line1)
  #  line1 = file.readline()

for line1 in file.readlines():
    print(line1)



file.close()
