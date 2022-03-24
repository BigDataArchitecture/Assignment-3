from Functions.nowcast_reader import read_data
from Functions import visualize
import os
os.environ["HDF5_USE_FILE_LOCKING"]='FALSE'
# import sys
# sys.path.append('../src/')
import h5py
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
import matplotlib.patches as patches
import pandas as pd

def predict(path,Model,index,res):
    path
    print("loading Model:",Model)
    gan_model = 0
    mse_style_model = 0
    style_model = 0
    mse_model = 0
    
    model_mapping = {"gan_generator":gan_model,"mse_and_style":mse_style_model,"style":style_model,"mse_file":mse_model}
            
    print("Loading Data")
    print("one sample file",res.keys())
    x_test,y_test = read_data(res)
    print(x_test.shape,y_test.shape)
    if Model == "gan_generator":
        path_file ="./Models/gan_generator.h5"
    elif Model == "mse_and_style":
        path_file = './Models/mse_and_style.h5'
    elif Model == "style":
        path_file = './Models/style_model.h5'
    elif Model == "mse_file":
        path_file = './Models/mse_file.h5'
    
    idx=index # adjust this to pick a case
    fig,ax = plt.subplots(4,7,figsize=(10,5), gridspec_kw={'width_ratios': [1,1,1,1,1,1,1]})
    y_pred = visualize.visualize_result([tf.keras.models.load_model(path_file,compile=False,custom_objects={"tf": tf})],x_test,y_test,idx,ax,path,labels=[Model])
    # fig.savefig(path + '/Prediction/Images/Prediction.png')    
    print("Saved Outputs")
    return y_pred
    
        