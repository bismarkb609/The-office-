#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Use this cell to begin your analysis, and add as many as you would like!
import matplotlib.pyplot as plt 
import pandas as pd 


# In[ ]:


episodeDataset = pd.read_csv("office_episodes.csv")
episodeDataset.info() # gives us information about the dataset 


# In[ ]:


# lets have a feel of how the data looks like visually 
fig = plt.figure() 
plt.plot(episodeDataset['episode_number'], episodeDataset['viewership_mil'])


# In[ ]:


# lets make a bit more easier to understand by using a scatter plot 


# In[ ]:


episodeNumber = episodeDataset["episode_number"] # subsetting the episode number 
episodeViewership = episodeDataset["viewership_mil"] # subsetting the number of views in (mil)


# In[ ]:


scaledRatings = episodeDataset["scaled_ratings"] # subsetting the scaled ratings 


# In[ ]:


colors_str = list() # creates and empty lists to append the string of the colors 

#from here, we try to add filters to the scaled ratings so we understand the plot very well 
for Ratings in scaledRatings:
    if Ratings < 0.25:       
        r_color = "red"
        colors_str.append(r_color)
    elif Ratings >= 0.25 and Ratings < 0.50:
        o_color = "orange"
        colors_str.append(o_color)
    elif Ratings >= 0.50 and  Ratings < 0.75:
        l_color = "lightgreen"
        colors_str.append(l_color)
    elif Ratings >= 0.75:
        dg_color = "darkgreen"
        colors_str.append(dg_color)


# In[ ]:


size_s = list() # creates an empty lists to assign the sizes into it 

# we will also like to know whether the dataset has a guest star or not and assign different marker sizes to it for more 
# understanding of the dataset 
guests = episodeDataset["has_guests"] 
for guest in guests:
    if guest == True: 
        s = 250
        size_s.append(s)
    elif guest == False: 
        s = 25
        size_s.append(s)


# In[ ]:


fig = plt.figure() # creteas a figure 

plt.scatter(episodeNumber, episodeViewership,s=size_s, c=colors_str) # creates a scatter plot of the data, with added filters 

#assigning the x and y lables and title 
plt.xlabel("Episode Number")
plt.ylabel("Viewership (Millions)")
plt.title("Popularity, Quality, and Guest Appearances on the Office")

plt.show() # shows the plot 


# In[ ]:


# name of guest start 
stars = episodeDataset[episodeDataset["viewership_mil"] == max(episodeViewership)]["guest_stars"]

listStars = list()
for star in stars: 
    listStars.append(star)


# In[ ]:


Stars = listStars[0]
top_star = Stars.split(",")[0] # gets the top star from the dataframe 
print(top_star)

