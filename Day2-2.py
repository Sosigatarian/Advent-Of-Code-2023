gameput = open("D:\Advent-Of-Code-2023\Day2.txt", "r")

gameid = 0
total = 0
power = 0

highestred = 0
highestgreen = 0
highestblue = 0

currentnumber = ""
on_number = True
currentcolor = ""
on_color = False



currentline = gameput.readline()
while currentline != "":
    gameid = gameid + 1
    for i in range((7+len(str(gameid))),len(currentline)): #Starts at first number, after "Game #: "
        if on_number and currentline[i].isdigit():
            currentnumber = f"{currentnumber}{currentline[i]}"
        elif on_number:
            on_number = False
            on_color = True
        elif on_color and currentline[i] != ";" and currentline[i] != "," and currentline[i] != " ":
            currentcolor = f"{currentcolor}{currentline[i]}"
            if i == (len(currentline) - 2):
                if currentcolor == "red" and int(currentnumber) > highestred:
                    highestred = int(currentnumber)
                elif currentcolor == "green" and int(currentnumber) > highestgreen:
                    highestgreen = int(currentnumber)
                elif currentcolor == "blue" and int(currentnumber) > highestblue:
                    highestblue = int(currentnumber)
        elif on_color and (currentline[i] == ";" or currentline[i] == (",")):
            if currentcolor == "red" and int(currentnumber) > highestred:
                highestred = int(currentnumber)
            elif currentcolor == "green" and int(currentnumber) > highestgreen:
                highestgreen = int(currentnumber)
            elif currentcolor == "blue" and int(currentnumber) > highestblue:
                highestblue = int(currentnumber)
        elif on_color:
            on_color = False
            on_number = True
            currentnumber = ""
            currentcolor = ""
    power = highestred * highestgreen * highestblue
    total = total + power
    print(highestred, highestgreen, highestblue, power, total, " - ", currentline, end="")
    currentline = gameput.readline()
    highestred = 0
    highestgreen = 0
    highestblue = 0
    on_color = False
    on_number = True
    currentnumber = ""
    currentcolor = ""

gameput.close()
print("\n",total, sep="")
