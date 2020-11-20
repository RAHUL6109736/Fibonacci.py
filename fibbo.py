num=int(input('upto to what number fibbo? :'))
fibbo=[0,1]
f=1
i=0
a=0
while(i<=num):
    f=f+a
    a=f-a
    fibbo.append(f)
    i=f+a
print('fibbo number are: ',fibbo)
