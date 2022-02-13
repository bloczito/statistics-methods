import requests
import json

token = "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIiwiaXNzIjoiaHR0cHM6Ly9kZXYtcC10aDlwcnEudXMuYXV0aDAuY29tLyJ9..hddpAUnoUiDBqybi.dMCvvTPk3hDsNvgTM9fBmuD_9MgQ82Fv3zCXBD5Mb8VQOLYACoRsmUsZ3fURnPp-AzMe7_4wnKWiA-BaZufr9_o_XdzD5hTL3a8yHc9t3RiNCL3_CUzjTKW273UHVo7TZrohH50eGU2qPp4ulgW90U97F6m1S1rX_FhFFjirq7bi4R5VG4bYLa_8puViSH79iXYf-U8Hb-Rt-e9gPrKootnuDadnsma0VppQOSXFYRv7FoXKVHsPmPmeegMONUW1Yr6EmsgP1GGzc7HDgvnWkF7Un1LVHl4zGezIaWAmy3yLoqXCmeMx8YmAGJC-zLXqzw.0eYA8pYMWJe1yNjqft1sGQ"
headers = {"Authorization": f"Bearer {token}"}

response = requests.get("https://dev-p-th9prq.us.auth0.com/userinfo", headers=headers)

print(json.dumps(response.json(), indent=4))

