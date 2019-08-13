s = list("AAAACCCGGT")
d = {"A":"T","T":"A","C":"G","G":"C"}

for i in range(len(s)):
    s[i] = d[s[i]]

s = s[::-1]

print(*s, sep='')
