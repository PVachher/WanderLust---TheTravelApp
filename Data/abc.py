a = open('wow.txt','r')
z = []
data = a.readlines()
for k in data:
    z.append(k.split(',')[-1]+', IN')
print z