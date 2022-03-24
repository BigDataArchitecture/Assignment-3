from turtle import distance
from Functions import datapipeline
from Functions import filtering_function
from Functions import prediction_funtion
from Functions import make_gif

import os
import h5py
import numpy as np

def input(BEGIN_LOCATION,BEGIN_YEARMONTH,BEGIN_DAY,BEGIN_TIME, model,index):
    print("Inside Input Main Time")
    event_id,file_path,file_index,describe, = filtering_function.filtering_time(BEGIN_LOCATION,BEGIN_YEARMONTH,BEGIN_DAY,BEGIN_TIME)
    if event_id == 0:
        return 1,1,1
    else:
        path,res = datapipeline.run(event_id,file_path,file_index)
        y_pred = prediction_funtion.predict(path,model,index,res)
        return path,describe,y_pred

def input_latlong(lat,lon,distance, model,index):
    print("Inside Input Main Latlong")
    event_id,file_path,file_index,describe, = filtering_function.filtering_distance(lat,lon,distance)
    if event_id == 0:
        return 1,1,1
    else:
        path,res = datapipeline.run(event_id,file_path,file_index)
        y_pred = prediction_funtion.predict(path,model,index,res)
        return path,describe,y_pred
