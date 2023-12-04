import regex as re

with open("input.txt","r") as f:
    inp = f.readlines()

regex = r"\d"

def convert(strnum):
    try:
        return int(strnum)
    except ValueError as e:
        print(e)
        maps = {"zero":0,
                "one":1,
                "two":2,
                "three":3,
                "four":4,
                "five":5,
                "six":6,
                "seven":7,
                "eight":8,
                "nine":9}
        return maps[strnum]

regex2 = r"(\d|zero|one|two|three|four|five|six|seven|eight|nine)"
res = 0
res2 = 0
for line in inp:
    line = line.strip("\n")
    matches = re.findall(regex,line)
    res += int(matches[0])*10+int(matches[-1])

    ## part 2

    firstdigit = re.findall(regex2,line)[0]
    matches = []
    it = 1
    while not matches:
        sector = line[-it:]
        matches = re.findall(regex2,sector)
        it+=1
    print(line)
    res2+=convert(firstdigit)*10+convert(matches[0])
    
print(res)
print(res2)