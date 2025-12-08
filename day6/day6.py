import operator
op_map = { "+": operator.add, "*": operator.mul }

INPUT = open("day6.in")

lines = INPUT.readlines()

lines = [line.strip() for line in lines]

nums = [[int(spl) for spl in line.split()] for line in lines[:-1]]
ops = [line for line in lines[-1].split() if line]

tot = 0
for i in range(len(nums[0])):
    op = op_map[ops[i]]
    rem = 1 if ops[i] == '*' else 0
    for j in range(len(nums)):
        # print(nums[j][i], rem, ops[i])
        rem = op(rem, nums[j][i])
    tot += rem

print(tot)