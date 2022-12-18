import requests 
import json
import os
from time import sleep
from random import random

class DiscordProxy():
    def __init__(self):
        print("initializing discord proxy")
        if "FISH_AUTH" in os.environ: 
           self.auth = os.getenv('FISH_AUTH')
        else:
            print("No Fishing Auth in env")

        self.retrieve_message_headers = {
            'authorization': self.auth
        }
        
        self.fish_headers = {
            'Content-Type': 'application/json',
            'authorization': self.auth
        }

        self.fish_payload = {
            'type': 2,
            'application_id': os.getenv('FISH_APPLICATION_ID'),
            'channel_id': os.getenv('FISH_CHANNEL_ID'),
            'guild_id': os.getenv('FISH_GUILD_ID'),
            'session_id': os.getenv('FISH_SESSION_ID'),
            'data': {
                'version': os.getenv('FISH_VERSION'),
                'id': os.getenv('FISH_ID'),
                'name': "fish",
                'type': '1',
                #'options': [],# [parameters] if parameters else [],
                #'application_command': '',# cmd_data,
                #'attachments': []
            },
        }


    def retrieve_messages(self):
        r = requests.get(f'https://discord.com/api/v9/channels/1042344356520149004/messages?limit=5', headers=self.retrieve_message_headers)

        return json.loads(r.text)

    def fish(self):
        print("fishing")

        r = requests.post(f'https://discord.com/api/v9/interactions', headers=self.fish_headers, json=self.fish_payload)


def retrieve_messages(proxy):
    verify = '**/verify**'


    ret = proxy.retrieve_messages()

    for value in ret:
        embed = value['embeds']
        if len(embed) > 0:
            first_embed = embed[0]
            if 'description' in first_embed:
                if verify in first_embed['description']:
                    print("You need to verify")
                    #print(first_embed['description'])
                    return True
                #print()
        # print(embed)
        # first
        # if verify in value['embeds'][0]['title']:
        #     print("THIS IS CAPATCHA MESSAGE")
        # print(value['embeds'], '\n')
        #print(value) 
        #print()

    return False
    
def fish(proxy):
    proxy.fish()



def loop():
    proxy = DiscordProxy()
    while not retrieve_messages(proxy):
        sleep_num = 3.5 + random()
        print("sleeping for " + str(sleep_num))
        sleep(sleep_num)
        fish(proxy)

# fish()
# retrieve_messages()