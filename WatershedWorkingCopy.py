This program that (1) calculates the annual runoff ratio of an individual stream from yearly precipitation and yearly runoff; (2) compares the stream runoff ratio to the average runoff ratio of the watershed that the stream lies in; and (3) states whether the stream has a higher/lower runoff ratio than the watershed. Data for daily discharge and precipitation needs to be sorted by year and discharge also needs to be converted from m3/s into runoff (mm) in order to calculate runoff ratio. 

#################################discharge to runoff###########################

import csv

with open("Discharge2008.csv") as fin:

    headerline = fin.next()
    total = 0
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

        total += float(runoffJan)
        total2 += float(runoffFeb)
        total3 += float(runoffMar)
        total4 += float(runoffApr)
        total5 += float(runoffMay)
        total6 += float(runoffJun)
        total7 += float(runoffJul)
        total8 += float(runoffAug)
        total9 += float(runoffSep)
        total10 += float(runoffOct)
        total11 += float(runoffNov)
        total12 += float(runoffDec)
        atotal = total + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11 + total12 
    
    print atotal
