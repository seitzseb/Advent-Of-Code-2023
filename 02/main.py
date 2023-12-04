import regex as re

with open("input.txt","r") as f:
    inp = f.readlines()

maxes = {"red":12,
         "green":13,
         "blue":14}

regex = r"Game (\d+): (\d+) (\d+)"
res = 0
res2 = 0
for line in inp:
    currentmaxes = {"red":0,
                    "green":0,
                    "blue":0}
    possible = 1
    gamenum = re.findall(r"Game (\d+)",line)[0]
    sets = line.strip("\n").split(":")[1].split(";")
    print(line)
    for draw in sets:
        nums = re.findall(r"(\d+) (red|blue|green)",draw)
        for group in nums:
            currentmaxes[group[1]] = max(currentmaxes[group[1]],int(group[0]))
            if maxes[group[1]] < int(group[0]):
                possible = 0
    print("currentmaxes",currentmaxes)
    prod = currentmaxes["blue"]*currentmaxes["green"]*currentmaxes["red"]
    print(prod)
    res2+= prod
    if possible:
        res+= int(gamenum)
    
print("part1:",res)
print("part2:",res2)