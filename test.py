n = 521

s = [int(i) for i in str(n)]
# print(s)
for i in range(1, len(s), 2):

    s[i] =- s[i]
    # print(s[i])
    # print(s)
print(s)
# print(sum(s))