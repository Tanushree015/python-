# items=["apple","banana","grapes"]
# print(items[1])

'''l=[1,"bru",True,0.8]
# print(l[-1])

l.pop(0)
print(l)

l.append("buscuit")
print(l)

list=["tanu",34,"daadu",0,8]
print(list)
list.pop()
print(list)

list.append("shas")
print(list)'''

#adding element to the list 

'''a=[1,2,3,4]
a.append(5)
print(a)

a=[1,2,3,4]
a.insert(2,5)
print(a)

a=[1,2,3,4]
a.extend([5,6])
print(a)'''

#updating an element 

# a=[1,2,3,4]
# a[1]=25
# print(a)


# removing an element  

'''a=[1,2,3,4]
a.remove(2)
print(a)

a=[1,2,3,4]
a.pop()
print(a)

a=[1,2,3,4]
del a[3]
print(a)

a=[1,2,3,4]
a.clear()
print(a)'''

#iterating over list
'''a=['apple','banana','cherry']
for item in a:
    print(item)

a=[1,2,4.5,"banana",True]
for item in a:
    print(item)'''


# nested list 
'''a=[[1,2,3],[4,5,6],[7,8,9]]
print(a)    
print(a[0])  #first list
print(a[0][1])'''

'''name="tanushree"
print(name .upper())
print(len(name))
print(name[::-1])
print(name[-1])

print(name.replace("tanushree","tanu"))
print(name.strip("tanushree"))

print(name.lower()  )'''


'''list=["soap","shampoo","toothpaste"]
print(list)
list.append("facewash")
print(list)
list.insert(1,"lotion")
print(list)
list.extend(["cream","perfume"])
print(list)
list.remove("toothpaste")
print(list)
list.pop()
print(list)
del list[0]
print(list)
list.clear()
print(list)         


l=[1,2,3,4]
print(l[0 : : 2])
print(l[0:])'''


list=[13,11,12,17,20]
sorted_list=sorted(list, reverse=True)
print(sorted_list)