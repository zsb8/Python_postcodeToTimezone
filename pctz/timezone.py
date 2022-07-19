import re
import time
import json
dic_provinces = dict()
dic_provinces["A"] = {"name": "Newfoundland and Labrador", "time_zone": -3.5, "DST": 1, "special": 1}
dic_provinces["B"] = {"name": "Nova Scotia", "time_zone": -4, "DST": 1, "special": 0}
dic_provinces["C"] = {"name": "Prince Edward Island", "time_zone": -4, "DST": 1, "special": 0}
dic_provinces["E"] = {"name": "New Brunswick", "time_zone": -4, "DST": 1, "special": 0}
dic_provinces["G"] = {"name": "Quebec East", "time_zone": -5, "DST": 1, "special": 1}
dic_provinces["H"] = {"name": "Montreal Metropolitan", "time_zone": -5, "DST": 1, "special": 0}
dic_provinces["J"] = {"name": "Quebec West", "time_zone": -5, "DST": 1, "special": 0}
dic_provinces["K"] = {"name": "Eastern Ontario", "time_zone": -5, "DST": 1, "special": 0}
dic_provinces["L"] = {"name": "Central Ontario", "time_zone": -5, "DST": 1, "special": 0}
dic_provinces["M"] = {"name": "Toronto", "time_zone": -5, "DST": 1, "special": 0}
dic_provinces["N"] = {"name": "South-western Ontario", "time_zone": -5, "DST": 1, "special": 0}
dic_provinces["P"] = {"name": "Northern Ontario", "time_zone": -5, "DST": 1, "special": 0}
dic_provinces["R"] = {"name": "Manitoba", "time_zone": -6, "DST": 1, "special": 0}
dic_provinces["S"] = {"name": "Saskatchewan", "time_zone": -6, "DST": 0, "special": 0}
dic_provinces["T"] = {"name": "Alberta", "time_zone": -7, "DST": 1, "special": 0}
dic_provinces["V"] = {"name": "British Columbia", "time_zone": -8, "DST": 1, "special": 1}
dic_provinces["X"] = {"name": "Northwest Territories and Nunavut", "time_zone": -6, "DST": 1, "special": 1}
dic_provinces["Y"] = {"name": "Yukon Territory", "time_zone": -7, "DST": 0, "special": 0}

dic_special = dict()
dic_special["G0G 0B8"] = {"province": "Quebec East", "name": "BLANC SABLON", "time_zone": -4, "DST": 0}
dic_special["G0G 1C0"] = {"province": "Quebec East", "name": "BLANC SABLON", "time_zone": -4, "DST": 0}
dic_special["G4T"] = {"province": "Quebec East", "name": "Îles de la Madeleine", "time_zone": -4, "DST": 1}
dic_special["A0P"] = {"province": "Newfoundland and Labrador", "name": "Central Labrador", "time_zone": -3, "DST": 1}
dic_special["A2V"] = {"province": "Newfoundland and Labrador", "name": "Labrador City", "time_zone": -3, "DST": 1}
dic_special["A0R"] = {"province": "Newfoundland and Labrador", "name": "North/Western Labrador", "time_zone": -3, "DST": 1}
dic_special['X0A'] = {"province": "Nunavut", "name": "Outer Nunavut", "time_zone": -5, "DST": 1}
dic_special['X0B'] = {"province": "Nunavut", "name": "Central Nunavut", "time_zone": -7, "DST": 1}
dic_special['X0C'] = {"province": "Nunavut", "name": "Inner Nunavut", "time_zone": -6, "DST": 1}
# Coral Harbour is the only Nunavut community that does not observe daylight saving time, remaining on Eastern Standard Time year-round
dic_special['X0C 0C0'] = {"province": "Northwest Territories and Nunavut", "name": "Coral Harbour", "time_zone": -6, "DST": 0}
dic_special['X0E'] = {"province": "Northwest Territories", "name": "Central Northwest Territories", "time_zone": -6, "DST": 1}
dic_special['X0G'] = {"province": "Northwest Territories", "name": "Southwestern Northwest Territories", "time_zone": -6, "DST": 1}
dic_special['X1A'] = {"province": "Northwest Territories", "name": "Yellowknife", "time_zone": -6, "DST": 1}
dic_special['V1G'] = {"province": "British Columbia", "name": "Dawson Creek", "time_zone": -7, "DST": 0}  # V1G 3V8
dic_special['V0C'] = {"province": "British Columbia", "name": "Fort Nelson", "time_zone": -7, "DST": 0}
dic_special['V1J'] = {"province": "British Columbia", "name": "Fort St. John", "time_zone": -7, "DST": 0}


def check_valid(post_code):
    # Only accept 6/7 letter length. such as H1X3N9 or H1X 3N9
    pattern = r'^[ABCEGHJ-NPRSTVXY]\d[ABCEGHJ-NPRSTV-Z](\s)?\d[ABCEGHJ-NPRSTV-Z]\d$'
    search_obj = re.search(pattern, post_code, re.M | re.I)
    return search_obj


def judge_dst(post_code):
    # Judge whether it has daylight saving time zone or not
    first_letter = post_code[0]
    dst = dic_provinces[first_letter]["DST"]
    special = dic_provinces[first_letter]["special"]
    if special:
        if post_code in dic_special:
            dst = dic_special[post_code]["DST"]
        elif post_code[0:3] in dic_special:
            dst = dic_special[post_code[0:3]]["DST"]
    return dst


def get_time_zone(post_code):
    # Main program
    if isinstance(post_code, str):
        post_code = post_code.upper()
        if check_valid(post_code):
            first_letter = post_code[0]
            time_zone = dic_provinces[first_letter]["time_zone"]
            special = dic_provinces[first_letter]["special"]
            if special:
                if post_code in dic_special:
                    time_zone = dic_special[post_code]["time_zone"]
                elif post_code[0:3] in dic_special:
                    time_zone = dic_special[post_code[0:3]]["time_zone"]
            if judge_dst(post_code):
                if time.localtime().tm_isdst:
                    dict_result = {"Result": "Success",
                        "Time_zone": time_zone+1,
                        "Daylight saving time": "Yes",
                        "Region":  dic_provinces[first_letter]["name"],
                        "Remark": "This time_zone means the hours before UTC time. If on the second Sunday of March or on the first Sunday in November, diff DST effect today in diff time zone"
                    }
            else:
                dict_result = {"Result": "Success",
                               "Time_zone": time_zone,
                               "Daylight saving time": "Not",
                               "Region": dic_provinces[first_letter]["name"],
                               "Remark": "This time_zone means the hours before UTC time."
                               }
    else:
        dict_result = {"Result": "Failed",
                       "Remark": "Check the post code format failed."
                       }
    return json.dumps(dict_result, ensure_ascii=False)


if __name__ == '__main__':
    my_post_code = "H1X 3N9"
    json_result = get_time_zone(my_post_code)
    print(json_result)




