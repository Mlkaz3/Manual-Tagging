import pandas as pd
import math 

# read file in 
df = pd.read_csv("manual_tag_data/manual_0.csv")

# adding one more column to the df
data = df
data["Tagged_Sentence"] = "_"

# export to something new //mayb can skip this one to prevent any overwritting 
data.to_csv("tagged_data/manual_0_tagged.csv", index = False)
data = pd.read_csv("tagged_data/manual_0_tagged.csv")

# start the process of tagging
count = 0
for i in range(len(data)):
    
    tag_status = data["Tagged_Sentence"].loc[i]
    print(tag_status)
    
    if str(tag_status)=="_":
    # if tag_status=="":
        print("CURRRENT SENTENCE")
        current = data["Sentence"].loc[i]
        print(count, " -> ", current)
        # print("Empty")
        
        token_list = current.split()
        tuple_list = []
        for token in token_list:
            print(token)
            tag = input('Enter tag:')
            tag_tuple = (token,tag)
            tuple_list.append(tag_tuple)
        
        print(tuple_list)
        
        # print(data["Tagged_Sentence"].loc[i])
        data["Tagged_Sentence"].loc[i] = tuple_list
        # print(data["Tagged_Sentence"].loc[i])
        
        print("")
    else:
        print("hehe")
    count+=1
    if count==2:
        break

print("- end of sys -")