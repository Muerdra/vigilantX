This program that (1) calculates the annual runoff ratio of an individual stream from yearly precipitation and yearly runoff; (2) compares the stream runoff ratio to the average runoff ratio of the watershed that the stream lies in; and (3) states whether the stream has a higher/lower runoff ratio than the watershed. Data for daily discharge and precipitation needs to be sorted by year and discharge also needs to be converted from m3/s into runoff (mm) in order to calculate runoff ratio. 

##############################Average Runoff Ratio for Mississipi River at Fergusen Falls#######################################

# Mike Wagner - program to calculate the Runoff Ratio of the Mississippi River at Fergusons Falls
# using the results of the SumRunoff_River which gives us the the average annual runnoff for the Mississipi 
# River for the chosen year, and SumPrecip_River, which gives us the average annual precipitation for the River

def RiverRunoffRatio(SRR, SPR):
    SRR = SumRunoff_River
    SPR = SumPrecip_River
    RnoffRatioRiv = float(SRR) / float(SPR)
    return RnoffRatioRiv



RunoffRatio_River = RiverRunoffRatio(SumRunoff_River, SumPrecip_River)



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

def main():
    try:  #Error detection added by Mike Wagner
        with open("Discharge2008.csv") as fin:

            fin.next()
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
    
    except IOError:
        print "Can\'t find file or read"
    else:
        print total

    
    
    try: #error detection added by Mike Wagner
        with open("Precipitation2008.csv") as precip2008file:
            next(precip2008file)

            total1 = 0
            total2 = 0
            total3 = 0
            total4 = 0
            total5 = 0
            total6 = 0
            total7 = 0
            total8 = 0
            total9 = 0
            total10 = 0
            total11 = 0
            total12 = 0

            for row in csv.reader(precip2008file):
                precipJan = float(row[1])
                precipFeb = float(row[2])
                precipMar = float(row[3])
                precipApr = float(row[4])
                precipMay = float(row[5])
                precipJun = float(row[6])
                precipJul = float(row[7])
                precipAug = float(row[8])
                precipSep = float(row[9])
                precipOct = float(row[10])
                precipNov = float(row[11])
                precipDec = float(row[12])

                total1 += float(precipJan)
                total2 += float(precipFeb)
                total3 += float(precipMar)
                total4 += float(precipApr)
                total5 += float(precipMay)
                total6 += float(precipJun)
                total7 += float(precipJul)
                total8 += float(precipAug)
                total9 += float(precipSep)
                total10 += float(precipOct)
                total11 += float(precipNov)
                total12 += float(precipDec)
                totalprecip = total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 

    except IOError:
        print "Can\'t find file or read"
    else:
        print totalprecip
    
    
    
    
if __name__ == '__main__':
    main()
