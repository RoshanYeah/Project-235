import requests

for i in range(1,5000):
    url_ID = f"http://ec2-3-108-196-161.ap-south-1.compute.amazonaws.com/api/get-customer?id={i}"
    request = requests.get(url=url_ID)
    if request.status_code == 200:
        print(url_ID)