from django.shortcuts import render
import requests
import json
from URL_Shortner.settings import TOKEN

# Create your views here.


def index(request):
    return render(request, "index.html")


def index_form(request):
    if request.method == "POST":
        long_url = request.POST.get("long_url")
        new_url = shorten_url(long_url)

        return render(request, "new_url.html", context={"url": new_url})
    return render(request, "index.html")


def shorten_url(url):
    print(TOKEN)
    headers = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}

    data_dict = {
        "long_url": url,
        "domain": "bit.ly",
        "group_guid": "Bo5s7obhBlB",
    }
    data = json.dumps(data_dict)

    response = requests.post(
        "https://api-ssl.bitly.com/v4/shorten", headers=headers, json=data_dict
    )

    response_dict = json.loads(response.text)

    print(response_dict)
    return response_dict["link"]
