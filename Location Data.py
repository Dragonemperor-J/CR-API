import requests
import json

Locationid = input("Please put the Location ID, You can get it in Locations.json")

url = "https://api.clashroyale.com/v1/locations/" + Locationid

payload={}
headers = {
  'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjFkYmNmOTM0LWIxMWQtNDY1ZS05NzJiLThlZDBhNDVjODk2YSIsImlhdCI6MTYyMDQ2Njc3MCwic3ViIjoiZGV2ZWxvcGVyLzc4Yjk2MTliLWE2MmItZDMwYS02MDMzLWRlZDhiMzNhOWY2ZCIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyI0OS4zNi4xMDcuMjkiLCIxMjguMTI4LjEyOC4xMjgiLCI1NC44Ni41MC4xMzkiXSwidHlwZSI6ImNsaWVudCJ9XX0.w0IOz0Wlsl7PRg7yGIFOREGwnd2plrlk_YT0zjmQq5v8htFI_3Fvj8383A3EItklWQKgggDWZ1ni44P4QbFDJw'
}

response = requests.request("GET", url, headers=headers, data=payload)
Response = json.loads(response)
ParsedResponse = json.dumps(response)

print(ParsedResponse)
print(Response[ #write the data's header which's value you want])

