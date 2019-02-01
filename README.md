# Daytime

This application is a set of AWS lambda functions and SAM/CloudFormation
configuration for a simple API/SPA that returns the sunrise and sunset times
for a specific location on a specific date.

## API Overview.

|method|endpoint|querystring|
|---|---|---|
|GET|/sunrise|latitude= longtitude= [altitude=]|

