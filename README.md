##Calculate Sunrise and Sunset times.

The python script is intended to be used as a cgi script and accepts a json object containing at a minimum the longitude and latitude
and returns a json object containing the sunrise and sunset times based on the location provided.

A sample front-end is provided which uses the HTML5/javascript location functions to retrieve a devices location,
submit it to the python script and display the result in a human friendly format.


#####Resuirements:
- pyephem
