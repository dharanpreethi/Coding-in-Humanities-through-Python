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



file = open ('Pamela.txt', encoding = "UTF-8") 
text = file.read()


# ##### Next we need to remove the metadata such as the information related to author, publisher and Project Gutenberg #####

# In[131]:


extract1 = text.find("LETTER I")
extract2 = text.find("End of Project Gutenberg's Pamela, or Virtue Rewarded, by Samuel Richardson")
analysis_part = text[extract1:extract2]
print(analysis_part)


# In[141]:


stopword_list = set(line.strip() for line in open('stopwords_en.txt'))

Frequent_word = {}

for words in analysis_part.lower().split():
    words = words.replace(".","")
    words = words.replace(",","")
    words = words.replace(":","")
    words = words.replace("\"","")
    words = words.replace("!","")
    words = words.replace("â€œ","")
    words = words.replace("â€˜","")
    words = words.replace("*","")
    if words not in stopword_list:
        if words not in Frequent_word:
            Frequent_word[words] = 1
        else:
            Frequent_word[words] += 1


# In[144]:


import collections
top_words = collections.Counter(Frequent_word)


no_top_words = int(input("How many the most frequent words to print: "))
for count in top_words.most_common(no_top_words):
    print(count)
lsts = top_words.most_common(no_top_words)
df = pd.DataFrame(lsts, columns = ['Word', 'Count'])
df.plot.bar(x='Word',y='Count')


# In[ ]:





# In[ ]:




