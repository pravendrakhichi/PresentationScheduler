import random
import sys



"""
Description:-

This approach is using greedy approach by searching for most optimal swap and then swap and 
doing it same again and again for considerable iterations.

"""
# In[ ]:
# Function to initialize greedy algorith with different initial states
def randomize():
    for i in range(24):
        a=random.randint(0,p*s*t-1)
        b=random.randint(0,p*s*t-1)
        swap(a,b)

# In[1]:
# Function Extracts table from txt file to a matrix along with sessions,time_slot and no of presentations.
def input_file(address):
    with open(address,'r') as file:
        lines=file.readlines()
        presentations=lines[0]
        sessions=lines[1]
        time_slot=lines[2]
        trade_off=lines[3]
        lines=lines[4:]
        lines=[line.split(" ") for line in lines]
        data=[[float(lines[i][j]) for j in range(0,len(lines))] for i in range(0,len(lines[0]))]
        return int(sessions),int(time_slot),int(presentations),float(trade_off),data

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
# Function to take inputs from file

s,t,p,z,dis=input_file(str(sys.argv[1]))
dict1={}
dict_i=0
for j in range(s):
    for l in range(t):
        for k in range(p):
            dict1[dict_i]=[j,l]
            dict_i+=1

# In[ ]:
# Function always search for most optimal solution by searching for maximum value increament in goodness.
# Here also we have initialized solution using randomize.

def optimizer_greedy(y):
    no_of_presentation=s*t*p
    max_goodness=0
    dt=[0,0]
    old=0
    for i in range(no_of_presentation):
        for j in range(i+1,no_of_presentation):
            bool1,old,new=is_safe(i,j,y)
            if bool1 and max_goodness<new:
                dt[0]=i
                dt[1]=j
                max_goodness=new
                #print("{}   {}  {}".format(i,j,new))
    swap(dt[0],dt[1])
    #print(goodness(p,s,z,t,dict1))
    print("iteration {}::old::{} new updated::{}".format(y,old,max_goodness))          
    y+=1
    return y,old,max_goodness
	
ans={}
maxofall=0

for i in range(6*s*t*p):
    y=0
    count=0
    randomize()
    good_value=0.0
    while(count!=5):        
        y,old,good_value=optimizer_greedy(y)
        
        if(int(good_value)>int(old)):
            count=0
        else:
            count+=1       
    if(maxofall<good_value):
        maxofall=good_value
        ans=dict1.copy()
    print("max goodness:: %s"%maxofall)
#print(ans)

# In[ ]:
# Code for output in file "output.txt"

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