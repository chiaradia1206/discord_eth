from requests import get
from matplotlib import pyplot as plt

API_KEY = "5FYPC6C5KPP9VJ1F1NKX34AESZBU624UIB"
BASE_URL = "https://api.etherscan.io/api"

def make_gas_api_url(module, action, **kwargs):
	url = BASE_URL + f"?module={module}&action={action}&apikey={API_KEY}"

	for key, value in kwargs.items():
		url += f"&{key}={value}"

	return url

get_balance_url = make_gas_api_url("gastracker", "gasoracle")
response = get(get_balance_url)
data = response.json()["result"]

for result in data
	SafeGasPrice = gas["SafeGasPrice"]
	ProposeGasPrice = gas["ProposeGasPrice"
	FastGasPrice = gas["FastGasPrice"]
	print("FastGasPrice:", FastGasPrice)
	print("ProposeGasPrice:", ProposeGasPrice)
	print("SafeGasPrice:", SafeGasPrice)