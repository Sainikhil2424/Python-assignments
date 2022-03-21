print("sss")

#Dictionary
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car["brand"])
#Dictionary Methods
#clear()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.clear()
print(car)
#copy()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.copy()
print(x)

#fromkeys()
x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)

print(thisdict)
x = ('key1', 'key2', 'key3')

thisdict = dict.fromkeys(x)

print(thisdict)
#get()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("model")

print(x)

#items()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": [1964,5561,8466,7886]
}

x = car.items()
print(x)
#keys()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.keys()
print(x)
#pop()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.pop("model")

print(car)
#popitem()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.popitem()
print(car)

#setdefault()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.setdefault("model", "Bronco")
print(x)
#if key not found insert
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("color", "White")

print(x)

#update()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.update({"Model": "White"})
print(car)

# values()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.values()

print(x)
#Iterating dictionaries
for keys in car:
    print(keys)
for keys in car:
    print(keys,"--> ",car[keys])

items=car.items()
print(items)

print(car.keys())
print(car.values())
#sorting
# Creates a sorted dictionary (sorted by key)
from collections import OrderedDict
 
dict = {'ravi':'10','rajnish':'9','sanjeev':'15','yash':'2','suraj':'32'}
dict1 = OrderedDict(sorted(dict.items()))
print(dict1)

##List
# list of integers
my_list = [1, 2, 3]
# empty list
my_list = []
# list with mixed data types
my_list = [1, "Hello", 3.4]
#Access List Elements
my_list = ['p', 'r', 'o', 'b', 'e']
# first item
print(my_list[0]) 
# third item
print(my_list[2])

# Iterate over a list
list = [1, 3, 5, 7, 9]
  # Using for loop
for i in list:
    print(i)

#Iterate over a list
list = [1, 3, 5, 7, 9]
# getting length of list
length = len(list)
# Iterating the index
# same as 'for i in range(len(list))'
for i in range(length):
	print(list[i])



# List slicing in Python

my_list = ['p','r','o','g','r','a','m','i','z']

# elements from index 2 to index 4
print(my_list[2:5])

# elements from index 5 to end
print(my_list[5:])

# elements beginning to end
print(my_list[:])


# Appending and Extending lists in Python
odd = [1, 3, 5]

odd.append(7)

print(odd)

odd.extend([9, 11, 13])

print(odd)

# Deleting list items
my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']

# delete one item
del my_list[2]

print(my_list)

# delete multiple items
del my_list[1:5]

print(my_list)

# delete the entire list
del my_list

# Error: List not defined
print(my_list)  
print(my_list.pop(1))
# nested list
my_list = ["mouse", [8, 4, 6], ['a']]
# Nested List
n_list = ["Happy", [2, 0, 1, 5]]

# Nested indexing
print(n_list[0][1])

print(n_list[1][3])

# Error! Only integer can be used for indexing
print(my_list[4.0])


#Tuple
tuple1=("good",1,2,3,"morning")
print(tuple1)
print(tuple1[0])  # accessing values using indexing
#tuple1[1]="change"  # a value cannot be changed as they are immutable
tuple2=("orange","grapes")
print(tuple1+tuple2)  # tuples can be concatenated
tuple3=(1,2,3)
print(type(tuple3))

#Delete Tuple Elements
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')

# Following action is not valid for tuples
# tup1[0] = 100;

# So let's create a new tuple as follows
tup3 = tup1 + tup2
print (tup3)
#Delete Tuple Elements
tup = ('physics', 'chemistry', 1997, 2000)
print (tup)
del tup
print ("After deleting tup : ")
print (tup)

myset = {"apple", "banana", "cherry"}
myset.pop()
myset.pop()



k='kalyan'
setk=set(k)
setk.pop()
print(setk)


##listpractice
lists=[1,2,3,4,5,6,7,8,9]
print(lists)

lists2=[10,11,12,13,14,15,16,17,18,19]
lists.extend(lists2)
print(lists)
lists.insert(2,0)
print(lists)
del lists[2]
lists.pop(2)
lists.pop()
print(lists)
print(lists[18])
for i in range(0,19):
  print(type(lists[i]))


lists.append("sainikhil")
print(type(lists[0]))
lists.remove(0)
print(lists)
lists2.clear()
print(lists2)

lists=map(str,lists)
for i in lists:
  print(i)
lists.sort(reverse=True)
  print(lists)