# import required module
import os
import pandas as pd
# assign directory
directory = 'manual_tag_data'
 
# iterate over files in
# that directory
count = 0
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        print(f)

        # do the splitting part 
        # read file in 
        df = pd.read_csv(f)

        # adding one more column to the df
        data = df
        data["Tagged_Sentence"] = "_"

        # export to something new //mayb can skip this one to prevent any overwritting 
        data.to_csv("to_tag_data/manual_" + str(count) + "tagged.csv", index = False)

        count+=1

print(count)
