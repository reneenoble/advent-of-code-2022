OP_R = "A"
OP_P = "B"
OP_S = "C"

ME_R = "X"
ME_P = "Y"
ME_S = "Z"

shape_scores = {"X": 1, "Y": 2, "Z": 3}
comp_scores = {"T": 3, "W": 6, "L": 0}

outcome_map = {"T": "Y", "W": "Z", "L": "X"}


# result = {(OP_R, ME_R): "T", (OP_R, ME_P): "W", (OP_R, ME_S): "L", (OP_P, ME_R): "L", (OP_P, ME_P): "T", (OP_P, ME_S):  "W", (OP_S, ME_R): "W", (OP_S, ME_P): "L", (OP_S, ME_S): "T"}
result = {(OP_R, ME_R): "T", (OP_R, ME_P): "W", (OP_R, ME_S): "L", (OP_P, ME_R): "L", (OP_P, ME_P): "T", (OP_P, ME_S):  "W", (OP_S, ME_R): "W", (OP_S, ME_P): "L", (OP_S, ME_S): "T"}
move_lookup = {}
for k, v in result.items():
    op, me = k
    move_lookup[(op, outcome_map[v])]= me

sum_score = 0

with open("day2-data.txt") as f:
    score = 0
    for line in f:
        line = line.strip().split()
        op, result_needed = line
        me = move_lookup[(op, result_needed)]

        shape_score = shape_scores[me]
        comp_score = comp_scores[result[(op, me)]]
        sum_score += shape_score + comp_score
        
print(sum_score)