
coord_input = open("D:\Python-Projects-Experimentation\Advent Of Code 2023\Day1.txt", "r")
coord_string = coord_input.read()
coord_input.close()

spelled = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

firstdigit = ""
seconddigit = ""

stringstore = [" ", " ", " ", " ", " "]
stringlen = 0

commonletters = 0

total = 0

for i in range(len(coord_string)):
    if coord_string[i].isdigit():
        if firstdigit == "":
            firstdigit = coord_string[i]
        seconddigit = coord_string[i]
        stringstore = [" "] in range(5)
        stringlen = 0
    elif coord_string[i] == "\n":
        total = total + int(f"{firstdigit}{seconddigit}")
        firstdigit = ""
        seconddigit = ""
        stringstore = [" "] in range(5)
        stringlen = 0
    else:
        stringstore[stringlen] = coord_string[i]
        stringlen = stringlen + 1
        for j in range(len(spelled)):
            for k in range(len(spelled[j])):
                if stringstore[k] == spelled[j][k]:
                    commonletters = commonletters + 1
            if commonletters == len(spelled[j]):
                if firstdigit == "":
                    firstdigit = j + 1
                seconddigit = j + 1
                stringstore = [" "] in range(5)
                stringlen = 0
            commonletters = 0
        if stringlen == 5:
            for l in range(4):
                stringstore[l] = stringstore[i + 1]
            stringstore[5] = " "
            stringlen = 4
total = total + int(f"{firstdigit}{seconddigit}")

print(total)