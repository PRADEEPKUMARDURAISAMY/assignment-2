#!/usr/bin/env python
# coding: utf-8

# In[6]:


sentence = input("Input a word to reverse: ")

for char in range(len(sentence) - 1, -1, -1):
    print(sentence[char], end="")
print("\n")

