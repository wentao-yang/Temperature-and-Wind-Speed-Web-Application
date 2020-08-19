# Temperature and Wind Speed Web App [![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

A web application using Flask that returns the temperature and wind speed and their forecasts given the zip code by calling to the AerisWeather API.

## Getting Started

First, make sure that your [AerisWeather](https://www.aerisweather.com/) subscription is up and running. Then, clone this repository.

```
> git clone https://github.com/wentao-yang/Temperature-and-Wind-Speed-Web-Application.git
```

Next, open ```application.py``` with a text editor and find this section:

```
# AerisWeather Access ID and Secret Key
client_id = 'ENTERYOURIDHERE'
client_secret = 'ENTERYOURSECRETKEYHERE'
```

Input your Access ID and Secret Key in the appropriate location. Make sure that the ID and Key are between their respective apostrophe pairs. 

## Launching the Web App

Check that all packages from ```requirements.txt``` are installed:

```
> pip3 install -r requirements.txt
```

Then, open your command prompt/terminal in this directory and enter:

```
> python3 application.py
```

You can go to a web browser and go to ```http://localhost:5000/``` to use the web application.

## Deploying on Cloud Servers

I have successully deploy this web application on AWS using Elastic Beanstalk. Here is the [Guide from AWS](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/GettingStarted.CreateApp.html) that I followed.