#file = open('test.txt')
# read the file and store all lines in list
#reverse the list
#write the reveresed list back to the file

#file.close()

with open('test.txt','r') as reader:
    content = reader.readlines()
    reversed(content)
    with open('test.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)
