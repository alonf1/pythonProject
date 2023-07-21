#tests

import requests

url = "http://universities.hipolabs.com/search?country=Israel"
response = requests.get(url)

if response.status_code == 200:
    universities = response.json()
    count = len(universities)
    if count >= 5:
        print(f"{count} universities in Israel.")
    else:
        print(f"Only {count} universities in Israel.")
else:
    print("Error fetching universities.")
print(universities)
