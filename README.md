##Calculate Sunrise and Sunset times.

The python script is intended to be used as a cgi script and accepts a json object containing at a minimum the longitude and latitude
and returns a json object containing the sunrise and sunset times based on the location provided.

A sample front-end is provided which uses the HTML5/javascript location functions to retrieve a devices location,
submit it to the python script and display the result in a human friendly format.

##Input.

As input this script accepts the following:

- location(Reguired):
a JSON object with one of the following formats:
```
{
	"latitude":(LATITUDE),
	"Longitude":(LONGITUDE),
	"altitude"(ALTITUDE)
}
```
or
```
{
	"latitude":(LATITUDE),
	"Longitude":(LONGITUDE),
}
```

##Response:
The response from this object is either an http error code or a JSON object of the following format:

```
-Date(optional):
a JSON object with one of the following formats:
```
{
	"Date":"YYYY-MM-DD"
}
```

To compute sunrise and sunset times for a date other than the current one.

{
	"is_daylight":(true|false),
	"previous_sunrise":(DateTime of previous sunrise),
	"next_sunrise":(DateTime of next sunrise),
	"previous_sunset":(DateTime of previous sunset),
	"next_sunset":(DateTimeof next sunset)
}
```


#####Resuirements:
- pyephem
