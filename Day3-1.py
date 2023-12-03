engine = open("D:\Advent-Of-Code-2023\Day3.txt", "r")

linenumber = 0

lastline = "............................................................................................................................................"
currentline = engine.readline()
nextline = engine.readline()

currentnumber = ""
onnumber = False
includenumber = False

addnumber = False

continuestate = True

total = 0

while continuestate:
    linenumber = linenumber + 1
    print(linenumber, end=": ")
    if nextline == "":
        continuestate = False
        nextline = "............................................................................................................................................"
    for i in range(len(currentline)):
        if currentline[i].isdigit():
            onnumber = True
            currentnumber = f"{currentnumber}{currentline[i]}"
            if (not lastline[i].isdigit() and lastline[i] != ".") or (not nextline[i].isdigit() and nextline[i] != "."):
                includenumber = True
        elif currentline[i] == ".":
            if onnumber and includenumber:
                addnumber = True
                includenumber = False
            if (not lastline[i].isdigit() and lastline[i] != ".") or (not nextline[i].isdigit() and nextline[i] != "."):
                if onnumber:
                    addnumber = True
                includenumber = True
            else:
                if not addnumber:
                    currentnumber = ""
                includenumber = False
            onnumber = False
        else: # if currentline[i] is-symbol
            includenumber = True
            if onnumber:
                addnumber = True
                onnumber = False
        if addnumber:
            print(currentnumber, end=", ")
            total = total + int(currentnumber)
            currentnumber = ""
            addnumber = False
    currentnumber = ""
    onnumber = False
    includenumber = False
    addnumber = False
    lastline = currentline
    currentline = nextline
    nextline = engine.readline()
    print("(", total, ")", sep="")

engine.close()
print(total)