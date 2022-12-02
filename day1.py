text = open("day1-data.txt").read()
elves = text.split("\n\n")
cals = []
for elf in elves:
    items = [int(i) for i in elf.split("\n")]
    print(items)
    cal_sum = sum(items)
    print(cal_sum)
    cals.append(cal_sum)

print(sum(sorted(cals)[-3:]))
