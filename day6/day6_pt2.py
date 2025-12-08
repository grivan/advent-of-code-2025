import operator
op_map = { "+": operator.add, "*": operator.mul }

INPUT = open("day6.in")

lines = INPUT.readlines()

lines = [line.strip('\r') for line in lines]

nums = [line for line in lines[:-1]]
ops = [line for line in lines[-1]]

n_ops = []
count = 0
for op in ops:
    if op in ['*', '+']:
        start = count
        n_ops.append((op, start, 0))
    else:
        l = n_ops.pop()
        l = (l[0], start, count)
        n_ops.append(l)
    count += 1

# take care of the end
l = n_ops.pop()
l = (l[0], start, l[2]+1)
n_ops.append(l)
    
# print(n_ops)

new_nums = []
for ops in n_ops:
    op = op_map[ops[0]]
    start, end = ops[1], ops[2]
    new_num = ''
    for i in range(start, end):
        new_num+=' '
        for num in nums:
            # print(ops[0], num[start:end])
            new_num += num[i]
    
    new_nums.append([int(n) for n in new_num.split()])

# print(new_nums)

tot = 0
for i in range(len(new_nums)):
    op = op_map[n_ops[i][0]]
    # print(new_nums[i], n_ops[i][0])
    rem = 1 if n_ops[i][0] == '*' else 0
    for j in range(len(new_nums[i])):
        rem = op(rem, new_nums[i][j])
    tot += rem

print(tot)