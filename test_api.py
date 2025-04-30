import requests

url = 'http://127.0.0.1:5000/predict'  # Assuming local Flask server is running
data = {
    "features": [0,	0,	1,	1,	42,	1,	0,	1,	0,	0,	0,	0,	2,	0,	0,	1,	1,	77.95,	3384

]
}

response = requests.post(url, json=data)
print(response.json())
