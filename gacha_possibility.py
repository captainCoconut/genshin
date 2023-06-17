#!/usr/bin/python3

""" gacha possibility """

# 最多计算出多少个金的概率
max_gold = 7
max_gacha = max_gold * 90 + 20  # 防溢出

# 单抽概率
def poss(x):
    if x <= 0:
        return 0.0
    if x <= 73:
        return 0.006
    if x >= 90:
        return 1.0
    return 0.006 + 0.06 * (x - 73)

simple_poss = [0.0]
left_poss = 1.0
for i in range(1, 91):
    current_poss = left_poss * poss(i)
    left_poss = left_poss - current_poss
    simple_poss.append(current_poss)
# print(simple_poss)    

# m个金恰好在n抽出的概率是total_poss[m][n]
total_poss = [[0 for _a in range(max_gacha)] for _b in range(7)]

total_poss[0] = list([simple_poss[i] if i <= 90 else 0 for i in range(max_gacha)])

for gold in range(1, max_gold):
    for total_gacha in range(max_gacha):
        total_poss[gold][total_gacha] = sum([total_poss[gold - 1][total_gacha - i] * simple_poss[i] if total_gacha - i > 0 else 0.0 for i in range(90)])

for i in range(0, max_gacha, 20):
    print(i)
    print([sum(total_poss[max_gold - 1][:i + j]) for j in range(20)])

# 校验
print(sum(total_poss[max_gold - 1]))  # 概率和为1
print(sum([total_poss[max_gold - 1][i] * i for i in range(max_gacha)]))  # 期望抽数大概是62.5 * 金数
