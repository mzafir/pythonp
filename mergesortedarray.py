class asim:

    def __init__ (self, data):
        self.data =data
        self.next = None

    def getdata(self):
        return self.data

    def getNext (self):
        return self.next

    def setData (self, newdata):
        self.data=newdata
        



alice=[9,3,5,6,6,8,9]
bob=  [4,5,3,6,1,2,8]

set_alice=set(alice)
set_bob=set(bob)

result=[]
for i in range(len(alice)):
    temp=alice[i]
    for j in range(len(bob)):
        if temp > bob[j]:
            temp=bob[j]


    result.append(temp)
      #  result.append(max)
       # set1=set(result)

print(result)
