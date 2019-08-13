import numpy as np
f = open('rosalind_rear.txt', 'r')

f2 = f.readlines()

length = len(f2)

lists = []
for l in range(length):
    if f2[l] != '\n':
        lists.append(list(map(int, f2[l].strip().split(' '))))

lists2 = np.array(lists)

length = len(lists2)
totc = []
for j in range(0,length-1, 2):
    beg = 0; end = length-1
    counter = int()
    print(j+1)
    while beg < end:
        if (np.where(lists2[j+1][beg] == lists2[j])[0][0])-beg == end-(np.where(lists2[j+1][end] == lists2[j])[0][0]) and beg != np.where(lists2[j+1][beg] == lists2[j])[0][0] and end != np.where(lists2[j+1][end] == lists2[j])[0][0]:
            k = np.where(lists2[j+1][beg] == lists2[j])[0][0]
            lists2[j][beg:k+1] = lists2[j][beg:k+1][::-1]
            #k = np.where(lists2[j+1][end] == lists2[j])[0][0]
            #lists2[j][k:end+1] = lists2[j][k:end+1][::-1]
            counter += 1
            beg += 1
            #end -= 1
            print(lists2[j], lists2[j+1], '==')
        elif (np.where(lists2[j+1][beg] == lists2[j])[0][0])-beg > end-(np.where(lists2[j+1][end] == lists2[j])[0][0]) and beg != np.where(lists2[j+1][beg] == lists2[j])[0][0] and end != np.where(lists2[j+1][end] == lists2[j])[0][0]:
            k = np.where(lists2[j+1][beg] == lists2[j])[0][0]
            lists2[j][beg:k+1] = lists2[j][beg:k+1][::-1]
            beg += 1
            counter += 1
            print(lists2[j], lists2[j+1], '>')
        elif (np.where(lists2[j+1][beg] == lists2[j])[0][0])-beg < end-(np.where(lists2[j+1][end] == lists2[j])[0][0]) and beg != np.where(lists2[j+1][beg] == lists2[j])[0][0] and end != np.where(lists2[j+1][end] == lists2[j])[0][0]:
            k = np.where(lists2[j+1][end] == lists2[j])[0][0]
            lists2[j][k:end+1] = lists2[j][k:end+1][::-1]
            end -= 1
            counter += 1
            print(lists2[j], lists2[j+1], '<')
        elif beg == np.where(lists2[j+1][beg] == lists2[j])[0][0]:
            beg += 1
        elif end == np.where(lists2[j+1][end] == lists2[j])[0][0]:
            end -= 1
        
    totc.append(counter)
