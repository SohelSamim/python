l1=[1,14,26,37,100,86,77]
l2=[2,13,27,38,99,85,78]
 
new_list=[]
 
for i in range(len(l1)):
    if l1[i] <= l2[i]:
        new_list.append(l1[i])
        new_list.append(l2[i])
    else:
        new_list.append(l2[i])
        new_list.append(l1[i])
            
print(new_list)
