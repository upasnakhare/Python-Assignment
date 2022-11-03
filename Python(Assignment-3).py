#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input('1. Why are functions advantageous to have in your programs');get_ipython().run_line_magic('pinfo', 'programs')

Having functions in program is beneficial because we can reuse a piece of code at any point of a time. 


# In[ ]:


get_ipython().set_next_input("2. When does the code in a function run: when it's specified or when it's called");get_ipython().run_line_magic('pinfo', 'called')
    
The code of a function will get run when the function is called.


# In[ ]:


get_ipython().set_next_input('3. What statement creates a function');get_ipython().run_line_magic('pinfo', 'function')

Def statement is used to create a function. Ex:  def test()


# In[ ]:


get_ipython().set_next_input('4. What is the difference between a function and a function call');get_ipython().run_line_magic('pinfo', 'call')

function: 
    1. A function is a piece of code which is used perform a specific operation or it is used to overcome the repeatation of code in our program. 

function call:
    1. A function call is used to invoke or call the function which we have written to perform a particular operation. 


# In[ ]:


get_ipython().set_next_input('5. How many global scopes are there in a Python program? How many local scopes');get_ipython().run_line_magic('pinfo', 'scopes')

There is only one global scope in python. When we create a variable inside the function that variable is belongs to the local scope of that function which is used inside that function only. 


# In[ ]:


get_ipython().set_next_input('6. What happens to variables in a local scope when the function call returns');get_ipython().run_line_magic('pinfo', 'returns')

When the function calls return the variable in a local scope gets destroyed. 


# In[ ]:


get_ipython().set_next_input('7. What is the concept of a return value? Is it possible to have a return value in an expression');get_ipython().run_line_magic('pinfo', 'expression')

A return value is a value which we get when return statement ends the execution of a function. The return value can be used in an expression like any other values.    


# In[ ]:


get_ipython().set_next_input('8. If a function does not have a return statement, what is the return value of a call to that function');get_ipython().run_line_magic('pinfo', 'function')

If a function doesn’t have return statement than the return value of that function which has been called will be “none type”.


# In[ ]:


get_ipython().set_next_input('9. How do you make a function variable refer to the global variable');get_ipython().run_line_magic('pinfo', 'variable')

We can use global keyword/statement to declare the variable of a function which will act as a global varibale after declaration. 


# In[ ]:


get_ipython().set_next_input('10. What is the data type of None');get_ipython().run_line_magic('pinfo', 'None')

Data type of “None” is “none type”.


# In[ ]:


get_ipython().set_next_input('11. What does the sentence import areallyourpetsnamederic do');get_ipython().run_line_magic('pinfo', 'do')

This sentence will import the module named as areallyourpetsnamederic.


# In[ ]:


get_ipython().set_next_input('12. If you had a bacon() feature in a spam module, what would you call it after importing spam');get_ipython().run_line_magic('pinfo', 'spam')

We will call it as spam.bacon()


# In[ ]:


get_ipython().set_next_input('13. What can you do to save a programme from crashing if it encounters an error');get_ipython().run_line_magic('pinfo', 'error')

We can write the particular code which in a try block to save it from crashing.


# In[ ]:


get_ipython().set_next_input('14. What is the purpose of the try clause? What is the purpose of the except clause');get_ipython().run_line_magic('pinfo', 'clause')

The piece of code which can possible through an error will be in try clause and the code which get executes if an error occurs will be in except clause

