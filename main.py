list1 = ["c","b","a"]
list2 = ["d","f","e"]
list1.sort()
list2.sort()
list3 = list1.copy()
list1.append("x")
list1.remove("c")
list1.pop(0)
print(list1)