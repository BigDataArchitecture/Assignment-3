import h5py
import numpy as np
import os

def run(eventid,file, end):
    # parent_dir = "/Users/parthshah/Documents/Northeastern/Spring2022/BigDataAnalytics/Assignment3/API/Intermediate_Files/"
    path = "Dummy Variable plz delete"
    data_path = "/Users/parthshah/Documents/Northeastern/Spring2022/BigDataAnalytics/Assignment3/data/raw/VIL_H5_Files/"
    file_path = data_path + file.split("/")[2]
    print(file_path)
    data = h5py.File(file_path, 'r')
    s = np.s_[end-1:end:end+1]
    vil = data['vil'][s]

    res = {'IN':[],"OUT":[]}
    for i in vil:
        split_data(i, res)
    # path = os.path.join(parent_dir, str(eventid))
    # try: 
    #     os.mkdir(path) 
    #     os.mkdir(path+'/Prediction')
    #     os.mkdir(path+'/Prediction/Array')
    #     os.mkdir(path+'/Prediction/Images')
    #     os.mkdir(path+'/Prediction/Images/12Images')
    # except OSError as error: 
    #     print(error)  
    res["IN"] = np.array(res["IN"])
    res["OUT"] = np.array(res["OUT"])

    # with h5py.File(path+"/data.h5", 'w') as data:
    #     data['IN'] = res["IN"]
    #     data['OUT'] = res["OUT"]
    # print("Testing data saved to:",path)
    return path,res


def split_data(array, res):
    for i in range(25):
        temp = np.dsplit(array, np.array([i, i + 13, i + 25]))
        res['IN'].append(temp[1])
        res['OUT'].append(temp[2])


