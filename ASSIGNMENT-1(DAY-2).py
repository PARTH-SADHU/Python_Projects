# DATA TYPES AND THEIR DEFAULT FUNCTIONS

# LISTS:
lst=['parth','sadhu',10,1.00,123.343,['champ',10,'blue']]
print(lst)
print(type(lst))
# 1
a=lst.append('pdgdxfc')
# 2
q=lst.insert(1,5)
print(lst)
# 3
b=lst.remove('sadhu')
print(lst)
# 4
c=lst.reverse()
print(lst)
# 5
p=lst.clear()
print(lst)



# DICT:
dict={"name":"parth","rollno":102,"age":20,"address":"vadodara","lang":"GUJARATI"}
print(dict)
# 1
print(dict.get("name"))
print(dict.get("age"))
# 2
print(dict.items())
# 3
print(dict.keys())
# 4
print(dict.values())
# 5
x=dict.clear()
print(x)


# SETS:

sets={"parth","sadhu","god",11,2,5,11,33,545,232,344,44,4,4444,4444}
print(sets)
# 1
sets1={"sadhu",11,76,34,676,3221,5,76,32,"everywhere","earth","laptop"}
a=sets.union(sets1)
print(a)
# 2
b=sets.difference(sets1)
print(b)
# 3
c=sets.pop()
print(c)
# 4
d=sets1.add(5252552)
print(sets1)
# 5
e=sets.remove("sadhu")
print(sets)

# TUPLES:

credit_card1=(2187552985,'ryan',12-3-2000,300)
credit_card2=(2187513335,'bond',12-3-2000,300)


credit_card=[credit_card1,credit_card2]
print(credit_card)

x=credit_card1.count('ryan')
print(x)
y=credit_card1.index(2187552985)
print(y)


# STRINGS:
mystr="YOUR MINDSET MATTERS THE MOST INN ANY SITUATION"
print(mystr)
# 1
print(len(mystr))
# 2
j=mystr.index("M")
print(j)
# 3
o=mystr.upper()
print(mystr)
# 4
r=mystr.islower()
print(r)
# 5
print(mystr[5:10])
print(mystr[4])
"""the index written in the [] directly prints the char of that place"""
print(mystr[0:2])
"""here o is  included and index 2 is excluded """
print(mystr[0:4:2])
#it will skip one number entered after the 3rd semicolon
print(mystr[::])
#if the bracket is empty then it will take  default value
print(mystr[-2:-6])
#it will work the same nut will start from ending or will start fromm last char
print(mystr[::-2])
#first it will reverse the whole string and then work same start skipping the chars


