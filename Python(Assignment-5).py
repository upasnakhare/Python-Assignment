#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input("1. What does an empty dictionary's code look like");get_ipython().run_line_magic('pinfo', 'like')

An empty dictionary's code will look like as {}

example: dict = {}


# In[1]:


2. What is the value of a dictionary value with the key 'foo' and the value 42?

The value of dictionary for the above example is: 

dict = {'foo' : 42}
dict


# In[ ]:


get_ipython().set_next_input('3. What is the most significant distinction between a dictionary and a list');get_ipython().run_line_magic('pinfo', 'list')

The list is an ordered collection of data with an individual indexes, however the dictionary stores the value in a key value pair which are unordered.


# In[3]:


4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?

We will get a keyerror shown below: 

spam = {'bar' : 100}
spam['foo']


# In[ ]:


5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?

There will be no difference as in operator will check wheather the value exists as a key in the dictionary.


# In[ ]:


6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?

'cat' in spam checks whether there is a key 'cat' in the dictionary, while 'cat' in spam.values() checks whether there is 
a value 'cat' for one of the keys in spam .


# In[6]:


get_ipython().set_next_input('7. What is a shortcut for the following code');get_ipython().run_line_magic('pinfo', 'code')
if 'color' not in spam:
spam['color'] = 'black'

The shortcut for the code is below as setdefault() method returns the value of the item with the specified key. 
If the key does not exist, insert the key, with the specified value:
    
    spam.setdefault('color', 'black')


# In[8]:


get_ipython().set_next_input('8. How do you "pretty print" dictionary values using which module and function');get_ipython().run_line_magic('pinfo', 'function')

pprint.pprint() module and function will be used to "pretty print" dictionary values.

