from sys import argv

script, filename = argv

txt = open(filename) #open the textfile

print(f"Here's your file {filename}")
print(txt.read()) # call a function called read to the txt file

txt.close() 

