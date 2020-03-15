# 1)
OUTPUT_FILE = "name.txt"                         # define the output file
input_name = input("Enter your name: ")          # receive a name from the user
out_file = open(OUTPUT_FILE, 'w')                # open the output file
out_file.write(input_name)                       # write the name to the file
out_file.close()                                 # close the file

# 2)
INPUT_FILE = "name.txt"                         # define the input file
in_file = open(INPUT_FILE, 'r')                 # open the input file
file_name = in_file.readline()                  # read in the first line of the file (as a string)
print("Your name is {}".format(file_name))      # print the name just read in
in_file.close()                                 # close the file

# 3)
in_file = open("numbers.txt", "r")              # open the numbers input file
first_number = int(in_file.readline())          # read in the first number/line as an integer
second_number = int(in_file.readline())         # read in the second number/line as an integer
print(first_number + second_number)             # add the two integers together
in_file.close()                                 # close the file

# 4)
in_file = open("numbers.txt", "r")              # open the numbers input file
count = 0                                       # add a count feature that adds up each line as it is read in
for line in in_file:                            # for loop that stands until there are no more lines in the text file
    number = int(line)                          # read in the next line/number from the file
    count += number                             # adding the new line/number to the existing amount
print(count)                                    # displaying the total number
in_file.close()                                 # close the file
