import os
import matplotlib.image as mpimg
import numpy as np
from PIL import Image
import json
from collections import OrderedDict

obj = OrderedDict()
masked_img=os.listdir(r'C:\Users\no\Desktop\경은\train\masked_img')


for x in masked_img:
    masked_img_path = r'C:\Users\no\Desktop\경은\train\masked_img/'+x
    mask = np.array(Image.open(masked_img_path))
    mask = mask.tolist()
    obj = {
        'shape':{'label':'defect','name':x.split('.')[0],'mask':mask}
    }
    with open(r'C:\Users\no\Desktop\경은\train\label_Data/{0}.json'.format(x.split('.')[0]),'w',encoding='utf-8') as make_file:
        json.dump(obj,make_file,ensure_ascii=False,indent='\t')