from tqdm import tqdm
from twilio_config import twilio_account_sid, twilio_auth_token, api_key_wapi
from utils import request_wapi, get_forecast, create_df, send_message, get_date

'''This script uses the WeatherAPI and Twilio to send an SMS
 with the weather forecast for a specific location to a mobile phone.
'''


query = 'London'
api_key = api_key_wapi

# Get the current date in the format "YYYY-MM-DD"
input_date = get_date()

# Make a request to the WeatherAPI to get the weather forecast for the specified location
response = request_wapi(api_key, query)


data = []

for i in tqdm(range(24), colour='green'):
    data.append(get_forecast(response, i))

df_rain = create_df(data)

# Send Message
message_id = send_message(twilio_account_sid, twilio_auth_token, input_date, df_rain, query)

print('Message sent successfully' + message_id)
