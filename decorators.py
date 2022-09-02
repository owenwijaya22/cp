url = f'https://graph.microsoft.com/v1.0/me/todo/lists'
import requests
r = requests.get(url)
app_name = 'Graph Python quick start'
client_id = '3f5d5010-7a49-4cef-b8ab-7ccf918f0443'
print(r.status_code)