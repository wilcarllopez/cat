#cat.py
#Wilcarl Lopez
#Import the argparse library
import argparse

#Start of functions
def read_file(texts):
    """Reads and open the text file"""
    for text in texts:
        with open(text + '.txt','r') as f:
            t = ""
            t += "\n" + f.read()
    return "Successfully read the file.\n" + t

def create_file(texts):
    """Creates a text file"""
    for text in texts:
        with open(text+".txt",'w+') as f:
            f.write(input("Content: "))
    return "Successfully created a file"

def write_file(texts):
    """Write content for the file"""
    for text in texts:
        with open(text+".txt",'w') as f:
            f.write(input("Content: "))
    return "Successfully wrote a file"

def cat_file(texts):
    """Concatenate text files and save to new file"""
    final_text = input("Save to: ")
    
    with open(final_text + '.txt', 'w') as outfile:
        for text in texts:
            with open(text + ".txt") as infile:
                for line in infile:
                    outfile.write(line + " ")
    return "Successfully concatenated the file"

def append_file(texts):
    """Append content to the file"""
    for text in texts:
        with open(text+".txt",'a') as f:
            f.write(input("Content to be added: "))
    return "Successfully appended to the file"

def prepend_file(texts):
    """Prepend content to the file"""
    content = input("Content to be added: ")
    for text in texts:
        with open(text+".txt",'r+') as f:
            old = f.read()
            f.seek(0)
            f.write(str(content)+ " " + old)
    return "Successfully prepended to the file"
#End of functions


parser = argparse.ArgumentParser()
#Adding arguments
parser.add_argument('texts', nargs='*', help='Filename of the text file/s')
parser.add_argument('-r','--read', action='store_true', help='Read the text file')
parser.add_argument('-c', '--create',action='store_true',help='Create a text file')
parser.add_argument('-w', '--write',action='store_true', help='Write content for the text file')
parser.add_argument('-cat', '--concat',action='store_true', help='Concatenate files and save it to another text file')
parser.add_argument('-app', '--append',action='store_true', help='Append content to the end of file chosen')
parser.add_argument('-prp', '--prepend',action='store_true', help='Prepend content at the start of file chosen')
args = parser.parse_args()
#End of addition of arguments

#If-else statements
if args.read:
    print(read_file(args.texts))
elif args.create:
    print(create_file(args.texts))
elif args.write:
    print(write_file(args.texts))
elif args.concat:
    print(cat_file(args.texts))
elif args.append:
    print(append_file(args.texts))
elif args.prepend:
    print(prepend_file(args.texts))
#End of if-else statements

