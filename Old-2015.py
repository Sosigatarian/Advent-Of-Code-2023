floorinstructions = ""
floor = 0
position = 0

for i in range(len(floorinstructions)):
    if floorinstructions[i] == "(":
        floor = floor + 1
    elif floorinstructions[i] == ")":
        floor = floor - 1
    position = position + 1
    if floor == -1:
        print(position)
        break

#print(floor)