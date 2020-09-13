import requests
import random
import time

StartId = 100000 # The ID you want to start searching from
MaxId = 1000000 # The max ID, group ID's will not be searched past this number

def search():
    Group = random.randint(StartId, MaxId)
    
    GetRequest = requests.get("https://groups.roblox.com/v1/groups/" + str(Group))
    JsonResponse = GetRequest.json()
    
    if GetRequest.status_code != 429:
        if JsonResponse["owner"] == None and JsonResponse["publicEntryAllowed"] == True:
            print("Group found! ID: " + str(Group))
    elif GetRequest.status_code == 429:
        print("Too many requests, waiting five seconds...")
        time.sleep(5)
    
while True:
    search()
