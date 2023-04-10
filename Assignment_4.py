#1
import requests

url = "https://api.github.com/users/avielb/repos"
response = requests.get(url)

if response.status_code == 200:
    repos = response.json()
    count = len(repos)
    if count >= 5:
        print(f"{count} repositories exist.")
    else:
        print(f"Only {count} repositories exist.")
else:
    print("Error fetching repositories.")

#2
import requests
import random

names = ["Alon", "David", "Moshe"]
age_range = range(0, 121)

for name in names:
    url = f"https://api.agify.io/?name={name}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        age = data["age"]
        if age in age_range:
            print(f"The age of {name} is {age}.")
        else:
            print(f"Error: {name} age is not in range.")
    else:
        print(f"Error fetching age for {name}.")
#3

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

#4
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.ycombinator.com/")
if driver.title == "Y Combinator":
    print("Title working")
else:
    print("Title for ycombinator.com is not working")
driver.quit()

#5
driver = webdriver.Chrome()
driver.get("https://hub.docker.com/")
assert driver.title == "Docker Hub Container Image Library | App Containerization"
print("Title for hub.docker.com is not working")
driver.quit()
