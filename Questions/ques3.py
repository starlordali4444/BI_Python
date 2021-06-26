# 1 
# 2 3 
# 3 4 5 
# 4 5 6 7 
# 5 6 7 8 9 
# 6 7 8 9 10 11

for i in range(0,7):
    for j in range(i,i+i):
        print(j,end=' ')
    print('\n')