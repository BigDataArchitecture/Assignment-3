Assignment3
==============================

Creating FASTApi for Maritime Nowcasting

Lets do some basics first! 

Why is API required?
Well, API allows us to share our results with the world in easier way!
Imagine you running the the SEVIR model and sharing the images over email! One time its fine! Again and Again its a pain.
So we have the API. Request as many outputs no limits on our Maritme API.

Our Maritime API will take inputs and output you set of 12 Image arrays. This are predictions of next one hour of images

How to Access our API?
You can go to out API link: 

and make some requests

New to API and dont know how to access it? Sit tight from here on we will explain you in detail everything

1) In API we have endpoints, endpoint is same as a "door" to something
We have 4 Endpoints(gates)
a) /nowcast_results/forecast/

Description: This endpoint will help you forecast next one of weather images depending on the input time and location you give it in the input parameters.

Note: Model and index in this parameters are optional. But you can give 

Input Parameters: 
    -- begin_location: City Name
    -- begin_yearmonth: Year-Month
    -- begin_day: Day
    -- begin_time : Time
    -- model (Optional): 
    -- index (Optional)

b) /nowcast_results/forecast/latlong/
Sample Input:


c) /nowcast_results/backtest/
d) /nowcast_results/backtest/latlong/
