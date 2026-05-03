file = open("text.txt", "r")
for line in file.readlines():
    print(line)
file.close()
file.read() #reads the entire file as a string
file.readline() #reads the next line of the file
file.readable() #returns true if the file can be read
file.closed #returns true if the file is closed