import requests, json
import base64

url = "https://id.cisco.com/oauth2/default/v1/token"

client_id = "client_id"  # Example client ID
client_secret = "client_secret"  # Example client secret



payload = "grant_type=client_credentials"
value = base64.b64encode(f'{client_id}:{client_secret}'.encode('utf-8')).decode('utf-8')
headers = {
    "Accept": "*/*",
    "Content-Type": "application/x-www-form-urlencoded",
    "Authorization": f"Basic {value}"
}
token_response = requests.request("POST", url, headers=headers, data=payload)
token_data = token_response.json()
api_key = token_data.get('access_token')
print(api_key)
