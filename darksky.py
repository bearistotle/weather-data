import requests
import json
from requests.exceptions import HTTPError
import argparse
import gen_requests

def main():

    # add args to arg parser; parse args from cml; create dict from parsed args
    parser = argparse.ArgumentParser(description="Get weather data for all days between two dates and write it to the given file.")
    parser.add_argument("csv_file", type=str, help="The csv file to which the data should be written.")
    parser.add_argument("moStart", type=int, help="The month of the first date for which data is desired (MM format).")
    parser.add_argument("dayStart", type=int, help="The day of the first date for which data is desired (DD format).")
    parser.add_argument("yrStart", type=int, help="The year of the first date for which data is desired (YYYY format).")
    parser.add_argument("moEnd", type=int, help="The month of the last date for which data is desired (MM format).")
    parser.add_argument("dayEnd", type=int, help="The day of the last date for which data is desired (DD format).")
    parser.add_argument("yrEnd", type=int, help="The year of the last date for which data is desired (YYYY format).")
    args = parser.parse_args()
    args_dict = vars(args)

    download_dir = args_dict["csv_file"]
    with open(download_dir,"w") as csv:
        column_titles = "Date,Actual High,Actual Low,Felt High,Felt Low,Summary\n"
        csv.write(column_titles)


    # init start and end vars from args_dict
    yr_start = args_dict["yrStart"]
    yr_end = args_dict["yrEnd"]
    mo_start = args_dict["moStart"]
    mo_end = args_dict["moEnd"]

    # loop through years, months, days requesting each day. Structure: If start, begin at
    # start val; elif end, stop at end val; else, start at 1 and loop through all.
    yr_int = yr_start
    mo_int = mo_start
   
    if yr_start != yr_end:

        for year in range(0, yr_end - yr_start + 1):

            if yr_int == yr_start:

                for month in range(mo_start, 13):

                    if mo_int == mo_start:
                        gen_requests.first_month_requests(args_dict, mo_int, yr_int)

                    elif mo_int == mo_end:
                        gen_requests.last_month_requests(args_dict, mo_int, yr_int)

                    else:
                        gen_requests.middle_month_requests(args_dict, mo_int, yr_int)

                    mo_int += 1

            elif yr_int == yr_end:

                mo_int = 1
                if mo_int == mo_end:
                    gen_requests.last_month_requests(args_dict, mo_int, yr_int)

                else:
                    for month in range(1, 13):
                        gen_requests.middle_month_requests(args_dict, mo_int, yr_int)
                        mo_int += 1

            else:
                mo_int = 1
                for month in range(1, 13):
                    gen_requests.middle_month_requests(args_dict, mo_int, yr_int)
                    mo_int +=1

            yr_int += 1

    else:
        for month in range(mo_start, mo_end + 1):

            if mo_int == mo_start:
                gen_requests.first_month_requests(args_dict, mo_int, yr_int)


            elif mo_int == mo_end:
                gen_requests.last_month_requests(args_dict, mo_int, yr_int)

            else:
                gen_requests.middle_month_requests(args_dict, mo_int, yr_int)

            mo_int += 1

if __name__ == "__main__":
    main()
