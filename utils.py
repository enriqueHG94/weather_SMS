from datetime import datetime
import pandas as pd
import requests
from twilio.rest import Client
from twilio_config import phone_number


def get_date():
    input_date = datetime.now()
    input_date = input_date.strftime("%Y-%m-%d")

    return input_date


def request_wapi(api_key, query):
    url_weather = 'http://api.weatherapi.com/v1/forecast.json?key=' + api_key + '&q=' + query + ('&days=1&aqi=no'
                                                                                                 '&alerts=no')

    try:
        response = requests.get(url_weather).json()
        print(response)
    except Exception as e:
        print(e)
        return None

    return response


def get_forecast(response, i):
    date = response.get('forecast', {}).get('forecastday', [{}])[0].get('hour', [{}])[i].get('time', '').split()[0]
    hour = int(response.get('forecast', {}).get('forecastday', [{}])[0].get('hour',
                                                                            [{}])[i].get('time', '').split()[1].split(
        ':')[0])
    condition = response.get('forecast', {}).get('forecastday', [{}])[0].get('hour', [{}])[i].get('condition', {}).get(
        'text', '')
    temperature = response.get('forecast', {}).get('forecastday', [{}])[0].get('hour', [{}])[i].get('temp_c', '')
    rain = response.get('forecast', {}).get('forecastday', [{}])[0].get('hour', [{}])[i].get('will_it_rain', '')
    prob_rain = response.get('forecast', {}).get('forecastday', [{}])[0].get('hour', [{}])[i].get('chance_of_rain', '')

    return date, hour, condition, temperature, rain, prob_rain


def create_df(data):
    col = ['Date', 'Hour', 'Condition', 'Temperature', 'Rain', 'prob_rain']
    df = pd.DataFrame(data, columns=col)
    df = df.sort_values(by='Hour', ascending=True)

    df_rain = df[(df['Rain'] == 1) & (df['Hour'] > 6) & (df['Hour'] < 22)]
    df_rain = df_rain[['Hour', 'Condition']]
    df_rain.set_index('Hour', inplace=True)

    return df_rain


def send_message(twilio_account_sid, twilio_auth_token, input_date, df, query):
    account_sid = twilio_account_sid
    auth_token = twilio_auth_token

    client = Client(account_sid, auth_token)

    message_body = f"\nHi! \n\n\n The forecast for rain today {input_date} in {query} is : \n\n\n {df}"

    message = client.messages \
        .create(
        body=message_body,
        from_=phone_number,
        to='phone number'
    )

    return message.sid
