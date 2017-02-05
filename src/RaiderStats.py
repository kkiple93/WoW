# -*- coding: utf-8 -*- need this encoding because Teria is alt code boi
__author__ = 'Kyle'

import requests, blizzKey

def getRaiderStats(realm, user, playerObject, playerList,maxSeen):
    url = "https://us.api.battle.net/wow/character/%s/%s?fields=stats&locale=en_US" % (realm, user)
    url += blizzKey.getKey()
    req = requests.get(url)

    print("Request Status Code for %s: %d") % (user,req.status_code)
    if(req.status_code == 200):
        print(req.json())
        val = req.json()['stats']



def main(playerList, playerObject):
    maxSeen = 0
    getRaiderStats("Alexstrasza", "Wickedsoul", playerObject, playerList,maxSeen)
    getRaiderStats("Alexstrasza", "Bagnar", playerObject, playerList,maxSeen)
    getRaiderStats("Alexstrasza", "Problim", playerObject, playerList,maxSeen)
    getRaiderStats("Terokkar", "Drx", playerObject, playerList,maxSeen)
    getRaiderStats("Alexstrasza", "Divr", playerObject, playerList,maxSeen)
    getRaiderStats("Alexstrasza", "Sythera", playerObject, playerList,maxSeen)
    getRaiderStats("Terokkar", "Zaxvriin", playerObject, playerList,maxSeen)
    getRaiderStats("Alexstrasza", "Soothing", playerObject, playerList,maxSeen)
    getRaiderStats("Alexstrasza", "Ragdas", playerObject, playerList,maxSeen)
    getRaiderStats("Alexstrasza", "Onemanaleft", playerObject, playerList,maxSeen)
    getRaiderStats("Alexstrasza", "Valanadria", playerObject, playerList,maxSeen)
    getRaiderStats("Alexstrasza", "Applejuice", playerObject, playerList,maxSeen)
    getRaiderStats("Alexstrasza", "Arroo", playerObject, playerList,maxSeen)
    getRaiderStats("Alexstrasza", "Azavia", playerObject, playerList,maxSeen)
    getRaiderStats("Alexstrasza", "Beckintailz", playerObject, playerList,maxSeen)
    getRaiderStats("Alexstrasza", "Dalkx", playerObject, playerList,maxSeen)
    getRaiderStats("Alexstrasza", "Hyuna", playerObject, playerList,maxSeen)
    getRaiderStats("Alexstrasza", "Newaayy", playerObject, playerList,maxSeen)
    getRaiderStats("Alexstrasza", "Nzx", playerObject, playerList,maxSeen)
    getRaiderStats("Alexstrasza", "Roiid", playerObject, playerList,maxSeen)
    getRaiderStats("Alexstrasza", "Travincal", playerObject, playerList,maxSeen)
    getRaiderStats("Alexstrasza", "Téria", playerObject, playerList,maxSeen)
    getRaiderStats("Alexstrasza", "Vladiri", playerObject, playerList,maxSeen)
    getRaiderStats("Alexstrasza", "Cyvusz", playerObject, playerList,maxSeen)