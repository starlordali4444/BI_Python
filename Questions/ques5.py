# Combine the given lists a & b, get the count of elements. Eg. ‘hello’ Occurs 3 times, ‘barbie’ occurs 2 times etc.,
# a=['hello','world','barbie','hello']
# b=['hello','barbie','hai']

a=['hello','world','barbie','hello']
b=['hello','barbie','hai']

c=a+b
print(c)
set_c=set(c)
print(set_c)
d_count={}
for n in set_c:
    d_count[n]=c.count(n)
print(d_count)