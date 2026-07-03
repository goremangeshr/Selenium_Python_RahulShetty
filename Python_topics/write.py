# file = open('text.txt')

# with open('test.txt', 'w') as file:     # File open in write mode
# with open('test.txt', 'r') as file:  # File open in read mode

# Read the file and stored all the lines in list
# Reverse the list
# write the list back to the file

with open('test.txt', 'r') as reader:
    content = reader.readlines()
    reversed(content)
    with open('test.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)











