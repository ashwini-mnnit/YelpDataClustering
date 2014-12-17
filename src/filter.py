from collections import defaultdict
import json

GlobalVD = defaultdict(int)

def getVotes():
    filename = "C:\\Users\\Owner\\Dropbox\\Courses\\Artificial Intillegence\\project\\Yelp data\\02.txt"
    recCount =0
    votesDataFile = "C:\\Users\\Owner\\Dropbox\\Courses\\Artificial Intillegence\\project\\Yelp data\\votesdataS.txt"
    writeF  = open(votesDataFile, 'w')
    with open(filename) as f:
        for line in f:
            recCount=recCount+1 
            if (recCount>10000):
                break;
           
            votesData = json.loads(line)
            writeF.write(line)
            if votesData["business_id"] not in GlobalVD:
                GlobalVD[votesData["business_id"]]=1
            
            
    writeF.close()        
            
    filename2 = "C:\\Users\\Owner\\Dropbox\\Courses\\Artificial Intillegence\\project\\Yelp data\\01.txt"
    recCount2 =0
    businessDataFile = "C:\\Users\\Owner\\Dropbox\\Courses\\Artificial Intillegence\\project\\Yelp data\\businessdataS.txt"
    writeF  = open(businessDataFile, 'w')
    
    with open(filename2) as f2:
        for line in f2:
            recCount2=recCount2+1
            if (recCount2>30000):
                break;
           
            businessData = json.loads(line)
            if(businessData["business_id"] in GlobalVD):
                writeF.write(line) 
    writeF.close()
def main():
    getVotes()   
if __name__ == '__main__': 
    main()