import time
start = time.time()
with open('rosalind_subs.txt') as f:
    s,t = f.read().strip().split('\n')

string = ""
for i in range(len(s)):
    if s[i:len(t)+i] == t:
        string += str(i+1)+" "

print(string)
print("Runtime %s seconds" % (round(time.time() - start, 8) ) )
