#!/usr/bin/env python
# coding: utf-8

# # Task 1: Read a File and Handle Errors 
# 

# In[8]:


get_ipython().run_cell_magic('writefile', 'sample.txt', 'this is sample text file\nit contains multiple lines')


# In[10]:


try:
    with open('sample.txt', 'r') as file:
        for index, line in enumerate(file, start=1):
            print(f"line {index}: {line.strip()}")
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")


# # Task 2: Write and Append Data to a File

# In[1]:


user_input = input("Enter text to write to the file: ")
with open('output.txt', 'w') as file:
    file.write(user_input)
print("Data successfully written to output.txt.")

additional_data = input("Enter additional text to append: ")
with open('output.txt', 'a') as file:
    file.write(" " + additional_data) 
print("Data successfully appended.")

with open('output.txt', 'r') as file:
    print("Final content of output.txt:")
    print(file.read())


# In[ ]:




