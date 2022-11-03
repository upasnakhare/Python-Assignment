#!/usr/bin/env python
# coding: utf-8

# In[ ]:


1. What exactly is []?

[] is ampty list value which is a list value contains no items in the list. 


# In[2]:


2. In a list of values stored in a variable called spam, how would you assign the value 'hello' as the third value? (Assume [2, 4, 6, 8, 10] are in spam.)

spam = [2, 4, 6, 8, 10]
spam[2]= "hello"

spam[2] because as per problem statement we want "hello" as a third value and index of list value will be start from 0. 

Result after we assign "hello" as the third value to a list of values: 
    
[2, 4, 'hello', 8, 10]


# In[ ]:


Let's pretend the spam includes the list ['a', 'b', 'c', 'd'] for the next three queries.
3. What is the value of spam[int(int('3' * 2) / 11)]?

The value of spam[int(int('3' * 2) / 11)] will be 'd' because int('3' *2) will be eventually interger 33 as *2 means 
it is replicating the '3' twice then int(33/11) after division the result will be 3 and spam[3] is 'd' and below is the output.


# In[10]:


spam = ['a', 'b', 'c', 'd']
spam[int(int('3' * 2) / 11)]


# In[ ]:


4. What is the value of spam[-1]?

The value of spam[-1] will be 'd' as negative index starts from the end of the list. 
Below is the output:


# In[11]:


spam = ['a', 'b', 'c', 'd']
spam[-1]


# In[ ]:


5. What is the value of spam[:2]?

The value of spam[:2] will be ['a', 'b'] as the index will by default start from '0 till 1' (excluding the upperbound index '2')
Below is the output:


# In[12]:


spam = ['a', 'b', 'c', 'd']
spam[:2]


# In[ ]:


Let's pretend bacon has the list [3.14, 'cat', 11, 'cat', 'True'] for the next three questions.
6. What is the value of bacon.index('cat')?

The value of bacon.index('cat') will be 1 because list contains the value 'cat' twice at index 1 and 3 
but result will be the first index as shown below:


# In[18]:


bacon = [3.14, 'cat', 11, 'cat', True]
bacon.index('cat')


# In[ ]:


get_ipython().set_next_input('7. How does bacon.append(99) change the look of the list value in bacon');get_ipython().run_line_magic('pinfo', 'bacon')

bacon.append(99) will append 99 at the end of the list as below:


# In[20]:


bacon.append(99)
bacon


# In[ ]:


get_ipython().set_next_input("8. How does bacon.remove('cat') change the look of the list in bacon");get_ipython().run_line_magic('pinfo', 'bacon')

bacon.remove('cat') will remove the value 'cat' which is at the index 1 only it will not remove the other one which is at index 3


# In[21]:


bacon.remove('cat')
bacon


# In[ ]:


get_ipython().set_next_input('9. What are the list concatenation and list replication operators');get_ipython().run_line_magic('pinfo', 'operators')

List concatenation operator is +
List Replication operator is *


# In[ ]:


10. What is difference between the list methods append() and insert()?

apend() - this method will append the given value at the end of the list only

example: 
    list = [1,2,3,4]
    list.append(5)
     output:
            [1,2,3,4,5]
    
insert()- this method will insert the given value to the particular index provided or anywhere in the list

example: 
    list = [1,2,3,4]
    list.insert(1,8)
     output:
            [1,8,2,3,4,5]


# In[ ]:


get_ipython().set_next_input('11. What are the two methods for removing items from a list');get_ipython().run_line_magic('pinfo', 'list')

The 2 different methods to remove the items from the list are:
    
    1.remove()
    2.delete()


# In[ ]:


12. Describe how list values and string values are identical.

List values and string values are almost identical as both have indexes, we can use both in for loop. We can concatenate any new
value to both. We can find out the lenght of list values and string values by using len() functions. 


# In[ ]:


get_ipython().set_next_input("13. What's the difference between tuples and lists");get_ipython().run_line_magic('pinfo', 'lists')

Tuples:
    1. Tuples are immutable which cannot be changes.
    2. We use paranthesis () to define tuples.
    
Lists:
    
    1. List is mutable we can change it anytime. We can add or remove any values from the list.
    2. We use sqaure brackets [] to define lists.


# In[ ]:


14. How do you type a tuple value that only contains the integer 42?

tuple = (42,) (the comma is mandatory because tuple return the list of integers with the ()) if we do not use comma then it will
return only value 42 not the list


# In[ ]:


get_ipython().set_next_input("15. How do you get a list value's tuple form? How do you get a tuple value's list form");get_ipython().run_line_magic('pinfo', 'form')

We get a list value's tuple form by using tuple() function
We get a tuple value's list form by using list() function


# In[ ]:


get_ipython().set_next_input('16. Variables that "contain" list values are not necessarily lists themselves. Instead, what do they contain');get_ipython().run_line_magic('pinfo', 'contain')

They will contain references to list values rather than list values themselves.


# In[ ]:


17. How do you distinguish between copy.copy() and copy.deepcopy()?

1. copy.copy() function will do a shallow copy of a list
2. copy.deepcopy() function will do a deep copy of a list means it will duplicate any lists inside the list.

The both functions have same value but different ids

