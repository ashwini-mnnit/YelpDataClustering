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

GlobalBussinessDict = defaultdict(lambda: defaultdict(str))
GlobalBussinessDict = defaultdict(lambda: defaultdict(str))
GlobalBussinessTextDict = defaultdict(lambda: defaultdict(str))
GlobalTagList=defaultdict(int)
GlobalvirTagDict=defaultdict(lambda: list())
GlobalTagDictionary= defaultdict(int)  
GlobalTagCount=0; 

#nltk.download()
stemmer = LancasterStemmer();
stopwordList = stopwords.words('english')

def getAttributeCount():
    return 16 # hard coded to 16

def getNumFeature():
    rv_Count =4
    rv_Count=rv_Count + getAttributeCount()+len(GlobalTagDictionary.keys());  
    return rv_Count
def processVirtualTags():
    for bussinessId in GlobalBussinessTextDict:
        GlobalvirTagDict[bussinessId]=getVirtualTags(GlobalBussinessTextDict[bussinessId])
        addToVirtagList(GlobalvirTagDict[bussinessId])
        
def getdocdict(documentWordFreqDict,WordDocDictionary,total_N_doc):

    docTFIDFDict = defaultdict(float) 
    
    for doc in documentWordFreqDict:
        for word in documentWordFreqDict[doc]:
            docTFIDFDict[word] = getTF(documentWordFreqDict[doc][word]) * getIDF(len(WordDocDictionary[word]),total_N_doc)
    return docTFIDFDict
def getVirtualTags(viewsDoc):
    WordDocDictionary = defaultdict(lambda: defaultdict(int)) 
    documentWordFreqDict = defaultdict(lambda: defaultdict(int))
    total_N_doc=0
    for textID in viewsDoc:
        if viewsDoc[textID]:
            text = viewsDoc[textID]
            for word in re.findall("[a-z]+", text): 
                if word and word not in stopwordList :
                    word=stemmer.stem(word.lower())
                    WordDocDictionary[word][textID] += 1
                    documentWordFreqDict[textID][word] += 1
                    total_N_doc+=1        

    docTFIDFDict=  getdocdict(documentWordFreqDict,WordDocDictionary,total_N_doc)
    heap = [(-value, key) for key,value in docTFIDFDict.items()]
    toptags = heapq.nsmallest(5, heap)
    toptags = [(key, -value) for value, key in toptags]
    return toptags;          

    rvList=list()        
    for doc in toptags:
        rvList.append(doc[0])
    return rvList


 
def addVirtualTags(clusterData,sample_count,businessId):
    for tag in GlobalvirTagDict[businessId]:
        if tag in GlobalTagDictionary:
            pos = 20 + int(GlobalTagDictionary[tag])
            clusterData[sample_count][pos]=1
   
def addToVirtagList(taglist):
    global GlobalTagCount
    for tag in taglist:
        if tag not in GlobalTagDictionary:
            GlobalTagDictionary[tag]=GlobalTagCount #index of the tag
            GlobalTagCount=GlobalTagCount+1;
                
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

           
def DoClustinrgWithText(sampleData):
    numSample= len(GlobalBussinessDict.keys())
    numFeature = getNumFeature()   
    sampleData=np.zeros(shape=(numSample,numFeature), dtype=float)  
    
    labels=[]  
    sample_count=0
    for businessId in GlobalBussinessDict:   
        labels.append(businessId)         
        sampleData[sample_count][0]=int(GlobalBussinessDict[businessId]["longitude"])+500
        sampleData[sample_count][1]=int(GlobalBussinessDict[businessId]["latitude"])+500
        sampleData[sample_count][2]=int(GlobalBussinessDict[businessId]["stars"])
        sampleData[sample_count][3]=int(GlobalBussinessDict[businessId]["review_count"])
        AddAtttributeTags(sampleData,sample_count,businessId)
        addVirtualTags(sampleData,sample_count,businessId)
        sample_count=sample_count+1 
        
    kMeanClustring(sampleData, 10, len(labels), labels,1) 
    kMeanMiniBatchClustring(sampleData, 10, len(labels), labels,1)
               
def main():
    clusterDataWithtText=np.ndarray(shape=(10,10), dtype=float)  
    businessDataParser()
    textParser();
    processVirtualTags()
    DoClustinrgWithText(clusterDataWithtText)
    ii=0;

if __name__ == '__main__': 
    main()
