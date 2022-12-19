import os
from time import sleep, time
from random import random
from discord_layer.discord_layer import DiscordProxy

from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler

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



def start_loop():
    scheduler = BackgroundScheduler()
    scheduler.add_job(loop, 'interval', minutes=0)
    scheduler.start()
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        # This is here to simulate application activity (which keeps the main thread alive).
        while True:
            sleep(2)
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        scheduler.shutdown()


def loop():
    print("starting loop")
    proxy = DiscordProxy()
    while not retrieve_messages(proxy):
        sleep_num = 3.5 + random()
        print("sleeping for " + str(sleep_num))
        sleep(sleep_num)
        fish(proxy)

# fish()
# retrieve_messages()