import os
from django.shortcuts import render 
# import json to load json data to python dictionary 
import json 
# urllib.request to make a request to api 
import urllib.request 
import datetime
import requests
from django.conf import settings

  
  
def index(request): 
    if request.method == 'POST': 
        city = request.POST['city'] 
        ''' api key might be expired use your own api_key 
            place api_key in place of appid ="your_api_key_here "  '''
  
        # source contain JSON data from API 
        my_secret = "YOUR_API_KEY_HERE"

        source = ('http://api.openweathermap.org/data/2.5/weather?&appid='+my_secret+'&q='+city)
        source1 =source.replace(" ","+")
        source2 = urllib.request.urlopen(source1).read()



        # converting JSON data to a dictionary 
        list_of_data = json.loads(source2) 
        time=int(list_of_data['dt'])
        sunrise1=int(list_of_data['sys']['sunrise'])
        sunset1=int(list_of_data['sys']['sunset'])
        ico=str(list_of_data['weather'][0]['icon'])

        # data for variable list_of_data 
        data = { 
            "country_code": str(list_of_data['sys']['country']), 
            "coordinate": str(list_of_data['coord']['lon']) + ' E '
                        + str(list_of_data['coord']['lat']) + ' N', 
            "temp": round(list_of_data['main']['temp']-273) , 
            "pressure": str(list_of_data['main']['pressure'])+' hPa', 
            "humidity": str(list_of_data['main']['humidity'])+ ' %',
            "des": str(list_of_data['weather'][0]['main']),
            "nam":str(list_of_data['name']),
            "max_temp": round(list_of_data['main']['temp_max']-273) , 
            "min_temp": round(list_of_data['main']['temp_min']-273) , 
            "tempf": round(list_of_data['main']['feels_like']-273) ,
            "wind": str(list_of_data['wind']['speed']),
            "deg":str(list_of_data['wind']['deg']),
            #"tempf": round(list_of_data['main']['feels_like']-273)
            "cloud":str(list_of_data['clouds']['all']),
            "timef":datetime.datetime.fromtimestamp(time),
            "sunrise2":datetime.datetime.fromtimestamp(sunrise1),
            "sunset2":datetime.datetime.fromtimestamp(sunset1),
            "ico1": "http://openweathermap.org/img/wn/"+ico+"@2x.png",
            "visibility":str(list_of_data['visibility']),

        } 

        #print(data) 
    else: 
        data ={} 
    return render(request, "main/index1.html", data) 
def error_404(request , exception ):
        data = {}
        return render(request,'main/error_404.html', data)

def error_500(request):
        data = {}
        return render(request,'main/error_500.html', data)
def extra_context(request):
    return {'base_url': settings.BASE_URL}
