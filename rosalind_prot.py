f1 = open('rosalind_prot-2.txt', 'r')
code = f1.readline().rstrip()
f1.close()
f2 = open('RNAcodonTable.txt', 'r')
rnaC = f2.read().rstrip().split()
f2.close()

rna_dict = dict(zip(rnaC[0::2], rnaC[1::2]))
protein = ""
for i in range(0, len(code)-3, 3):
    protein += rna_dict[code[i:i+3]]

print(protein)

f3 = open('output.txt', 'w')
f3.write(protein)
f3.close()
