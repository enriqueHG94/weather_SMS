# **weather_SMS**
This project uses the WeatherAPI and Twilio API to send an SMS with the weather forecast for a specific location to a mobile phone number.
## **Requirements**
To run this project, you will need the following Python packages installed:

- twilio==7.14.0
- pandas==1.3.4
- requests==2.22.0
- tqdm==4.62.3

You will also need to have a Twilio account and a WeatherAPI API key.
## **Configuration**
Before running the main script, you will need to configure your Twilio and WeatherAPI credentials in the twilio_config.py file. Make sure to replace the values of the variables TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, PHONE_NUMBER and API_KEY_WAPI with your own credentials.
You will also need to add your phone number to the end of the utils.py file.
## **Execute**
To run the main script, open a terminal and navigate to the directory where the project is located. Then, run the following command:

python twilio_script.py

If everything is configured correctly, you should receive a message on your mobile phone with the weather forecast for the location specified in the script.
## **Customisation**
You can customise the main script to change the location for which you want to get the weather forecast, or to modify the message that is sent to your mobile. To do this, open the twilio_script.py file and modify the variables and functions as needed.
