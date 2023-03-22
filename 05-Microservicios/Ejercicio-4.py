import requests
#from datetime import datetime
#import time

url= "https://openapi.emtmadrid.es/v1/mobilitylabs/user/login"

myheaders={"X-ClientID": "cbbba1b0-9bf0-440e-8d82-ef2cdba45eed","passKey": "E50ECCA4EBD615519B3E8F8C7197F7203B9386011C2A10046D732434BA4220538F809F5B2FA7D542CD66EBEAD8004E938C3DF036C23C3EA1355A906C035460C8", }
try:

    response = requests.get(url, headers=myheaders)
    if (response.status_code == 200):
        data = response.json()
        print(data)
        
    else:
        print(f"Error:", response.reason)

except Exception as err:
    print(f"Error: {err}")

















exit()

#stop_id=input("Parada?: ")
url = "https://openapi.emtmadrid.es/v2/transport/busemtmad/stops/888/arrives/"


myheaders = {"accessToken": "f5f9990e-c6f3-11ed-a34b-02dc46d0efe2",'Content-Type': 'application/json'}


"""
body = {

    "cultureInfo": "ES",

    "Text_StopRequired_YN": "Y",

    "Text_EstimationsRequired_YN": "Y",

    "Text_IncidencesRequired_YN": "Y",

    "DateTime_Referenced_Incidencies_YYYYMMDD": datetime.now().strftime('%Y%m%d')

}


response= requests.get(url, headers=myheaders)
if (response.status_code == 200):
        data = response.json()
        print(data)
else:
        print(f"Error:", response.reason)
#response = requests.post(url=url.format(stop_id=stop_id), headers=myheaders, json=body)
"""