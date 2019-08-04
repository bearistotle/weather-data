import requests
import json
from requests.exceptions import HTTPError

with open("credentials.json") as creds_json:
    creds_dict = json.load(creds_json)
    API_KEY = creds_dict["creds"]["API_KEY"]
    API_HOST = creds_dict["creds"]["API_HOST"]

latitude = "38.627003"
longitude = "-90.199402"
mo_length = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30,
    10: 31, 11: 30, 12: 31}
hour = "12"
minute = "00"
second = "00"

def first_month_requests(args_dict, mo_int, yr_int):

    # init start and end vars from args_dict
    download_dir = args_dict["csv_file"]
    day_int = args_dict["dayStart"]

    if args_dict["moStart"] != args_dict["moEnd"]:

        for day in range(day_int, mo_length[mo_int] + 1):
            
            if mo_int < 10:

                if day_int < 10:
                    time = f"{yr_int}-0{mo_int}-0{day_int}T{hour}:{minute}:{second}"

                else:
                    time = f"{yr_int}-0{mo_int}-{day_int}T{hour}:{minute}:{second}"
            
            else:
                time = f"{yr_int}-{mo_int}-{day_int}T{hour}:{minute}:{second}"

            url = f"https://dark-sky.p.rapidapi.com/{latitude},{longitude},{time}"

            try:
                response = requests.get(url, headers={
                    "X-RapidAPI-Host": f"{API_HOST}",
                    "X-RapidAPI-Key" : f"{API_KEY}"
                    }
                )
                response.raise_for_status()
            except HTTPError as http_err:
                print(f"HTTP Error occured: {http_err}")
            except Exception as err:
                print(f"Other error occurred: {err}")
            else:
                json_response = response.json()
                date = f"{mo_int}/{day_int}/{yr_int}"
                high_temp = json_response["daily"]["data"][0]["temperatureHigh"]
                low_temp = json_response["daily"]["data"][0]["temperatureLow"]
                felt_high = json_response["daily"]["data"][0]["apparentTemperatureHigh"]
                felt_low = json_response["daily"]["data"][0]["apparentTemperatureLow"]
                summary = json_response["daily"]["data"][0]["summary"]
                
                # Write the results of each request to a line in a .csv file
                with open(download_dir,"a") as csv:
                    row = f"{date},{high_temp},{low_temp},{felt_high},{felt_low},{summary}\n"
                    csv.write(row)

            day_int += 1
    else:
        for day in range(day_int, args_dict["dayEnd"] + 1):
            
            if mo_int < 10:

                if day_int < 10:
                    time = f"{yr_int}-0{mo_int}-0{day_int}T{hour}:{minute}:{second}"

                else:
                    time = f"{yr_int}-0{mo_int}-{day_int}T{hour}:{minute}:{second}"
            
            else:
                time = f"{yr_int}-{mo_int}-{day_int}T{hour}:{minute}:{second}"

            url = f"https://dark-sky.p.rapidapi.com/{latitude},{longitude},{time}"

            try:
                response = requests.get(url, headers={
                    "X-RapidAPI-Host": f"{API_HOST}",
                    "X-RapidAPI-Key" : f"{API_KEY}"
                    }
                )
                response.raise_for_status()
            except HTTPError as http_err:
                print(f"HTTP Error occured: {http_err}")
            except Exception as err:
                print(f"Other error occurred: {err}")
            else:
                json_response = response.json()
                date = f"{mo_int}/{day_int}/{yr_int}"
                high_temp = json_response["daily"]["data"][0]["temperatureHigh"]
                low_temp = json_response["daily"]["data"][0]["temperatureLow"]
                felt_high = json_response["daily"]["data"][0]["apparentTemperatureHigh"]
                felt_low = json_response["daily"]["data"][0]["apparentTemperatureLow"]
                summary = json_response["daily"]["data"][0]["summary"]
                
                # Write the results of each request to a line in a .csv file
                with open(download_dir,"a") as csv:
                    row = f"{date},{high_temp},{low_temp},{felt_high},{felt_low},{summary}\n"
                    csv.write(row)

            day_int += 1

def last_month_requests(args_dict, mo_int, yr_int):
    
    download_dir = args_dict["csv_file"]
    day_end = args_dict["dayEnd"]
    day_int = 1

    for day in range(day_int, int(day_end) + 1):

        if mo_int < 10:

            if day_int < 10:
                time = f"{yr_int}-0{mo_int}-0{day_int}T{hour}:{minute}:{second}"

            else:
                time = f"{yr_int}-0{mo_int}-{day_int}T{hour}:{minute}:{second}"
        
        else:
            time = f"{yr_int}-{mo_int}-{day_int}T{hour}:{minute}:{second}"

        url = f"https://dark-sky.p.rapidapi.com/{latitude},{longitude},{time}"

        try:
            response = requests.get(url, headers={
                "X-RapidAPI-Host": f"{API_HOST}",
                "X-RapidAPI-Key" : f"{API_KEY}"
                }
            )
            response.raise_for_status()
        except HTTPError as http_err:
            print(f"HTTP Error occured: {http_err}")
        except Exception as err:
            print(f"Other error occurred: {err}")
        else:
            json_response = response.json()
            date = f"{mo_int}/{day_int}/{yr_int}"
            high_temp = json_response["daily"]["data"][0]["temperatureHigh"]
            low_temp = json_response["daily"]["data"][0]["temperatureLow"]
            felt_high = json_response["daily"]["data"][0]["apparentTemperatureHigh"]
            felt_low = json_response["daily"]["data"][0]["apparentTemperatureLow"]
            summary = json_response["daily"]["data"][0]["summary"]
            
            # Write the results of each request to a line in a .csv file
            with open(download_dir,"a") as csv:
                row = f"{date},{high_temp},{low_temp},{felt_high},{felt_low},{summary}\n"
                csv.write(row)

        day_int += 1

def middle_month_requests(args_dict, mo_int, yr_int):

    download_dir = args_dict["csv_file"]    
    day_int = 1

    for day in range(day_int, mo_length[mo_int] + 1):

        if mo_int < 10:

            if day_int < 10:
                time = f"{yr_int}-0{mo_int}-0{day_int}T{hour}:{minute}:{second}"

            else:
                time = f"{yr_int}-0{mo_int}-{day_int}T{hour}:{minute}:{second}"
        
        else:
            time = f"{yr_int}-{mo_int}-{day_int}T{hour}:{minute}:{second}"

        url = f"https://dark-sky.p.rapidapi.com/{latitude},{longitude},{time}"

        try:
            response = requests.get(url, headers={
                "X-RapidAPI-Host": f"{API_HOST}",
                "X-RapidAPI-Key" : f"{API_KEY}"
                }
            )
            response.raise_for_status()
        except HTTPError as http_err:
            print(f"HTTP Error occured: {http_err}")
        except Exception as err:
            print(f"Other error occurred: {err}")
        else:
            json_response = response.json()
            date = f"{mo_int}/{day_int}/{yr_int}"
            high_temp = json_response["daily"]["data"][0]["temperatureHigh"]
            low_temp = json_response["daily"]["data"][0]["temperatureLow"]
            felt_high = json_response["daily"]["data"][0]["apparentTemperatureHigh"]
            felt_low = json_response["daily"]["data"][0]["apparentTemperatureLow"]
            summary = json_response["daily"]["data"][0]["summary"]
            
            # Write the results of each request to a line in a .csv file
            with open(download_dir,"a") as csv:
                row = f"{date},{high_temp},{low_temp},{felt_high},{felt_low},{summary}\n"
                csv.write(row)

        day_int += 1
