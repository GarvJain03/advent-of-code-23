def calibration():
    with open("data.txt", "r") as F:
        L = []
        lines = F.readlines()
        for i in range(0, len(lines)):
            num = list(map(str, filter(str.isdigit, lines[i])))
            L.append(int(num[0]+num[-1]))
        print(sum(L))
 

calibration()