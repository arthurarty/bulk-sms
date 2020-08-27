import africastalking
import os
from dotenv import load_dotenv

username = os.environ.get('AFRICASTAKLING_USERNAME')
api_key = os.environ.get('AFRICASTAKLING_API_KEY')
africastalking.initialize(username, api_key)
sms = africastalking.SMS

response = sms.send("Here is your text message frm Arty", ['+256'])

print(response)
