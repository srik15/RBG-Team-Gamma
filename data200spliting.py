import pandas as pd
import numpy as np
import os
import shutil
df=pd.read_csv("D:/RBG.AI/forest_image_classification/data_splitting/train_labels.csv") 
folder_path1="D:/RBG.AI/forest_image_classification/train_features.csv"
source_folder="D:/RBG.AI/forest_image_classification/train_features"
for i in df.columns[1:]:
    x = np.array([])
    count = 0
    if not os.path.exists(folder_path1):
        os.makedirs(folder_path1)
    for j in range(len(df)):
        if count>200:
            break
        if df[i][j] == 1:
            count+=1
            val = df["id"][j]
            x = np.append(x,val)
    print(f"{len(x)},{i}")
    destination_folder=f"D:/RBG.AI/forest_image_classification/data_splitting/poc_sample_data/{i}"
    for filename in x:
        file_to_copy=f"{filename}.jpg"
        source_filepath = os.path.join(source_folder,file_to_copy)
        destination_filepath = os.path.join(destination_folder,file_to_copy)
        if os.path.exists(source_filepath):
            shutil.copyfile(source_filepath,destination_filepath)
    
            

