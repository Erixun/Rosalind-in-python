f = open('rosalind_hamm.txt', 'r')

s = f.readline().rstrip()
t = f.readline()

hamm = int()
for i in range(len(s)):
    if s[i] != t[i]:
        hamm += 1

print(hamm)

#zip returns a list of tuples, from elements in s and t respectively
print(sum(a != b for a, b in zip(s, t))) #
