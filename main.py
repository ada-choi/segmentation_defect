import os
import sys
import random
import math
import re
import time
import numpy as np
import cv2
import matplotlib
import matplotlib.pyplot as plt
import json

os.environ["CUDA_VISIBLE_DIVICES"]='1'
# Root directory of the project
ROOT_DIR ='/mnt/c/Users/no/PycharmProjects/proto_mrcnn'
# r'C:\Users\no\PycharmProjects\proto_mrcnn'


# Import Mask RCNN
sys.path.append(ROOT_DIR)  # To find local version of the library
from Mask_RCNN.mrcnn.config import Config
from Mask_RCNN.mrcnn import utils
import Mask_RCNN.mrcnn.model as modellib
from Mask_RCNN.mrcnn import visualize
from Mask_RCNN.mrcnn.model import log
from Config import *
from DefectDataset import *

#%matplotlib inline


# Directory to save logs and trained model
MODEL_DIR = os.path.join(ROOT_DIR, "logs")

# Local path to trained weights file
COCO_MODEL_PATH = os.path.join(ROOT_DIR, "mask_rcnn_coco.h5")
# Download COCO trained weights from Releases if needed
if not os.path.exists(COCO_MODEL_PATH):
   utils.download_trained_weights(COCO_MODEL_PATH)

# Create training and validation set
# train set

dataset_train = DefectDataset()
dataset_train.load_dataset('/mnt/d/ADA/경은/train')
    #r'C:\Users\no\Desktop\경은\train')
    # '/mnt/c/Users/no/Desktop/경은/train')
dataset_train.prepare()
#print('Train: %d' % len(dataset_train.image_ids))

# test/val set
dataset_val = DefectDataset()
dataset_val.load_dataset('/mnt/d/ADA/경은/test')
    #r'C:\Users\no\Desktop\경은\test')
#'/mnt/c/Users/no/Desktop/경은/test')
dataset_val.prepare()
#print('Test: %d' % len(dataset_val.image_ids))

# Load and display random samples
# image_ids = np.random.choice(dataset_train.image_ids, 4)
# for image_id in image_ids:
#     image = dataset_train.load_image(image_id)
#     mask, class_ids = dataset_train.load_mask(image_id)
#
#     visualize.display_top_masks(image, mask, class_ids, dataset_train.class_names)


model = modellib.MaskRCNN(mode="training", config=config,
                          model_dir=MODEL_DIR)

# Which weights to start with?
init_with = "coco"  # imagenet, coco, or last

if init_with == "imagenet":
    model.load_weights(model.get_imagenet_weights(), by_name=True)
elif init_with == "coco":
    # Load weights trained on MS COCO, but skip layers that
    # are different due to the different number of classes
    # See README for instructions to download the COCO weights
    model.load_weights(COCO_MODEL_PATH, by_name=True,
                       exclude=["mrcnn_class_logits", "mrcnn_bbox_fc",
                                "mrcnn_bbox", "mrcnn_mask"])
elif init_with == "last":
    # Load the last model you trained and continue training
    model.load_weights(model.find_last(), by_name=True)

model.train(dataset_train, dataset_val,
            learning_rate=config.LEARNING_RATE,layers='head',
            epochs=5
            )
