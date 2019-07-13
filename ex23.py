import sys #import sys library, allows use of argv
script, encoding, error = sys.argv # argv provices acces to command line arguments via the script


def main(language_file, encoding, errors): 
    line = language_file.readline()
# function to read a line and return a print out of each line
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)
# returning main at the within the function creates a loop which has an if statement (avoiding an infinite loop)
def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)
# breaks up string into bytes
    print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding="utf-8") #open languages doc

main(languages, encoding, error) # close function main