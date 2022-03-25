Assignment3
==============================

Creating FASTApi for Maritime Nowcasting

Lets do some basics first! 

Why is API required?
Well, API allows us to share our results with the world in easier way!
Imagine you running the the SEVIR model and sharing the images over email! One time its fine! Again and Again its a pain.
So we have the API. Request as many outputs no limits on our Maritme API.

Our Maritime API will take 13 images as input and output a set of 12 Image arrays. These are predictions of next one hour of images

Our API Documentation: https://documenter.getpostman.com/view/5665918/UVyn1JLo

and make some requests

New to API and dont know how to access it? Sit tight from here on we will explain you in detail everything

1) In API we have endpoints, endpoint is same as a "door" to something
We have 4 Endpoints(gates)

a) /nowcast_results/forecast/

Description: This endpoint will help you forecast next one hour of weather images depending on the input time and location you give it in the input parameters.

Note: Model and index in this parameters are optional. But you can give 

Input Parameters: 
    -- begin_location: City Name
    -- begin_yearmonth: Year-Month
    -- begin_day: Day
    -- begin_time : Time
    -- model: 
    -- index (Optional):

b) /nowcast_results/forecast/latlong/

Description: This endpoint will help you forecast next one hour of weather images depending on the input latitude, longitude and distance you give it in the input parameters.
Input parameters:
    -- lat: Latitude
    -- lon: Longitude
    -- distance: Distance value to predict the weather for the nearest loicat
    -- model:
    -- index(Optional): 
