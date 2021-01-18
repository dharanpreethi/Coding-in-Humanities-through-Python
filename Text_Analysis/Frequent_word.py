#!/usr/bin/env python
# coding: utf-8

# # Text Analysis
# The computational text analysis began in the early 1949s when Father Robert Busa produced concordance for Thomas Aquinas’ works by using computer. Later, it is extended to investigate author attribution, stylistic and linguistic variation. This process augmented after the establishment of the digitisation of printed text, digital publication and digital formation that transform the humanities way of approaching the text.
# 
# In this lesson, first we are going to learn a simple frequent word analysis and then move to...

# ### Frequent word analysis ###
# 
# For this analysis, we can download a text file of a...from Gutenberg...I will also explain the same using the HTML link of the novel.

# In[126]:


from collections import Counter # import this module for counting the words 
import pandas as pd
import matplotlib as plt
import re


# #### what is stopwords list? ####
# This might sound familiar to most of you! Removing words like _a_,_an_,_the_ etc.would...

# Now we access the text (copy the text file and place it in your working directory)

# In[127]:


file = open ('Pamela.txt', encoding = "UTF-8") 


# In[128]:


text = file.read() #read the file


# In[42]:


text_clean1 = re.sub("[^a-zA-Z]+", " ", text)
text_clean2 = text_clean1.lower()


# In[43]:


type(text_clean2)


# In[129]:


os.chdir ('C:\\Users\\Shanmugapriya\\CoursePythonprojects')


# In[130]:


file = open ('Pamela.txt', encoding = "UTF-8") 
text = file.read()


# ##### Next we need to remove the metadata such as the information related to author, publisher and Project Gutenberg #####

# In[131]:


extract1 = text.find("LETTER I")
extract2 = text.find("End of Project Gutenberg's Pamela, or Virtue Rewarded, by Samuel Richardson")
analysis_part = text[extract1:extract2]
print(analysis_part)


# In[ ]:


stopwords = set(line.strip() for line in open('stopwords_en.txt'))

wordcount = {}

for word in analysis_part.lower().split():
    word = re.sub("[^a-zA-Z]+", " ", analysis_part)
    #word = word.replace(".","")
    #word = word.replace(",","")
    #word = word.replace(":","")
    #word = word.replace("\"","")
    #word = word.replace("!","")
    #word = word.replace("â€œ","")
    #word = word.replace("â€˜","")
    #word = word.replace("*","")
    if word not in stopwords:
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1


# In[125]:


import collections
word_counter = collections.Counter(wordcount)
n_print = int(input("How many most common words to print: "))
for count in word_counter.most_common(n_print):
    print(count)
lst = word_counter.most_common(n_print)
df = pd.DataFrame(lst, columns = ['Word', 'Count'])
df.plot.bar(x='Word',y='Count')

