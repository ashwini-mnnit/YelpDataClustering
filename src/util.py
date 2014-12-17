import math

def log10(x): 
    return math.log(x) / math.log(10)  

def getIDF(x, totalDocCount):
    return log10(totalDocCount/x)
def getTF(x):
    return 1+log10(x)
def getTrueFalse(val):
    if val is "false":
        return 0
    return 1

def getGoofForVal(valdict):
    if("dessert" in  valdict and getTrueFalse(valdict["dessert"])):
        return 1;
    if(getTrueFalse(valdict["latenight"])):
        return 2;
    if(getTrueFalse(valdict["lunch"])):
        return 3;
    if(getTrueFalse(valdict["dinner"])):
        return 4;
    if(getTrueFalse(valdict["breakfast"])):
        return 5;
    if(getTrueFalse(valdict["brunch"])):
        return 6;
    return 0;
 
def getParkingVal(valdict):
    if(getTrueFalse(valdict["garage"])):
        return 1;
    if(getTrueFalse(valdict["street"])):
        return 2;
    if(getTrueFalse(valdict["validated"])):
        return 3;
    if(getTrueFalse(valdict["lot"])):
        return 4;
    if(getTrueFalse(valdict["valet"])):
        return 5;
    return 0;
    
def getAmbianceVal(valdict):
    if(getTrueFalse(valdict["romantic"])):
        return 1;
    if(getTrueFalse(valdict["intimate"])):
        return 2;
    if(getTrueFalse(valdict["touristy"])):
        return 3;
    if(getTrueFalse(valdict["hipster"])):
        return 4;
    if(getTrueFalse(valdict["classy"])):
        return 5;
    if(getTrueFalse(valdict["trendy"])):
        return 6;
    if(getTrueFalse(valdict["upscale"])):
        return 7;
    if(getTrueFalse(valdict["casual"])):
        return 8
    return 0;
    