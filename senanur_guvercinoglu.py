#!/usr/bin/env python
# coding: utf-8

# In[320]:



#Build a software that searches Twitter for the term "request for startup" and extracts information, 
#in other words tweets, then stores this information in a very simple file format, such as a CSV file or a
#simple text file, and displays results in a simple web interface.


#I used twint module to the reaches tweets realted with term "request for startup".



#!/usr/bin/env python
# coding: utf-8
get_ipython().system('pip3 install twint')


# In[321]:


get_ipython().system('pip install nest_asyncio')


# In[322]:


import twint


# In[323]:


pip install --upgrade pip


# In[324]:


#scraping tweets related with specific search key; "request for startup" and write csv file.


import nest_asyncio
nest_asyncio.apply()

nest_asyncio.apply()


c = twint.Config()
c.Search = 'request for startup' #search tweets with related key
c.Limit = 10
c.Until="2020-07-14" #limit the date 
c.t="Tweet id:{id}| Date:{date}| Time:{time}| Tweet:{tweet}|Likes Count:{likes_count}"
c.Store_json = True
c.Output = "twt.csv"#write tweets to the csv file
twint.run.Search(c)



# In[328]:


import pandas as pd 
from pandas import DataFrame
pd.options.display.max_columns=100

df = DataFrame(data)

#sort columns  
sort_columns = df.sort_values(['retweets_count','likes_count','replies_count','date'],ascending=(False,True,False,True))

#cleaning tweets data frame with specific ones and delete null columns 

test = sort_columns[['id', 'conversation_id','created_at','date','time','timezone','user_id','username','name','place','tweet','language','mentions','replies_count','retweets_count','likes_count','retweet']]



# In[329]:


test.head(30) #tweets with related search key and specific columns


# In[330]:


csvfile=test.to_csv('tweets_final.csv') #create csv file from new data frame


# In[331]:


import pandas as pd

# Read the csv file in
df = pd.read_csv('tweets_final.csv')

# Save to file
df.to_html('Tweet_Table.html')

# Assign to string
htmTable = df.to_html()

