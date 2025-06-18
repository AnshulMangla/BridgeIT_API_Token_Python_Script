# !pip install openai 
import os
from openai import AzureOpenAI

message_with_history = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello, who won the last FIFA World Cup?"}
]
 
client = AzureOpenAI(
  azure_endpoint = 'https://chat-ai.cisco.com', 
  api_key="api_key",  
  api_version="2024-08-01-preview"
)

app_key = "app_key"
 
response = client.chat.completions.create(
    model="gpt-4o-mini", # model = "deployment_name".
    messages=message_with_history,
    user=f'{{"appkey": "{app_key}"}}'
)
print(response.choices[0].message.content)
