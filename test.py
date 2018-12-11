asim=[383838383]
print(asim[0:4])
mylist=['a','b','c']
mylist.append('d')
print(mylist)

mylis_2=[0,1,3,mylist]
print (mylis_2)

d={'alpha':mylist,'asim':40, 'maryam':2018-1989, 'hina':38, 'hiba':34, 'abbo':2018-1948, 'ammee':2018-1952}

print(d)


seta=set(d)
print(seta)

def asimsync(x):
    out = [num** 2 for num in x ]
    print(out)

asimsync([1,2,3,3,4,5,6,7,9])

def square(num):
    return num**2


ouput1 = square(2)

print(ouput1)


seq=[1,3,4,4,6,7,7,7,8]

list3333=list(map(lambda num:num/2, seq))

print(list3333)

seq1=[4,6,7,7,7,7,9,7,7,7,8,10,102]

q=list(filter(lambda num: num%2==0, seq))

print(q)

tweet="this is not me"
list1=tweet.split()
print (list1)



asim3=[(1,3),(4,4),(4,6)]

for (a,b) in asim3:
    print(a%2==0)