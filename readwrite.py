input_file = open("text.txt", "r")
output_file = open("output.txt", "w")
for line in input_file.readlines():
    output_file.write(line)
input_file.close()
output_file.close()
