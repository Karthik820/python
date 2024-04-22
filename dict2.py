# Creating a Dictionary       
Dict1 = {1: 'EZTS', 2: 'In-plant Training', 3: 'College'}       
# Deleting a key        
# using pop() method       
pop_key = Dict1.pop(2)       
print(Dict1)

# for loop to print all the keys of a dictionary    
Employee = {"Name": "Balaji", "Age": 70, "salary":200000,"Company":"EZTS"}        
for x in Employee:        
    print(x)
    

#for loop to print all the values of the dictionary    
Employee = {"Name": "Balaji", "Age": 70, "salary":200000,"Company":"EZTS"}
for x in Employee:        
    print(Employee[x])

#for loop to print the values of the dictionary by using values() method.    
Employee = {"Name": "Balaji", "Age": 70, "salary":200000,"Company":"EZTS"}     
for x in Employee.values():        
    print(x)
print("--------------")
#for loop to print the items of the dictionary by using items() method    
Employee = {"Name": "Balaji", "Age": 70, "salary":200000,"Company":"EZTS"}
for x in Employee.items():        
    print(x)
print("--------------")    
dict = {1: "Chennai", 2: "Vijayawada", 3: "Ballari", 4: "Banglore"}  
print(len(dict))
print("--------------")

dict = {7: "Chennai", 5: "Vijayawada", 8: "Ballari", 1: "Banglore"}
print(sorted(dict))
print("--------------")
#{'Name': 'nandhu', 'Age': 25, 'salary': 50000, 'Company': 'Yahoo', 'x-lover': 'yes'} dictionary methods    
dict = {1: "Chennai", 2: "Vijayawada", 3: "Ballari", 4: "Banglore"}   
# clear() method    
dict.clear()    
print(dict)
print("--------------")
# dictionary methods    
dict = {1: "Chennai", 2: "Vijayawada", 3: "Ballari", 4: "Banglore"}    
# copy() method    
dict_demo = dict.copy()    
print(dict_demo)

# dictionary methods    
dict = {1: "Chennai", 2: "Vijayawada", 3: "Ballari", 4: "Banglore"}
# pop() method    
dict_demo = dict.copy()    
x = dict_demo.pop(1)    
print(x)
print(dict_demo)

# dictionary methods    
dict = {1: "Chennai", 2: "Vijayawada", 3: "Ballari", 4: "Banglore"}
# keys() method    
print(dict.keys())

# dictionary methods    
dict = {1: "Chennai", 2: "Vijayawada", 3: "Ballari", 4: "Banglore"}
# items() method    
print(dict.items())

# dictionary methods    
dict = {1: "Chennai", 2: "Vijayawada", 3: "Ballari", 4: "Banglore"}
# get() method    
print(dict_demo.get(3))

# dictionary methods    
dict = {1: "Chennai", 2: "Vijayawada", 3: "Ballari", 4: "Banglore"}
# values() method    
print(dict_demo.values())

# dictionary methods    
dict = {1: "Chennai", 2: "Vijayawada", 3: "Ballari", 4: "Banglore"}
# update() method    
#dict.update({(3,"TCS"),()})    
print(dict)

for i in dict.items():
    print(i)