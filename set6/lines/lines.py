import sys

if len(sys.argv)<2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv)>2:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")
else:
    try:
        with open(sys.argv[1], 'r') as file:
            lines = file.readlines()
        lineNumber = 0
        for line in lines:
            if not line.lstrip().startswith("#") and not line.strip() =="":
                #print("line: ", line, end="")
                lineNumber = lineNumber+1
        print(lineNumber,end="")
    except IOError:
        sys.exit("File does not exist")
