import numpy as np
import glob
from PIL import Image
from matplotlib import pyplot as plt
import h5py
    

def make_gif(frame_folder):
    frame_folder = frame_folder+"/Prediction/Images/12images/"
    frames = [Image.open(image) for image in glob.glob(f"{frame_folder}/*.png")]
    frame_one = frames[0]
    print(frames)
    frame_one.save(frame_folder+"/Animation.gif", format="GIF", append_images=frames,
               save_all=True, duration=100, loop=0)


def save_fig(path):
    print(path)
    a = h5py.File(path + "/Prediction/Array/Y_Pred.h5",'r')
    print(a['Pred'][0].shape)
    for i in range(11):
        plt.imshow(a['Pred'][0][:,:,i])
        plt.savefig(path + "/Prediction/Images/12images/"+ str(i)+".png")
    make_gif(path)

save_fig("/Users/parthshah/Documents/Northeastern/Spring2022/BigDataAnalytics/Assignment3/API/Intermediate_Files/694474")