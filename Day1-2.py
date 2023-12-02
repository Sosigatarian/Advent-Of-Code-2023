coord_input = open("D:\Advent Of Code 2023\Day1.txt", "r")


spelled = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

firstdigit = ""
seconddigit = ""
spelledpos = 0

stringstore = ""
stringlen = 0

commonletters = 0

total = 0

linepos = 0

currentline = coord_input.readline()
while currentline != "":
    linepos = linepos + 1
    for i in range(len(currentline)):
        if currentline[i].isdigit():
            if firstdigit == "":
                firstdigit = currentline[i]
            seconddigit = currentline[i]
            stringstore = ""
            spelledpos = 0
        else:
            stringstore = f"{stringstore}{currentline[i]}"
            for j in range(len(spelled)):
                for k in range(len(stringstore) - len(spelled[j]) + 1):
                    if stringstore[k:(len(spelled[j])+k)] == spelled[j]:
                        if firstdigit == "":
                            firstdigit = j + 1
                        if k >= spelledpos:
                            seconddigit = j + 1
                            spelledpos = k
    #print(f"{linepos} - {firstdigit}{seconddigit}, {currentline}", end="")
    total = total + int(f"{firstdigit}{seconddigit}")
    currentline = coord_input.readline()
    firstdigit = ""
    seconddigit = ""
    stringstore = ""
    spelledpos = 0
coord_input.close()
print(total)
