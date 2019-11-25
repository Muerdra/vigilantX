This program that (1) calculates the annual runoff ratio of an individual stream from yearly precipitation and yearly runoff; (2) compares the stream runoff ratio to the average runoff ratio of the watershed that the stream lies in; and (3) states whether the stream has a higher/lower runoff ratio than the watershed. Data for daily discharge and precipitation needs to be sorted by year and discharge also needs to be converted from m3/s into runoff (mm) in order to calculate runoff ratio. 
################################Average Runoff Ratio for Entire Mississipi Valley WS###########################################
# Mike Wagner - program to calculate the Runoff Ratio of the entire Mississipi Valley Watershed
# using average Runnoff and average Precipitation from the years 1971 - 2000, these values
# were sourced from https://www.mrsourcewater.ca/images/Documents/ConceptualWaterBudget/MainReport/M-RConceptualWaterBudget_PrelimDraft.pdf

def MVWRunoffRatio():
    AvgRnoff = 367.0
    AvgPrecip = 898.0
    RnoffRatio = AvgRnoff / AvgPrecip
    return RnoffRatio
RunoffRatio_Watershed = MVWRunoffRatio()


#################################discharge to runoff###########################

import csv

with open("Discharge2008.csv") as fin:

    headerline = fin.next()
    Jan = 0
    Feb = 0
    Mar = 0
    Apr = 0
    May = 0
    Jun = 0
    Jul = 0
    Aug = 0
    Sep = 0
    Oct = 0
    Nov = 0
    Dec = 0

    for row in csv.reader(fin):
        runoffJan = float(row[1])
        runoffJan = (runoffJan*1000*24*3600)/(2620000000)

        runoffFeb = float(row[2])
        runoffFeb = (runoffFeb*1000*24*3600)/(2620000000)

        runoffMar = float(row[3])
        runoffMar = (runoffMar*1000*24*3600)/(2620000000)

        runoffApr = float(row[4])
        runoffApr = (runoffApr*1000*24*3600)/(2620000000)

        runoffMay = float(row[5])
        runoffMay = (runoffMay*1000*24*3600)/(2620000000)

        runoffJun = float(row[6])
        runoffJun = (runoffJun*1000*24*3600)/(2620000000)

        runoffJul = float(row[7])
        runoffJul = (runoffJul*1000*24*3600)/(2620000000)

        runoffAug = float(row[8])
        runoffAug = (runoffAug*1000*24*3600)/(2620000000)

        runoffSep = float(row[9])
        runoffSep = (runoffSep*1000*24*3600)/(2620000000)

        runoffOct = float(row[10])
        runoffOct = (runoffOct*1000*24*3600)/(2620000000)   
        
        runoffNov = float(row[11])
        runoffNov = (runoffNov*1000*24*3600)/(2620000000) 

        runoffDec = float(row[12])
        runoffDec = (runoffDec*1000*24*3600)/(2620000000)

        Jan += float(runoffJan)
        Feb += float(runoffFeb)
        Mar += float(runoffMar)
        Apr += float(runoffApr)
        May += float(runoffMay)
        Jun += float(runoffJun)
        Jul += float(runoffJul)
        Aug += float(runoffAug)
        Sep += float(runoffSep)
        Oct += float(runoffOct)
        Nov += float(runoffNov)
        Dec += float(runoffDec)
        total = Jan + Feb + Mar + Apr + May + Jun + Jul + Aug + Sep + Oct + Nov + Dec 
    
    print total
