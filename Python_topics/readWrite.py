
file = open("test.txt") # Open file
# print(file.read())             # Read all the content of file
# print(file.read(7))            # Read specific content from file
# print(file.readline())           # Read one single line
# print(file.readline())           # Read one single line
for line in file.readlines():      # Read line by line
    print(line)



# print line by line using readline method()
# line = file.readline()
# while line!="":
#     print(line)
#     line = file.readline()





file.close()            # always Close file to prevent from currupt