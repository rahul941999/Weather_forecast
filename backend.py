import requests

API_KEY = "52dbc1fb7330af3988e3670bd8ae8e56"


def get_data(name, days, kind):
    url = (f"http://api.openweathermap.org/data/2.5/forecast?q={name}"
           f"&appid={API_KEY}&units=metric")
    response = requests.get(url=url)
    data = response.json()
    filtered_data = data["list"][:8*days]
    data_dates = []
    final_data = []

    if kind == "Temperature":
        for item in filtered_data:
            final_data.append(str(item["main"]["temp"]))
            data_dates.append(str(item["dt_txt"]))
        # final_data = [item["main"]["temp"] for item in filtered_data]
    else:
        for item in filtered_data:
            final_data.append(str(item["weather"][0]['main']))
            data_dates.append(str(item["dt_txt"]))
        # final_data = [item["weather"][0]["description"] for item in filtered_data]
    return final_data, data_dates


if __name__ == "__main__":
    print(get_data("Delhi", 3, "Sky"))
