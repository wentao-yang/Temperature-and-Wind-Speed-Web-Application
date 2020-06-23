import requests
from flask import Flask, render_template, request

app = Flask(__name__)

# AerisWeather Access ID and Secret Key
client_id = 'ENTERYOURIDHERE'
client_secret = 'ENTERYOURSECRETKEYHERE'


@app.route('/wind_speed', methods=['POST'])
def get_speed():
    '''Requests the weather data from AerisWeather at a zip code, finds the wind speed, and returns wind_speed.html.'''
    zip_code = request.form['zip']

    try: 
        # Requests the weather data, which gives a json object, and finds the data for wind speed
        req = requests.get(
            'http://api.aerisapi.com/observations/' + zip_code + '?client_id=' + client_id +
            '&client_secret=' + client_secret)
        json_object = req.json()
        wind_speed = float(json_object['response']['ob']['windKTS'])

        return render_template('wind_speed.html', wind=wind_speed, zipcode=zip_code)
    except:
        return render_template('error.html')


@app.route('/get_wind_speed')
def req_speed():
    '''Returns get_wind_speed.html.'''
    return render_template('get_wind_speed.html')


@app.route('/temperature', methods=['POST'])
def get_temp():
    '''Requests the weather data from AerisWeather at a zip code, finds the temperature, and returns
    temperature.html. '''
    zip_code = request.form['zip']

    try:
        # Requests the weather data, which gives a json object, and finds the data for temperature
        req = requests.get(
            'http://api.aerisapi.com/observations/' + zip_code + '?client_id=' + client_id +
            '&client_secret=' + client_secret)
        json_object = req.json()
        temperature = float(json_object['response']['ob']['tempF'])

        return render_template('temperature.html', temp=temperature, zipcode=zip_code)
    except:
        return render_template('error.html')


@app.route('/get_temperature')
def req_temp():
    '''Returns get_temperature.html.'''
    return render_template('get_temperature.html')


@app.route('/home')
def home():
    '''Returns home.html.'''
    return render_template('home.html')


@app.route('/')
def index():
    '''Returns home.html.'''
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
