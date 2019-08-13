
from Bio import SeqIO                                                 
from Bio.Seq import Seq                                               
from Bio.Alphabet import generic_dna                                  
reads = []                                                            
handle = open('sampledata.fasta', 'r')                                
for record in SeqIO.parse(handle, 'fasta'):                           
    reads.append(str(record.seq))                                     
handle.close()                                                        

right = []                                                            
wrong = []                                                            
for i, j in enumerate(reads):                                         
    read = Seq(j, generic_dna)                                        
    rev_read = read.reverse_complement()                              
    for k in range(i + 1, len(reads)):                                
        if read == reads[k] or rev_read == reads[k]:                  
            if read not in right and rev_read not in right:           
                right.append(str(read))                               
                right.append(str(rev_read))                           

for l in reads:                                                       
    if l not in right:                                                
        wrong.append(l)                                               

for incorrect in wrong:                                               
    for correct in right:                                             
        hamming = 0                                                   
        for nt1, nt2 in zip(incorrect, correct):                      
            if nt1 != nt2:                                            
                hamming += 1                                          
                if hamming > 2:                                       
                    break                                             
        if hamming == 1:                                              
            with open('answer.txt', 'a') as textfile:                 
                print(incorrect, '->', correct, sep='', file=textfile)
