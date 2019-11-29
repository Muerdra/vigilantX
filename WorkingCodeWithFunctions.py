import csv

def SumRunoff2008():
    with open("Discharge2008.csv") as DischargeFile2008:
        DischargeFile2008.next()
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

        for row in csv.reader(DischargeFile2008):
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
            totalDischarge2008 = Jan + Feb + Mar + Apr + May + Jun + Jul + Aug + Sep + Oct + Nov + Dec 
    DischargeFile2008.close()
    return totalDischarge2008


def SumRunoff2018():
    with open("Discharge2018.csv") as DischargeFile2018:
        DischargeFile2018.next()
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

        for row in csv.reader(DischargeFile2018):
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
            totalDischarge2018 = Jan + Feb + Mar + Apr + May + Jun + Jul + Aug + Sep + Oct + Nov + Dec 
    
    DischargeFile2018.close()
    return totalDischarge2018

    
def SumPrecipitation2008():
    with open("Precipitation2008.csv") as precip2008file:
        next(precip2008file)

        totalJan = 0
        totalFeb = 0
        totalMar = 0
        totalApr = 0
        totalMay = 0
        totalJun = 0
        totalJul = 0
        totalAug = 0
        totalSep = 0
        total1Oct = 0
        total1Nov = 0
        totalDec = 0

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

            totalJan += float(precipJan)
            totalFeb += float(precipFeb)
            totalMar += float(precipMar)
            totalApr += float(precipApr)
            totalMay += float(precipMay)
            totalJun += float(precipJun)
            totalJul += float(precipJul)
            totalAug += float(precipAug)
            totalSep += float(precipSep)
            total1Oct += float(precipOct)
            total1Nov += float(precipNov)
            totalDec += float(precipDec)

            totalprecip2008 = totalJan + totalFeb + totalMar + totalApr + totalMay + totalJun + totalJul + totalAug + totalSep + total1Oct + total1Nov + totalDec 
    
    precip2008file.close()
    return totalprecip2008

def SumPrecipitation2018():
    with open("Precipitation2018.csv") as precip2018file:
        next(precip2018file)

        totalJan = 0
        totalFeb = 0
        totalMar = 0
        totalApr = 0
        totalMay = 0
        totalJun = 0
        totalJul = 0
        totalAug = 0
        totalSep = 0
        total1Oct = 0
        total1Nov = 0
        totalDec = 0

        for row in csv.reader(precip2018file):
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

            totalJan += float(precipJan)
            totalFeb += float(precipFeb)
            totalMar += float(precipMar)
            totalApr += float(precipApr)
            totalMay += float(precipMay)
            totalJun += float(precipJun)
            totalJul += float(precipJul)
            totalAug += float(precipAug)
            totalSep += float(precipSep)
            total1Oct += float(precipOct)
            total1Nov += float(precipNov)
            totalDec += float(precipDec)

            totalprecip2018 = totalJan + totalFeb + totalMar + totalApr + totalMay + totalJun + totalJul + totalAug + totalSep + total1Oct + total1Nov + totalDec 
    
    precip2018file.close()
    return totalprecip2018   

def RiverRunoffRatio(SRR, SPR):
    RnoffRatioRiv = float(SRR) / float(SPR)
    return RnoffRatioRiv

def MVWRunoffRatio():
    AvgRnoff = 367.0
    AvgPrecip = 898.0
    RnoffRatio = AvgRnoff / AvgPrecip
    return RnoffRatio

def CHComparisonH():
      high = "HIGHER"
      return high

def CHComparisonL():
      low = "LOWER"
      return low

datafunction2008runoff = SumRunoff2008()
datafunction2008precip = SumPrecipitation2008()

datafunction2018runoff = SumRunoff2018()
datafunction2018precip = SumPrecipitation2018()

RunoffRatio_River2008 = RiverRunoffRatio(datafunction2008runoff, datafunction2008precip)
RunoffRatio_River2018 = RiverRunoffRatio(datafunction2018runoff, datafunction2018precip)
RunoffRatio_Watershed = MVWRunoffRatio()

if (RunoffRatio_River2008 > RunoffRatio_Watershed):
    calcrra2008 = CHComparisonH()
elif (RunoffRatio_River2008 < RunoffRatio_Watershed):
    calcrra2008 = CHComparisonL()

if (RunoffRatio_River2018 > RunoffRatio_Watershed):
    calcrra2018 = CHComparisonH()
elif (RunoffRatio_River2018 < RunoffRatio_Watershed):
    calcrra2018 = CHComparisonL()

print "\t\t\t\t\t\tRunoff Ratio Calculator"
print
print "Our calculator compares the Mississippi River at Fergusons Falls runoff ratio with the Mississippi Valley Watershed runoff ratio."  
print

year = raw_input("Enter year (2008/2018): ")    
year = year.rstrip('\r')
print  

if year == '2008' :
      print "Data for 2008"
      print "Total Stream Runoff in year (2008): " + str(round(datafunction2008runoff,2)) + " mm"
      print
      print "Total Precipitation in year (2008): " + str(round(datafunction2008precip,2)) + " mm"
      print
      print "Average Runoff Ratio of Mississippi Valley Watershed: " + str(round(RunoffRatio_River2008,2))
      print
      print "The stream has a " + str(calcrra2008) + " runoff ratio than average."

elif year == '2018' :
      print "Data for 2018"
      print "Total Stream Runoff in year (2018): " + str(round(datafunction2018runoff,2)) + " mm"
      print
      print "Total Precipitation in year (2018): " + str(round(datafunction2018precip,2)) + " mm"
      print
      print "Average Runoff Ratio of Mississippi Valley Watershed: " + str(round(RunoffRatio_River2018,2))
      print
      print "The stream has a " + str(calcrra2018) + " runoff ratio than average."

else:
      print "No can-do man-do"
      
  
question = raw_input("Would you like to calculate the runoff ratio for another year (Y/N)? ")
question = question.rstrip('\r')   
# (if user selects Y) Repeat above layout  
if question.upper() == "y":
      print "does stuff again"
# (if user selects N) Thank you for using the Runoff Ratio Calculator for the Mississippi River! 
else:
      print "Thank you for using the Runoff Ratio Calculator for the Mississippi River! "
