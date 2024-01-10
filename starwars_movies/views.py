from django.shortcuts import render
import requests

# Create your views here.
def myview(request):
    return render(request, "index.html")

def starwars_data(request):
    api_url='https://swapi.dev/api/films'
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()
        return render(request, "index.html", {'starwars_data': data})
    else:
        return render(request, 'myapp_starwars/error_template.html')
