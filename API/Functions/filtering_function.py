from pydoc import describe
import pandas as pd
from geopy import distance

def filtering_time(BEGIN_LOCATION,BEGIN_YEARMONTH,BEGIN_DAY,BEGIN_TIME):
    df = pd.read_csv('/Users/parthshah/Documents/Northeastern/Spring2022/BigDataAnalytics/Assignment3/data/raw/Nowcast_Catalog.csv')
    try:
        print("finding your file")
        a = df[(df['BEGIN_LOCATION'] == BEGIN_LOCATION) & (df['BEGIN_YEARMONTH'] == BEGIN_YEARMONTH) & (df['BEGIN_DAY'] == BEGIN_DAY) & ((df['BEGIN_HH'] == BEGIN_TIME) | (df['BEGIN_TIME'] == BEGIN_TIME))]
        if len(a) > 0:
            event_id = int(a['event_id'].iloc[0])
            file_name = str(a['file_name'].iloc[0])
            file_index = int(a['file_index'].iloc[0])
            describe = a['EPISODE_NARRATIVE'].iloc[0]
            print('File Found')
            return event_id,file_name,file_index,describe
        else:
            print("Cannot find the File")
            return 0,0,0,0
            
    except Exception:
        traceback.print_exc()   

def filtering_distance(lat,lon,distance1):
    data = pd.read_csv('/Users/parthshah/Documents/Northeastern/Spring2022/BigDataAnalytics/Assignment3/data/raw/Nowcast_Catalog.csv')
    print(lat,lon)
    distance_list = []
    for i in range(len(data)):
        a = (data['BEGIN_LAT'].iloc[i],data['BEGIN_LON'].iloc[i])
        b = (lat,lon)
        distance_list.append(distance.distance(a,b).miles)
    data['Distance'] = distance_list
    a = data.sort_values(by=['Distance']).iloc[0]
    print(a['Distance'])
    if a['Distance'] < distance1:
        return a['event_id'],a['file_name'],a['file_index'],a['EPISODE_NARRATIVE']
    else:
        print("Cannot find the File")
        return 0,0,0,0