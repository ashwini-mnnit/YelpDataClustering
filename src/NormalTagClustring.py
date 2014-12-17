import nltk
from nltk.corpus import stopwords
from collections import defaultdict
from nltk.stem.lancaster import LancasterStemmer
import numpy as np
import json
import re
import heapq

from util import *
from clustring import *
from parser import *

GlobalBussinessDict = defaultdict(lambda: defaultdict(str))
GlobalBussinessDict = defaultdict(lambda: defaultdict(str))
GlobalBussinessTextDict = defaultdict(lambda: defaultdict(str))
GlobalTagList=defaultdict(int)

def AddAtttributeTags(clusterData,sample_count,businessId):
    if type(GlobalBussinessDict[businessId]["attributes"]) is not dict:
        return
    if "Take-out" in GlobalBussinessDict[businessId]["attributes"]:
        clusterData[sample_count][4]=getTrueFalse(GlobalBussinessDict[businessId]["attributes"]["Take-out"])    
    if("Good For" in GlobalBussinessDict[businessId]["attributes"]):
        clusterData[sample_count][5]=getGoofForVal(GlobalBussinessDict[businessId]["attributes"]["Good For"])
    if "Caters" in GlobalBussinessDict[businessId]["attributes"]:
        clusterData[sample_count][6]=getTrueFalse(GlobalBussinessDict[businessId]["attributes"]["Caters"])
    if "Noise Level" in GlobalBussinessDict[businessId]["attributes"]:
        clusterData[sample_count][7]=getTrueFalse(GlobalBussinessDict[businessId]["attributes"]["Noise Level"])
    if "Takes Reservations"  in  GlobalBussinessDict[businessId]["attributes"]:      
        clusterData[sample_count][8]=getTrueFalse(GlobalBussinessDict[businessId]["attributes"]["Takes Reservations"])
    if "Delivery" in GlobalBussinessDict[businessId]["attributes"]:
        clusterData[sample_count][9]=getTrueFalse(GlobalBussinessDict[businessId]["attributes"]["Delivery"])
    
    if "Parking" in GlobalBussinessDict[businessId]["attributes"]:
        clusterData[sample_count][10]=getParkingVal(GlobalBussinessDict[businessId]["attributes"]["Parking"])
    
    if "Has TV" in GlobalBussinessDict[businessId]["attributes"]:
        clusterData[sample_count][11]=getTrueFalse(GlobalBussinessDict[businessId]["attributes"]["Has TV"])
    if "Outdoor Seating" in  GlobalBussinessDict[businessId]["attributes"]:
        clusterData[sample_count][12]=getTrueFalse(GlobalBussinessDict[businessId]["attributes"]["Outdoor Seating"])
    if "Attire" in GlobalBussinessDict[businessId]["attributes"]:
        clusterData[sample_count][13]=getTrueFalse(GlobalBussinessDict[businessId]["attributes"]["Attire"])
    
    if "Ambience" in GlobalBussinessDict[businessId]["attributes"]:
        clusterData[sample_count][14]=getAmbianceVal(GlobalBussinessDict[businessId]["attributes"]["Ambience"])

    if "Waiter Service" in GlobalBussinessDict[businessId]["attributes"]:
        clusterData[sample_count][15]=getTrueFalse(GlobalBussinessDict[businessId]["attributes"]["Waiter Service"])
    if "Accepts Credit Cards" in GlobalBussinessDict[businessId]["attributes"]:    
        clusterData[sample_count][16]=getTrueFalse(GlobalBussinessDict[businessId]["attributes"]["Accepts Credit Cards"])
    if "Good for Kids" in GlobalBussinessDict[businessId]["attributes"]:
        clusterData[sample_count][17]=getTrueFalse(GlobalBussinessDict[businessId]["attributes"]["Good for Kids"])
    if "Good For Groups" in GlobalBussinessDict[businessId]["attributes"]:
        clusterData[sample_count][18]=getTrueFalse(GlobalBussinessDict[businessId]["attributes"]["Good For Groups"])
    if "Price Range" in GlobalBussinessDict[businessId]["attributes"]:
        clusterData[sample_count][19]=getTrueFalse(GlobalBussinessDict[businessId]["attributes"]["Price Range"])
     
     
def DoClustinrgWithoutText(sampleData):  
    numSample= len(GlobalBussinessDict.keys()) 
    labels=[]  
    sample_count=0
    sampleData=np.zeros(shape=(numSample,20), dtype=float)
    for businessId in GlobalBussinessDict:   
        labels.append(businessId)         
        sampleData[sample_count][0]=int(GlobalBussinessDict[businessId]["longitude"])+500
        sampleData[sample_count][1]=int(GlobalBussinessDict[businessId]["latitude"])+500
        sampleData[sample_count][2]=int(GlobalBussinessDict[businessId]["stars"])
        sampleData[sample_count][3]=int(GlobalBussinessDict[businessId]["review_count"])
        AddAtttributeTags(sampleData,sample_count,businessId)     
        sample_count=sample_count+1   
    kMeanClustring(sampleData, 10, len(labels), labels,0)
    kMeanMiniBatchClustring(sampleData, 10, len(labels), labels,0)
        
def businessDataParser():
    filename_sample="C:\\Users\\Owner\\Dropbox\\Courses\\Artificial Intillegence\\project\\Yelp data\\businessdataS.txt"
    with open(filename_sample) as f:
        for line in f:
            businessData = json.loads(line)
            GlobalBussinessDict[businessData["business_id"]]["longitude"]=businessData["longitude"]
            GlobalBussinessDict[businessData["business_id"]]["latitude"]=businessData["latitude"]
            GlobalBussinessDict[businessData["business_id"]]["attributes"]= businessData["attributes"]
            GlobalBussinessDict[businessData["business_id"]]["stars"]= businessData["stars"]
            GlobalBussinessDict[businessData["business_id"]]["review_count"]= businessData["review_count"]
            
def textParser():
    filename_sample="C:\\Users\\Owner\\Dropbox\\Courses\\Artificial Intillegence\\project\\Yelp data\\votesdataS.txt"
    with open(filename_sample) as f:
        for line in f:
            votesData = json.loads(line)
            if votesData["business_id"] in GlobalBussinessTextDict:
                count= len(GlobalBussinessTextDict[votesData["business_id"]].keys())
                name="text"+str(count)
                GlobalBussinessTextDict[votesData["business_id"]][name]= votesData["text"]
            else: 
                GlobalBussinessTextDict[votesData["business_id"]]["text0"]=votesData["text"]
           
def main():
    clusterDataWithOutText=np.ndarray(shape=(10,10), dtype=float)  
    businessDataParser()
    textParser();
    DoClustinrgWithoutText(clusterDataWithOutText)
    ii=0;

if __name__ == '__main__': 
    main()
