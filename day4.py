total = 0

with open("day4-data.txt") as f:
        for line in f:
            parts = line.split(",")
            part_ranges = [tuple([int(i) for i in part.split("-")]) for part in parts]
            # print(part_ranges)

            
            # sorted_ranges = sorted(part_ranges, key=lambda x: (x[0], -x[1]))
            # if sorted_ranges[1][1] <= sorted_ranges[0][1]:
            #     total += 1
            
            sorted_ranges = sorted(part_ranges, key=lambda x: (x[0], -x[1]))
            if sorted_ranges[1][0] <= sorted_ranges[0][1]:
                total += 1
            else:
                print(sorted_ranges)

print(total)