import africastalking
import os
import csv

from dotenv import load_dotenv
from utils import format_phone_number

load_dotenv()

username = os.environ.get('AFRICASTAKLING_USERNAME')
api_key = os.environ.get('AFRICASTAKLING_API_KEY')
africastalking.initialize(username, api_key)
sms = africastalking.SMS


list_of_contacts = []

with open('contact_list.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        phone_number = format_phone_number(row[0])
        if phone_number is None:
            continue
        list_of_contacts.append(phone_number)

if len(list_of_contacts) > 0:
    response = sms.send("Here is your text message frm Arty", list_of_contacts)
    print(response)
