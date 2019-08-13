s = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"

b = ['A','C','G','T']
count = []
for n in b:
    count.append(s.count(n))

print(*count)
