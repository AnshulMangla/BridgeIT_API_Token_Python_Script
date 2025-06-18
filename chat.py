# !pip install openai 
import os
from openai import AzureOpenAI

message_with_history = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello, who won the last FIFA World Cup?"}
]
 
client = AzureOpenAI(
  azure_endpoint = 'https://chat-ai.cisco.com', 
  api_key="eyJraWQiOiJYYmZSeTktVmNqc0hHSUJDcVcySUVrMmtwdGhPcXFZVHdVdkJmQzJ5b2ljIiwiYWxnIjoiUlMyNTYifQ.eyJ2ZXIiOjEsImp0aSI6IkFULktQWEdrZERUNmZEdkV2SEc3bTdDc1V3bUh6Tnl2TFBnWVJBSzVkNDVadXciLCJpc3MiOiJodHRwczovL2lkLmNpc2NvLmNvbS9vYXV0aDIvZGVmYXVsdCIsImF1ZCI6ImFwaTovL2RlZmF1bHQiLCJpYXQiOjE3NTAxNjE4MDYsImV4cCI6MTc1MDE2NTQwNiwiY2lkIjoiMG9hcDBlaTBwZmRoTXR1V2U1ZDciLCJzY3AiOlsiY3VzdG9tc2NvcGUiXSwic3ViIjoiMG9hcDBlaTBwZmRoTXR1V2U1ZDciLCJhenAiOiIwb2FwMGVpMHBmZGhNdHVXZTVkNyJ9.iAL8BWSdBf2YoBboTktAsbzAjD3aVluz6DFxkH8JmCY-oQ5okLGI_tnWh9cZUP2zSg-hxroa9_ccqPtYRQk59dg7HcCD9QuhaYSQOCqX57KSjykFr10ugXzH6mZisthh_DZXAUH5RYZkJsqqWjJk5KKjNRM3guOgZKztgYFqkMdaMWxHDGM2kGC04Ku_LcRcQn_OGC3CSIkTH-tER8nqPB2JWJLDA4OQa_vbP-Nn2SHhwrP7Vycj_goYeAT3LAH4yxiucnHzJ8GDwTtVDYCTxtWKzVX9NVjLfG2ySgspYSNYT0uQuWqNnGzm2FfhdGD3_1hQSVVFQgtKKon5H5E3CA",  
  api_version="2024-08-01-preview"
)

app_key = "egai-prd-cx-115058258-rag-1748607968194"
 
response = client.chat.completions.create(
    model="gpt-4o-mini", # model = "deployment_name".
    messages=message_with_history,
    user=f'{{"appkey": "{app_key}"}}'
)
print(response.choices[0].message.content)