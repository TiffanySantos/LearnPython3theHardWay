from sys import argv
from os.path import exists 
# OMG just realised that this is importing a library like in CS50 #include<stdio.h>
script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}.")

#we could to these two on one line, how?
indata = open(from_file).read() #doing it this way automatically closes the file, you don't need to put .close() at the end

#print(f"The input file is {len(indata)} bytes long.") #returns length, like string length in CS50

#print(f"Does the output file already exist? {exists(to_file)}") #returns a bool
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, "w").write(indata)



