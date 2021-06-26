l = [7,3,8,2,5,9,12,78]
even=[]
odd=[]

for n in l:
    if n%2==0:
        even.append(n)
    else:
        odd.append(n)

print(odd)
print(even)
