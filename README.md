# cowin_vaccine_availability_tracker
A basic Python script that can show vaccine availability based on the pincode you enter. 

I have created a basic python script that can get info about the vaccine availability in your area , It can also show the details for upto 7 days based on your input and the script you select

I have two versions of the script
1. **Cowin_Dist.py** : This script will run until it finds a centre and alerts it using tkinter. This tracker is based on the district code (District code is available at a CSV file named **district.csv**). Change the **ENTER_VACCINE_NAME (LINE 20) to the vaccine name** that you are searching.
2. **cowin_pincode.py** : This file will run continuously and will print the details based on the pincode that you enter.

I am working on a GUI version of this Script to make the script more attractive and user friendly.

Library used 
* Requests 
* Json
* datetime

Script 2 will give the following information:
* Pincode of the centre
* Date of the Vaccine
* Centre Name
* Number of vaccine's Available
* Vaccine Type
* Minimum Age limit


Fell free to email me at ashwin3082002@gmail.com if you have any doubts.
