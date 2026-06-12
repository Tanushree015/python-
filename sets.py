# sets

'''a={1,2,3}
b={2,3,4}
u=a | b
print(u)

u =a&b
print(u)

u=a-b
print(u)

s= list([1,2,3,4])
print(s)


s1={1,2,3,4}
s2={3,4,5,6}
print(s1 | s2   )'''


'''items=("laptop","mouse","keyboard   ")
print(items[0])
print(items[-1])
print(len(items))
print("mouse" in items)'''

'''fruits = {"Apple", "Banana", "Mango", "Orange"}

print(len(fruits)   )

print("Mango" in fruits)
fruits.add("grapes")
print(fruits)'''

'''roll_numbers = {101, 102, 103, 104}

print(103 in roll_numbers   )
roll_numbers.remove(102)
print(roll_numbers)
print(len(roll_numbers)   ) '''


'''movies=("bahubali","rrr","kgf","pushpa")
print(movies[2:4])
print("kgf" in movies)
print(len(movies))'''



'''products=("laptop","mouse","keyboard","mouse")
print(products)
print(len(products))
print(set(products) )
print(products)

print(len(set(products)))'''

# dictionaries

'''student={
    "name":"Tanushree",
    "age":22,
    "course":"mca"
}
print(student)
print(student["name"])
print(student["age"])
student["city"]="bangalore"
print(student)
print(student.keys())
print(student.values())
print(student.items()   )


menu={
    "pizza":250,
    "burger":150,
    "pasta":200

}
print(menu)
print(menu["pizza"])
print(menu["burger"])
menu["sandwich"]=150
print(menu)
menu["pasta"]=250
print(menu)
print(menu.items())'''


'''account={
    "name":"tanushree",
    "balance":1000,
    "account_type":"savings"

}

print(account)
print(account["name"])
print(account["balance"]    )
account["city"]="hubballi"
print(account)
account['balance']=70000
print(account)
print(account.keys())
print(account.values())
print(account.items())
print(len(account))'''

# mixed 

'''name = "Tanushree"

subjects = ["Python", "Java", "DBMS"]

marks = (85, 90, 88)

skills = {"Communication", "Python", "Java"}

profile = {
    "age": 22,
    "city": "Hubballi"
}

print("Name:", name)
print(subjects[0])

print(max(marks))
print(len(skills))  
print(profile["city"])'''




items = ["Laptop", "Mouse", "Keyboard"]

prices = (50000, 1000, 1500)

brands = {"Dell", "HP", "Lenovo"}

customer = {
    "name": "Rahul",
    "city": "Bangalore"
}

print(items[-1])
print(max(prices))
print(len(brands))

print(customer["name"])
customer["membership"]="gold"
print(customer)
