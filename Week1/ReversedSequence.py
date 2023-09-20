# FOR LOOP
ori_sequence = [1, 2, 4, 3, 5]
rev_sequence = []

for item in reversed(ori_sequence):
    rev_sequence.append(item)

print(rev_sequence)

# WHILE LOOP
orig_sequence = [1, 2, 4, 3, 5]
reve_sequence = []

index = len(orig_sequence) - 1
while index >= 0:
    reve_sequence.append(orig_sequence[index])
    index -= 1

print(reve_sequence)
