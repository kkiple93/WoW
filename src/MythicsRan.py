# -*- coding: utf-8 -*-
__author__ = 'Kyle'
import requests, blizzKey


def getRaidersMythicsRan(realm, user, playerObject, playerList):
    url = "https://us.api.battle.net/wow/character/%s/%s?fields=achievements&locale=en_US" % (realm, user)
    #grab your developerKey - not giving you mine :p
    url += blizzKey.getKey()
    req = requests.get(url)
    print("Request Status Code for %s: %d") % (user,req.status_code)
    if(req.status_code == 200):
        val = req.json()
        #Grab the criteria Array
        criteriaIdArray = val["achievements"]["criteria"]
        criteriaQuantityArray = val["achievements"]["criteriaQuantity"]
        criteriaIndexObj = {}
        for i in range(len(criteriaIdArray)):
            if(criteriaIdArray[i] == 33096):
                criteriaIndexObj["33096"] = i
            elif(criteriaIdArray[i] == 33097):
                criteriaIndexObj["33097"] = i
            elif(criteriaIdArray[i] == 33098):
                criteriaIndexObj["33098"] = i
            elif(criteriaIdArray[i] == 32028):
                criteriaIndexObj["32028"] = i
        if(criteriaIndexObj.get("33096", "Empty") != "Empty"):
            criteriaIndexObj["33096"] = criteriaQuantityArray[criteriaIndexObj["33096"]]
        else:
            criteriaIndexObj["33096"] = 0;
        if(criteriaIndexObj.get("33097", "Empty") != "Empty"):
            criteriaIndexObj["33097"] = criteriaQuantityArray[criteriaIndexObj["33097"]]
        else:
            criteriaIndexObj["33097"] = 0;
        if(criteriaIndexObj.get("33098", "Empty") != "Empty"):
            criteriaIndexObj["33098"] = criteriaQuantityArray[criteriaIndexObj["33098"]]
        else:
            criteriaIndexObj["33098"] = 0;
        if(criteriaIndexObj.get("32028", "Empty") != "Empty"):
            criteriaIndexObj["32028"] = criteriaQuantityArray[criteriaIndexObj["32028"]]
        else:
            criteriaIndexObj["32028"] = 0;
        playerObject[user] = criteriaIndexObj
        playerList.append(user)



    return playerObject

def main(playerList, raidersMythicDataObject):


    print("Get M+ Information Start")
    getRaidersMythicsRan("Alexstrasza", "Wickedsoul", raidersMythicDataObject, playerList)
    getRaidersMythicsRan("Alexstrasza", "Bagnar", raidersMythicDataObject, playerList)
    getRaidersMythicsRan("Alexstrasza", "Problim", raidersMythicDataObject, playerList)
    getRaidersMythicsRan("Terokkar", "Drx", raidersMythicDataObject, playerList)
    getRaidersMythicsRan("Alexstrasza", "Divr", raidersMythicDataObject, playerList)
    getRaidersMythicsRan("Alexstrasza", "Sythera", raidersMythicDataObject, playerList)
    getRaidersMythicsRan("Terokkar", "Zaxvriin", raidersMythicDataObject, playerList)
    getRaidersMythicsRan("Alexstrasza", "Soothing", raidersMythicDataObject, playerList)
    getRaidersMythicsRan("Alexstrasza", "Ragdas", raidersMythicDataObject, playerList)
    getRaidersMythicsRan("Alexstrasza", "Onemanaleft", raidersMythicDataObject, playerList)
    getRaidersMythicsRan("Alexstrasza", "Valanadria", raidersMythicDataObject, playerList)
    getRaidersMythicsRan("Alexstrasza", "Applejuice", raidersMythicDataObject, playerList)
    getRaidersMythicsRan("Alexstrasza", "Arroo", raidersMythicDataObject, playerList)
    getRaidersMythicsRan("Alexstrasza", "Azavia", raidersMythicDataObject, playerList)
    getRaidersMythicsRan("Alexstrasza", "Beckintailz", raidersMythicDataObject, playerList)
    getRaidersMythicsRan("Alexstrasza", "Dalkx", raidersMythicDataObject, playerList)
    getRaidersMythicsRan("Alexstrasza", "Hyuna", raidersMythicDataObject, playerList)
    getRaidersMythicsRan("Alexstrasza", "Newaayy", raidersMythicDataObject, playerList)
    getRaidersMythicsRan("Alexstrasza", "Nzx", raidersMythicDataObject, playerList)
    getRaidersMythicsRan("Alexstrasza", "Roiid", raidersMythicDataObject, playerList)
    getRaidersMythicsRan("Alexstrasza", "Travincal", raidersMythicDataObject, playerList)
    getRaidersMythicsRan("Alexstrasza", "Téria", raidersMythicDataObject, playerList)
    getRaidersMythicsRan("Alexstrasza", "Vladiri", raidersMythicDataObject, playerList)
    getRaidersMythicsRan("Alexstrasza", "Cyvusz", raidersMythicDataObject, playerList)
    print("Get M+ Information End")

