#!/usr/bin/env python
# coding: utf-8

# In[38]:


player_score =  {}
with open("scores.csv","r") as rd:
    for line in rd:
        player,score = line.split(',')
        score = int(score)
        if player in player_score:
            player_score[player].append(score)
        else:
            player_score[player] = [score]
print(player_score)


# In[ ]:





# In[40]:


for i,j in player_score.items():
    minj = min(j)
    maxj = max(j)
    avgj = sum(j)/len(j)
    print(f"the minimum for {i} is {minj} , max is {maxj} and avg is {avgj}")


# In[ ]:





# In[ ]:




