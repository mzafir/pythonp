list_num=[1,2,7,4,5,4,1,8,3,3,4,1,9,6,2,1,0,3]
dicts={}
for i in list_num:
    temp=list_num[i-1]
    print(temp, "temp val")
    count=0
    for j in list_num:
        print(j, "j value")
        print(list_num[j-1], "list val at j")
        if temp==list_num[j]:
            count+=1;
            print(f"temp is {temp} and first element of array is {list_num[j]} is same")
    dicts.update({temp: count})
for key,value in dicts.items():
    print(key, value)
    

print(len(list_num))