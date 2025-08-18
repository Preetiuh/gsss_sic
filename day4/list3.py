list1 = [1 , 2 , 3 , 4]
list2 = [5 , 6 , 7]

print(list1.extend(list2)) # [1 , 2 , 3 , 4 , 5 , 6 , 7]
print(list1)
list1.append(list2) # [1 , 2 , 3 , 4 , [5 , 6 ,7] ]
print(list1)