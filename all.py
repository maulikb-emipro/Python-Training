import datetime

"""    Lists    """

list1 = [1, 2, 3, 4, 5 ]
list2 = ["a", "b", "c", "d"]

"""    List indexing and Slicing    """
print(list1[3])
print(list2[2:3])
print(list2[1:])
print(list1[-5])

"""    List assignments    """
list1[2]=5
print(list1)

"""    List Operations    """
print(len(list1))
print(list1+[6,7,8])
print(list2*3)
print(4 in list1)
for x in list2: 
    print(x,end=' ')

"""    Built-in Functions and List methods    """
print(max(list1))
print(min(list2))
print(list((1,2,3)))

list2.append('e')
list1.extend([9,11])
list2.insert(3, 'l')
list1.remove(2)
list1.reverse()
list2.sort()
print(list1.count(5))
print(list1.index(5))
print(list1.pop(5))
print(list1)
print(list2)

i=100
a = 1 if i<100 else 2 if i>100 else 0 if i==100 else 3
print(a)

"""    Sets    """
set1={1,2,3}
set2={1,2,3,4,3,2}

"""    Operations    """
set1.add(4)
set2.update([6,5,7])
set1.update([4,5],{6,7,8,9})
set1.discard(8)
set2.remove(4)
set1.pop()
print(set1)
print(set2)

print(set1|set2)
print(set1&set2)
print(set1-set2)
print(set2-set1)
print(set1^set2)
print(8 in set1)

"""    Dictionary    """
dict1 = {'Name': 'You', 'Age': 7, 'Class': 'M1'}

dict2=dict1.copy()
dict3=dict2.fromkeys(['First','Second','Third'],10)
del dict1['Age']
dict2.update(dict3)
print(dict1)
print(dict2)
print(dict3)

print(dict1['Class'])
print(dict2.get('Name'))
print('Age' in dict2)
print(dict1.keys())
print(dict2.values())
print(dict3.items())

"""    Datetime    """

date_now=datetime.datetime(1996,12,27,19,5,33,7)
print(date_now)
print(datetime.date.today())
print(datetime.date.weekday(date_now))

"""    Dates    """

print("Year :",date_now.strftime("%Y"))
print("Month No :",date_now.strftime("%m"))
print("Date :",date_now.strftime("%d"))
print("Short Year :",date_now.strftime("%y"))
print("Short Month :",date_now.strftime("%b"))
print("Full Month :",date_now.strftime("%B"))
print("Weekday starting 1-Monday :",date_now.strftime("%w"))
print("Weekday Name :",date_now.strftime("%A"))
print("Week No :",date_now.strftime("%W"))

"""    Time    """

print("Hours :",date_now.strftime("%H"))
print("Minutes :",date_now.strftime("%M"))
print("Seconds :",date_now.strftime("%S"))
print("Hours :",date_now.strftime("%c"))
