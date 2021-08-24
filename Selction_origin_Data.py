
import os
origin_list=os.listdir(r'C:\Users\no\Desktop\경은\defect\origin')
ol=[x.split('.')[0] for x in origin_list]

label_list=os.listdir(r'C:\Users\no\Desktop\경은\defect\label_Data')
ll=[x.split('.')[0] for x in label_list]




for i in ol:
    if i not in ll :
        os.remove(r'C:\Users\no\Desktop\경은\defect\origin/'+i+'.bmp')



