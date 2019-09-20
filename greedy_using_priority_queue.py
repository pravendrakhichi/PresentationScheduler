#!/usr/bin/env python
# coding: utf-8

"""
Description:-
 ****Very Efficient Solution

  This Method uses a priority queue to store distances between nodes( presentations ) and take pair with 
  maximum distance and place it in different sessions of same time slot if overall goodness value is rising.
  This method considers 3 cases. 
 1) p1(s1,t1) and p2(any s, t2!=t1) If pair of presentations is in different time slots then find node in one
  of the pairs time slot p3(s3!=s1 , t1) or p3(s3!=s2 , t2)  such that it is at minimum distance from p1 or 
  p2(whichever in the same point) and swap with the node in different slot.
  
 2) p1(s1,t1) and p2(s2!=s1, t1) No changes required.

 3) p1(s1,t1) and p2(s1, t1) Find node p3(s3!=s1) such that it is minimum distant from any point. and swap.

 Important :- Greedy solutions many times depend on initial state. Therefore we use randomize function to 
 start algorithm from s*t*p*4 different states.
"""
# In[1]:
# Function Extracts table from txt file to a matrix along with sessions,time_slot and no of presentations.
import sys

def input_file(address):
    with open(address,'r') as file:
        lines=file.readlines()
        presentations=lines[0]
        print(presentations)
        sessions=lines[1]
        time_slot=lines[2]
        trade_off=lines[3]
        lines=lines[4:]
        lines=[line[:-1].split(" ") for line in lines]
       
        data=[[float(lines[i][j]) for j in range(0,len(lines))] for i in range(0,len(lines[0]))]       
        return int(presentations),int(sessions),int(time_slot),float(trade_off),data
        

# In[ ]:
# Function to evaluate goodness of current state.
def goodness(p,s,z,t,dict1):
    distance=0
    unidist=0
    no_of_presentation=s*p*t
    for i in range(no_of_presentation):
        for j in range(i+1,no_of_presentation):
            if(dict1[i][0]!=dict1[j][0] and dict1[i][1]==dict1[j][1]):
                distance+=dis[i][j]
            if(dict1[i][0]==dict1[j][0] and dict1[i][1]==dict1[j][1]):
                unidist+=1-dis[i][j]
                
    return z*distance+unidist


# In[ ]:
# Function to perform swap (edit values of session and time slot in dictionary)
def swap(pres1,pres2):
       temp=dict1[pres1]
       dict1[pres1]=dict1[pres2]
       dict1[pres2]=temp

# In[ ]:
# Function to check if swap is any good at all. returns true if goodness after swap is higher
def is_safe(pres1,pres2,y):
    old=goodness(p,s,z,t,dict1)
    swap(pres1,pres2)
    new=goodness(p,s,z,t,dict1)
    swap(pres2,pres1)
    if old>new:
        return False,old,new
    else:
        return True,old,new


# In[ ]:
# Function to find node (presentation) p3(s,t) in the same time slot to swap.
def minimum_fn(p1):
    s1,t1=dict1[p1]
    mini=2.0
    ans=p1
    for i in range(p*s*t):
        if(dict1[i][0]!=s1  and dict1[i][1]==t1):
            if(dis[i][p1]<mini):
                mini=dis[i][p1]
                ans=i
    return ans


# In[ ]:

#print("Value of s : %d"%s)
#s=3
#p=2
#t=2
dict1={}
i=0



# In[ ]:
# Function to initialize greedy algorith with different initial states

import random
def randomize():
    for i in range(24):
        a=random.randint(0,p*s*t-1)
        b=random.randint(0,p*s*t-1)
        swap(a,b)


# In[ ]:
# Priority queue stores distance, p1,p2 whereas distance is stored with -ve sign to have maximum distance
#  as top. Once all distances entered, one by one, maximum distance pairs are arranged according to description

from queue import PriorityQueue
y=0
def optimizer(y):
    no_of_presentation=s*t*p
    randomize()
    q=PriorityQueue()
    for i in range(no_of_presentation):
        for j in range(i+1,no_of_presentation):
            q.put((-dis[i][j],i,j))
    while not q.empty():
        _,p1,p2=q.get()
        if((dict1[p1][0]!=dict1[p2][0] and dict1[p1][1]==dict1[p2][1])):
            y+=1
        else:
            pres2=minimum_fn(p1)
            pres3=minimum_fn(p2)
            flag1,old_val,new_val=is_safe(pres2,p2,y)
            flag2,oldval,newval=is_safe(pres3,p1,y)
            if(new_val>newval and flag1):
                swap(pres2,p2)
                goodval=new_val
            elif(newval>new_val and flag2):
                swap(pres3,p1)
                goodval=newval
            else:
                goodval=oldval
            y+=1

    print(goodval)
    
    return goodval
        

# In[2]:
# Taking inputs from file and storing weighted edges in dictionary as dict[p1]=[session, time_slot]

p,s,t,z,dis=input_file(str(sys.argv[1]))

print("val of s : %d"%s)

print("val of t : %d"%t)

print("val of p : %d"%p)
#s=3
#p=2
#t=2
for j in range(s):
    for l in range(t):
        for k in range(p):
            dict1[i]=[j,l]
            i+=1
dict1
# In[ ]:
# start initializer and check for maximum goodness output.

ans={}
maxofall=0
for i in range(s*t*p*4):
    good_value=optimizer(y)
    if(maxofall<good_value):
        maxofall=good_value
        ans=dict1.copy()
        print(maxofall)

print("Maximum Goodness value from all random starts: %f "%maxofall)

# In[ ]:
# Code for output in file "output.txt"
#print(ans)
list_key=[i for i in ans]
list_val=[[i,c] for i,c in ans.values()]
line=""
filename=str(sys.argv[2])
with open(filename,"w+") as file:
    for i in range(s):
        for j in range(t):
            for k in range(s*t*p):
                if(list_val[k]==[i,j]):
                    line+="%d "%(k+1)
            line+="| "
        line=line[:-2]
        file.write(line+'\n')
        print(line)
        line=""
    file.close()


