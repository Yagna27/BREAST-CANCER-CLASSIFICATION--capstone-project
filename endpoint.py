import requests
import json

# URL for the web service, should be similar to:
# 'http://42e7f579-4b3d-4250-aee7-702d67e48ee5.southcentralus.azurecontainer.io/score'
scoring_uri = 'http://42e7f579-4b3d-4250-aee7-702d67e48ee5.southcentralus.azurecontainer.io/score'
# If the service is authenticated, set the key or token
key = 'D0zGpcSmGMdVKuDLbKtPFoIZUwehwyYT'
# Two sets of data to score, so we get two results back
data={"data": 
    [{
        "Age": 46, 
        "BMI": 33.18, 
        "Glucose": 92, 
        "Insulin": 5.75, 
        "HOMA": 1.304866667, 
        "Leptin": 18.69, 
        "Adiponectin": 9.16, 
        "Resistin": 8.89, 
        "MCP.1": 209.19},
    {
        "Age": 58, 
        "BMI": 29.15451895, 
        "Glucose": 139, 
        "Insulin": 16.582, 
        "HOMA": 5.685415067, 
        "Leptin": 22.8884, 
        "Adiponectin": 10.26266, 
        "Resistin": 13.97399, 
        "MCP.1": 923.886},
    {
        "Age": 44, 
        "BMI": 27.88761707, 
        "Glucose": 99, 
        "Insulin": 9.208, 
        "HOMA": 2.2485936, 
        "Leptin": 12.6757, 
        "Adiponectin": 5.47817, 
        "Resistin": 23.03306, 
        "MCP.1": 407.206}]}
input_data = json.dumps(data)
with open("data.json", "w") as _f:
    _f.write(input_data)

# Set the content type
headers = {'Content-Type': 'application/json'}
# If authentication is enabled, set the authorization header
headers['Authorization'] = f'Bearer {key}'

# Make the request and display the response
resp = requests.post(scoring_uri, input_data, headers=headers)
print(resp.json())