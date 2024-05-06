#Lists: ordered, mutable, allows duplicate elements
mylist = ["banana", "cherry", "apple"]
""" #print(mylist) """

# we can create a empty list using list function later we can append items later
mylist2 = list()
""" #print(mylist2) """

# list can contain diff datatypes and allows duplicates. 
# we can access the element by using index. R->L(start with 0), L->R(starts with -1)
mylist3 = [ "apple", "guava", "grapes", "banana"]
""" #print(mylist3[-2]) """

# iterate all elements using for loop
""" for e in mylist3:
    print(e) """

#check if elemnt inside the list
""" if "apple" in mylist3:
    print("yes")
else:  
    print("no") """

                     
###########  Methods ##############

#check how many elements inside the list : len()
""" print(len(mylist3)) """

#to append item : append() - insertion at the end of the list
mylist3.append("guava")
""" print(mylist3) """

# inset element at a specific position : insert() - first index number comma separated value
mylist3.insert(1, "mango")
""" print(mylist3) """

# remove element from last : pop()
item = mylist3.pop()
""" print(item)
print(mylist3)
 """

# reverese the list : reverse() 
item = mylist3.reverse()
""" print(mylist3) """

# sort the list : sort() : ascending order
# not supported between instances of 'str' and 'int' and 'boolean'
item = mylist3.sort()
""" print(mylist3) """

# if dont don't to sort original list instead create a new list
new_list = sorted(mylist3)
""" print(new_list) """

# remove a specific element : remove()
item1 = mylist3.remove("mango")
""" print(mylist3) """

# remove all the element : clear()
mylist3.clear()
""" print(mylist3) """

###################### Tricks ###############################
# create a new list with the same elements
alist = [0] * 5
""" print(alist) """

# concate two lists using (+) operator
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new = alist + list1
""" print(new) """

# slice a list : will ommit given index numbers and ofcourse outside the given index : output [2, 3, 4, 5]
# if we dont specify the start index [: 5] will go from 0 to 5
# if we dont specify the last index [1 : ] will go till the end
a = list1[1:5]
""" print(a) """

# slice a list with step index
a = list1[::1] # will go all the step from beginning from 1
a1 = list1[::2] # it will take every second item : output [1, 3, 5, 7, 9]
a2 = list1[:: -1] # reverse the index : outout [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(a2)

# copy a list from existing list : will get a copy but in case if we change the copy it will also change the original so after the assignment both lists refers to the same list inside the memmory.
mylist4 = [ "apple", "guava", "grapes", "banana"]
new_list = mylist4
""" print(new_list) """
new_list.append("lemon")
""" print(new_list) """
""" print(mylist4) """
# Three ways to copy a list which will not overwrite the original list
new_list = mylist4.copy() # using copy method
new_list = list(mylist4) # using list method
new_list = mylist4[:]  # using slicing
""" print(new_list) """

# square the elements of a list
list1 = [1, 2, 3, 4, 5]
list2 = [i*i for i in list1]
""" print(list1) """
""" print(list2) """