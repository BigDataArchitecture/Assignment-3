from typing import Optional
import uvicorn
from fastapi import FastAPI, File,HTTPException
from pydantic import BaseModel
import tensorflow as tf
import input_main
# from Functions import make_gif
import os
import h5py
import io
from fastapi.responses import FileResponse
from starlette.responses import StreamingResponse
import numpy as np
import glob
from PIL import Image
from matplotlib import pyplot as plt
import json

app = FastAPI()

@app.get("/")
def welcome():
     return FileResponse('/Users/parthshah/Downloads/international-Container-Cargo-ship-in-the-ocean.jpg')

# Api root or home endpoint
@app.get('/nowcast_results/backtest/')
def nowcast_backtest_function(begin_location,begin_yearmonth:int,begin_day:int,begin_time:int,model: Optional[str] = None,index: Optional[str] = None):
    output = {}
    if model== "":
        model = "gan_generator"
    if index == "":
        index = 24
    output['Model'] = model
    output['Index'] = index
    print("model",model)
    try:
        path,describe,y_pred = input_main.input(begin_location,begin_yearmonth,begin_day,begin_time,model,int(index))
        if path == 1:
            raise HTTPException(status_code=404, detail="Event not found")
        else:
            for i in range(12):
                output[i] = y_pred[:,:,:,i].tolist()            
            return output            
            # return {"Model": model, "Index":index,"Main":path, "Y Preds":"/Prediction/Array/Y_Pred.h5","Y Preds Analyse Image":"/Prediction/Image/Prediction.png","describe":describe}
    except IndexError as error: 
        print(error)
        raise HTTPException(status_code=404, detail=str(error))
    except UnboundLocalError as error:
        raise HTTPException(status_code=406, detail="No such Model Please select any of following ['gan_generator','mse_and_style','style','mse_file']")


@app.get('/nowcast_results/forecast/')
def nowcast_forecast_function(begin_location,begin_yearmonth:int,begin_day:int,begin_time:int,model: Optional[str] = None,index: Optional[str] = None):
    print("index",index)
    if model== "":
        model = "gan_generator"
    if index == "":
        index = 24
    output = {}
    try:
        output['Model'] = model
        output['Index'] = index
        path,describe,y_pred = input_main.input(begin_location,begin_yearmonth,begin_day,begin_time,model,int(index))
        if path == 1:
            raise HTTPException(status_code=404, detail="Event not found")
        else:
            for i in range(12):
                output[i] = y_pred[:,:,:,i].tolist()
            return output
            # {"Y Pred":y_pred.shape,"Model": model, "Index":index,"Main":path, "Y Preds":"/Prediction/Array/Y_Pred.h5","Y Preds 12 Image":"/Prediction/Image/12Images/","Describe":describe}
    except IndexError as error: 
        print(error)
        raise HTTPException(status_code=404, detail=str(error))
    except UnboundLocalError as error:
        raise HTTPException(status_code=406, detail="No such Model Please select any of following ['gan_generator','mse_and_style','style','mse_file']")

@app.get('/nowcast_results/backtest/latlong/')
def nowcast_backtest_analysis_function(lat:float,lon:float,distance:int,model: Optional[str] = None,index: Optional[str] = None):
    output = {}
    if model== "":
        model = "gan_generator"
    if index == "":
        index = 1
    output['Model'] = model
    output['Index'] = index
    try:
        path,describe,y_pred = input_main.input_latlong(lat,lon,distance,model,index)
        if path == 1:
            raise HTTPException(status_code=404, detail="Event not found")
        else:
            for i in range(12):
                output[i] = y_pred[:,:,:,i].tolist()
            return output
            # return {"Model": model, "Index":index,"Main":path, "Y Preds":"/Prediction/Array/Y_Pred.h5","Y Preds Analyse Image":"/Prediction/Image/Prediction.png","describe":describe}
    except IndexError as error: 
        print(error)
        raise HTTPException(status_code=404, detail=str(error))
    except UnboundLocalError as error:
        raise HTTPException(status_code=406, detail="No such Model Please select any of following ['gan_generator','mse_and_style','style','mse_file']")


@app.get('/nowcast_results/forecast/latlong/')
def nowcast_forecast_gif_function(lat:float,lon:float,distance:int,model: Optional[str] = None,index: Optional[str] = None):
    output = {}
    if model== "":
        model = "gan_generator"
    if index == "":
        index = 24
    print("model",model)
    output['Model'] = model
    output['Index'] = index
    try:
        path,describe,y_pred = input_main.input_latlong(lat,lon,distance,model,index)
        if path == 1:
            raise HTTPException(status_code=404, detail="Event not found")
        else:
            for i in range(12):
                output[i] = y_pred[:,:,:,i].tolist()
            return output
            # return {"Model": model, "Index":index,"Main":path, "Y Preds":"/Prediction/Array/Y_Pred.h5","Y Preds 12 Image":"/Prediction/Image/12Images/","Describe":describe}
    except IndexError as error: 
        print(error)
        output["Error"] = str(error)
        raise HTTPException(status_code=404, detail=str(error))
    except UnboundLocalError as error:
        raise HTTPException(status_code=406, detail="No such Model Please select any of following ['gan_generator','mse_and_style','style','mse_file']")


# @app.get('/nowcast_results/try/')
# def nowcast_forecast_gif_function1():
#     a = h5py.File('/Users/parthshah/Documents/Northeastern/Spring2022/BigDataAnalytics/Assignment3/API/Intermediate_Files/694474/Prediction/Array/Y_Pred.h5','r')
#     dict1 = {}
#     dict1[1] = a['Pred'][:,:,:,11]
#     print(type(dict1))
#     str1 = str(dict1)
#     print(json.dumps(dict1[1].tolist()))
#     return dict1[1].tolist()


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8001, reload=True)
