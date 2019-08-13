##import re
##f = open('rosalind_gc_py.txt', 'r')
##
##f2 = f.readlines() #read and store all lines in a list
##f2 = ''.join(f2) #convert list into a string
##names = re.findall('>R+[a-z]+_+[0-9]+', f2) #find and store all fasta id:s in a separate list
##f2 = re.sub(r'>R+[a-z]+_+[0-9]+\n', ',', f2) #remove/replace all fasta id:s from list w DNA strings
##f2 = f2.replace('\n','') #remove all EOL symbols
##f2 = f2.split(',') #split the string at ',' and store strings in a list
##f2.remove('') #remove the 1st empty string
##
##GC = [] #list with proportion of GC in each string
##for i in range(len(f2)):
##    GC.append( (f2[i].count('G')+f2[i].count('C'))/len(f2[i]) )
##
##print(names[GC.index(max(GC))])
##print(round(max(GC)*100, 7) )
##f.close()


f = open('rosalind_gc_py.txt', 'r')

max_gc_name, max_gc_content = '', 0

buf = f.readline().rstrip()
while buf:
    seq_name, seq = buf[1:], ''
    buf = f.readline().rstrip()
    while not buf.startswith('>') and buf:
        seq = seq + buf
        buf = f.readline().rstrip()
    seq_gc_content = (seq.count('C') + seq.count('G'))/float(len(seq))
    if seq_gc_content > max_gc_content:
        max_gc_name, max_gc_content = seq_name, seq_gc_content

print('%s\n%.6f%%' % (max_gc_name, max_gc_content * 100))
f.close()
