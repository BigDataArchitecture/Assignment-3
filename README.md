Assignment3
==============================

**Creating FASTAPI for Maritime Nowcasting**

Lets do some basics first! 

Why is API required?
Well, API allows us to share our results with the world in an easy way!
Imagine you are running the SEVIR model and sharing the images over email! One time its fine! Again and again its a pain.
So we have the API. Request as many outputs, no limits on our Maritme API.

Our Maritime API will take 13 images as input and output a set of 12 Image arrays. These are predictions of next one hour of images.

Our API Documentation: https://documenter.getpostman.com/view/5665918/UVyn1JLo

New to API and dont know how to access it? Sit tight from here on we will explain you in detail everything

1) In API we have endpoints, endpoint is same as a "door" to something
We have the following endpoints(gates) for our Maritime usecase:

a) **/nowcast_results/forecast/**

Description: This endpoint will help you forecast next one hour of weather images depending on the input time and location you give it in the input parameters.

Note: Model and index in this parameters are optional. But you can give 

Input Parameters: 
    -- begin_location: City Name
    -- begin_yearmonth: Year-Month
    -- begin_day: Day
    -- begin_time : Time
    -- model: 
    -- index (Optional):
    
 Sample input:
 
 ![image](https://user-images.githubusercontent.com/78776808/160180751-9b040734-1136-4edc-9716-2057ec9091cc.png)


b) **/nowcast_results/forecast/latlong/**

Description: This endpoint will help you forecast next one hour of weather images depending on the input latitude, longitude and distance you give it in the input parameters.

Input parameters:
    -- lat: Latitude
    -- lon: Longitude
    -- distance: Distance value to predict the weather for the nearest loicat
    -- model:
    -- index(Optional): 

Sample input: 

![image](https://user-images.githubusercontent.com/78776808/160180937-b192ced4-0073-404c-82be-6641b7e5a3d6.png)


Error Handling:
We handled error with the help of different ports. So status 200 will not come up when you have an error fetching data from API
1) status_code=404 for "Event not found"
2) status_code=406 for "Invalid Model Name"
3) status_code=200 for "Correct Response"

    
To make requests to our API head towards: https://bigdata-assignment-340502.ue.r.appspot.com

If it is difficult for you to access the API you can also use our webapp to forecast
https://share.streamlit.io/shahparth0007/maritime_streamlit/main/streamlit.py
