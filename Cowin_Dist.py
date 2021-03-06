from tkinter.constants import E
import requests
import time
from tkinter import messagebox
dist = 571                   #Enter District Code (Refer district.csv for District Code)
date = '14-06-2021'          #Enter the Date
URL = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={}&date={}'.format(
    dist, date)

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}


def findAvailability():
    counter = 0
    result = requests.get(URL, headers=header)
    response_json = result.json()
    data = response_json["sessions"]
    for each in data:
        #Change ENTER_VACCINE_NAME to the vaccine that you are searching for.
        if((each["available_capacity_dose2"] > 0) & (each["min_age_limit"] == 18) and (each["vaccine"] == "ENTER_VACCINE_NAME")):
            counter += 1
            print(each["name"])
            est=each["name"]
            print(each["pincode"])
            print(each["vaccine"])
            print(each["available_capacity_dose2"])
            messagebox.showinfo("INFO", "Vaccine Found at:  "+est)
        
    if(counter == 0):
        print("No Available Slots")
        return False


while(findAvailability() != True):
    time.sleep(5)
    findAvailability()
