"""
Dictionary: 
Store Data Value in 'KEY : VALUE' pair.
They are Unordern, Mutable (Changable), and don't allow Duplicate Key.
"""

"Store All Data Type In Dict Value, but not set List and Dictionary as KEY"

#Simple Dict
d = {
    'Name' : 'Jhon',
    'Age' : 23,
    'Skills' : ['Python', 'Java', 'JS'],
    'isActive_on_Github' : True,
    5 : 5
}

print(d) #print Dict

print(type(d)) #Print Data Type 

#Acces data/value with Key:
print(f"Student Name: {d['Name']}")
print(f"Student Age: {d['Age']}")
print(f"Student Skills: {d['Skills']}")

# If Not Exist key there is Error Show:
# print(d['data']) #key not set in d. Give KeyError

"""Direct Chane Values and add New Key:value"""
# Change Value jhon to Rohan 
d['Name'] = 'Rohan' #Overwrite Not create a New Dict change/Replace in same Dict

d['isActive_on_Github'] = False #Change True to false
print(d)

d['Surname'] = 'Jakson' #Add New Value with Assignment Operator (=) 'Surname'
print(d)

'We can Cretae a Empty Dict'
null_d = {}
print(null_d)
print(type(null_d))



"""We can create a Nested Dict in Dict"""
student = {
    'name' : 'Jadeja',
    'subject' : { #nested Dict
        'science' : 90,
        'math' : 95,
    }
}
print(student) # Print Full Dict
print(student['subject']) # Print Nested Dict "Subject"
print(student['subject']['math']) # Print Nested Dict specific Subject 

"""
Dictionary Methods:
myDict.keys()  = give all 'Keys' of Dict
myDict.values() = give all 'Values' of Dict
myDict.items() = give all Key-Value pair as "TUPLE"
myDict.get() = give specific "key" value 
myDict.update() = can add new key-value or update currect key-value  
"""
#.keys()
print(d.keys()) #Return dict_keys("All Keys")
print(student.keys()) #get all keys but not Nested Key Included only Main Dict Keys

print(list(d.keys())) #print Simple List formate all keys
print(len(list(student.keys()))) #print length of keys (TOTAL KEYS in Dict)

#.values()
print(d.values()) #Return dict_values("All values")
print(student.values()) # Return all Values Include Nested Dict Also

print(list(d.values())) #print Simple List formate all values

#.items()
print(d.items()) #give dict_items([('key', 'value'), ('key', 'value')])
print(student.items()) #give dict_items([('key', 'value'), ('key', 'value')])
item = list(student.items())
print(item[1]) #Access Speific Key Value Pair 

# .get()
print(d['Name']) 
print(d.get('Name'))

"Note: Both give same value but main Diff.. is if there is key we Called/Access that not Exist in Dict without '.get()' not give Error Give 'None' "
# print(d['midname']) #Give Error 
print(d.get('midname')) #give None

#.update()
d.update({'city' : 'surat'}) #add New Key-value City
print(d)

new_dict = {
    'Data' : [20,10],
    'skills' : "py"
    }

student.update(new_dict) #Add Full New_dict in old Dict
print(student)

d.update({'Name' : "Kali"}) #Udate Old key = New with new value/ overwrite
print(d)