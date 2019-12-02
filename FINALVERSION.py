# RunoffRatioCalculator.py
# 29 November 2019
# Created by: Craig Harding, Mike Wagner, Roshelle Chan, Tasfia Khaled
# 
# Contributions:
# Craig - Introduction/user input, runoff function, comparison of stream runoff ratio vs watershed runoff ratio, reptition, 
#         error/test results excel file, problematic test file, putting section of code into functions 
# Mike - runoff ratio for stream and watershed, error handling/data validation/exceptions, problematic test file, putting section
#        of code into function  
# Roshelle - error handling/data validation/exceptions, runoff and precipitation functions, organzing code, merging functions with design,
#            writing comments
# 
# Purpose:
# This program determines the runoff ratio of the Mississippi River at # Fergusons Falls and 
# compares it to the average runoff ratio of the Mississippi Valley Watershed. Calculating the 
# runoff ratio is important for flood control and possible flood zone hazard delineation. 
# Our program’s target audience are hydrologists, water resource and flood risk specialists. 
# It will also be accessible to the general public as it may be especially useful to those 
# residing close to the river
#
# Program structure:
# First the program converts daily discharge to runoff and sums it up to get yearly discharge. Then the 
# program sums up daily precipitation to get year precipitation. Afterwards, annual runoff ratio is 
# calculated by dividing yearly precipitation with yearly runoff. Then the stream runoff ratio is compared
# to the average runoff ratio of the watershed that the stream lies in and the program states whether the 
# stream has a higher/lower runoff ratio than the watershed. 
#
# Assumptions/Planned for limitations:
# For simplicity purposes, the program only has the option of two years (2018, 2008) and one
# stream (Mississippi River at Ferguson Falls). Therefore, this program assumes that the 
# users are only interested in this stream and watershed, however, the program has the potential to be 
# scaled up to include other streams and watersheds. Precipitation and runoff data that was available and 
# used to calculate the average runoff ratio of the Mississippi Valley Watershed spans 29 years
# only, from 1971 to 2000, which may impact its accuracy in the comparison result. 
# 
# Inputs:
# Inputs are daily discharge and daily precipitation of csv files of Mississippi River at Ferguson Falls
# in csv format for 2008 and 2018 (Discharge2008, Discharge2018, Precipitation2008, Precipitation2018). 
# All these input files are already formatted according to month and day, with all unnecessary years 
# and fields removed. In addition, the program wil prompt for user input for which year they wish to view. 
#
# Output: 
# The output is via a screen/command prompt. Data error/accuracy is dependent on data provided by 
# Environment Canada/Government of Canada. Rounding to two decimal places may give an error of +/- 0.001. 

# Units:
# Discharge (m3/s) converted to Runoff (mm)
# Precipitation (mm)
# Drainage area for river (m2)
# Runoff ratio (no units)
# 
# References:
# Use of runoff ratio (https://www.waterboards.ca.gov/water_issues/programs/swamp/docs/cwt/guidance/513.pdf)
# Daily discharge for Mississippi River at Fergusons Falls in 2008, 2018 (https://wateroffice.ec.gc.ca/report/historical_e.html?stn=02KF001&dataType=Daily&parameterType=Flow&year=2008&mode=Graph&y1Max=1&y1Min=1)
# Daily precipitation from Drummond Centre Weather station in 2008, 2018 (https://climate.weather.gc.ca/climate_data/daily_data_e.html?hlyRange=%7C&dlyRange=1984-06-01%7C2019-10-23&mlyRange=1984-01-01%7C2006-12-01&StationID=4268&Prov=ON&urlExtension=_e.html&searchType=stnName&optLimit=yearRange&StartYear=1840&EndYear=2019&selRowPerPage=25&Line=0&searchMethod=contains&txtStationName=drummond&timeframe=2&Day=24&Year=2008&Month=10)
# Drainage area of Mississippi River at Ferguson Falls, Average precipitation and runoff for Mississippi Valley Watershed (https://www.mrsourcewater.ca/images/Documents/ConceptualWaterBudget/MainReport/M-RConceptualWaterBudget_PrelimDraft.pdf)
# Formula for converting discharge to runoff (https://www.researchgate.net/post/How_to_convert_discharge_m3_s_to_mm_of_discharge)


import csv

# Function for converting daily discharge to daily runoff and summing daily runoff to get annual runoff for 2008
# Final units are in mm
# Inputs required: Discharge2008 csv file with daily discharge values for 2008
# Returns: Sum of daily runoff for 2008
def SumRunoff2008():
    try: 
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
            
            # converts each value from discharge (m3/s) to runoff (mm)
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

                # error handling to ensure there are no negative numbers in the csv
                if (runoffJan < 0) or (runoffFeb < 0) or (runoffMar < 0) or (runoffApr < 0) or (runoffMay < 0) or (runoffJun < 0) or (runoffJul < 0) or (runoffAug < 0) or (runoffSep < 0) or (runoffOct < 0) or (runoffNov < 0) or (runoffDec < 0):
                    print "Discharge2008 file contains a negative number - please check values to ensure there are no negatives."
                    exit()

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
    
    # error handling and return message for opening a file that does not exist          
    except IOError:
        print "Can\'t find or read file - please check input file name and format."
        exit()

    # error handling for strings/null values in input file  
    except ValueError:
        print "Values in Discharge2008 file must be numeric and cannot contain null values or letters."
        exit()

    else:
        DischargeFile2008.close()
        return totalDischarge2008

# Function for converting daily discharge to daily runoff and summing daily runoff to get annual runoff for 2018
# Final units are in mm 
# Inputs required: Discharge2018 csv file with daily discharge values for 2018
# Returns: Sum of daily runoff for 2018
def SumRunoff2018(): 
    try:
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

            # converts each value from discharge (m3/s) to runoff (mm)
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

                # error handling to ensure there are no negative numbers in the csv
                if (runoffJan < 0) or (runoffFeb < 0) or (runoffMar < 0) or (runoffApr < 0) or (runoffMay < 0) or (runoffJun < 0) or (runoffJul < 0) or (runoffAug < 0) or (runoffSep < 0) or (runoffOct < 0) or (runoffNov < 0) or (runoffDec < 0):
                    print "Discharge2018 file contains a negative number - please check values to ensure there are no negatives."
                    exit()

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

    # error handling and return message for opening a file that does not exist          
    except IOError:
        print "Can\'t find or read file - please check input file name and format."
        exit()
    
    # error handling for strings/null values in input file         
    except ValueError:
        print "Values in Discharge2018 file must be numeric and cannot contain null values or letters."
        exit()

    else:
        DischargeFile2018.close()
        return totalDischarge2018   

# Function for summing daily precipitation to get annual precipitation for 2008
# Units are in mm
# Inputs required: Precipitation2008 csv file with daily discharge values for 2008
# Returns: Sum of daily precipitation for 2008
def SumPrecipitation2008():
    try:       
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
            totalOct = 0
            totalNov = 0
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

                # error handling to ensure there are no negative numbers in the csv
                if (precipJan < 0) or (precipFeb < 0) or (precipMar < 0) or (precipApr < 0) or (precipMay < 0) or (precipJun < 0) or (precipJul < 0) or (precipAug < 0) or (precipSep < 0) or (precipOct < 0) or (precipNov < 0) or (precipDec < 0):
                    print "Precipitation2008 file contains a negative number - please check values to ensure there are no negatives."                 
                    exit()

                totalJan += float(precipJan)
                totalFeb += float(precipFeb)
                totalMar += float(precipMar)
                totalApr += float(precipApr)
                totalMay += float(precipMay)
                totalJun += float(precipJun)
                totalJul += float(precipJul)
                totalAug += float(precipAug)
                totalSep += float(precipSep)
                totalOct += float(precipOct)
                totalNov += float(precipNov)
                totalDec += float(precipDec)

                totalprecip2008 = totalJan + totalFeb + totalMar + totalApr + totalMay + totalJun + totalJul + totalAug + totalSep + totalOct + totalNov + totalDec 
    
    # error handling and return message for opening a file that does not exist           
    except IOError:
        print "Can\'t find or read file - please check input file name and format."
        exit()

    # error handling for strings/null values in input file         
    except ValueError:
        print "Values in Precipitation2008 file must be numeric and cannot contain null values or letters."
        exit()

    else:
        precip2008file.close()
        return totalprecip2008

# Function for summing daily precipitation to get annual precipitation for 2018
# Units are in mm
# Inputs required: Precipitation2008 csv file with daily discharge values for 2018
# Returns: Sum of daily precipitation for 2018
def SumPrecipitation2018():
    try:   
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
            totalOct = 0
            totalNov = 0
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

                # error handling to ensure there are no negative numbers in the csv
                if (precipJan < 0) or (precipFeb < 0) or (precipMar < 0) or (precipApr < 0) or (precipMay < 0) or (precipJun < 0) or (precipJul < 0) or (precipAug < 0) or (precipSep < 0) or (precipOct < 0) or (precipNov < 0) or (precipDec < 0):
                    print "Precipitation2008 file contains a negative number - please check values to ensure there are no negatives."                                   
                    exit()

                totalJan += float(precipJan)
                totalFeb += float(precipFeb)
                totalMar += float(precipMar)
                totalApr += float(precipApr)
                totalMay += float(precipMay)
                totalJun += float(precipJun)
                totalJul += float(precipJul)
                totalAug += float(precipAug)
                totalSep += float(precipSep)
                totalOct += float(precipOct)
                totalNov += float(precipNov)
                totalDec += float(precipDec)

                totalprecip2018 = totalJan + totalFeb + totalMar + totalApr + totalMay + totalJun + totalJul + totalAug + totalSep + totalOct + totalNov + totalDec 
    
    # Error handling and return message for opening a file that does not exist            
    except IOError:
        print "Can\'t find or read file - please check input file name and format."
        exit()
    
    # Error handling for strings/null values in input file                
    except ValueError:
        print "Values in Precipitation2018 file must be numeric and cannot contain null values or letters"
        exit()

    else:
        precip2018file.close()
        return totalprecip2018   

# Function for calculating runoff ratio of the stream 
# There are no units for runoff ratio 
def RiverRunoffRatio(SRR, SPR):
    RnoffRatioRiv = float(SRR) / float(SPR)
    return RnoffRatioRiv

# Function for calculating runoff ratio fo the watershed
# This is placed in a function so that it can be easily modified 
# in the future / updated with more accurate values, if any 
def WatershedRunoffRatio():
    AvgRnoff = 367.0
    AvgPrecip = 898.0

    RnoffRatio = AvgRnoff / AvgPrecip
    return RnoffRatio

# Functions for returning comparison result of watershed vs stream runoff ratio
def CHComparisonH():
    high = "HIGHER"
    return high

def CHComparisonL():
    low = "LOWER"
    return low

def CHComparisonE():
    equal = "EQUAL"
    return equal


# Start of loop for program: if users enter any keys (except for N) when prompted to repeat the program,
# they will be given a message to re-enter the year and the program repeats
while True:
    
    # Retrieve watershed runoff ratio from function 
    RunoffRatio_Watershed = WatershedRunoffRatio()
    
    # Display of program title and description
    print
    print "\t\t\t\t\t\tRunoff Ratio Calculator"
    print
    print "This calculator compares the Mississippi River at Fergusons Falls runoff ratio with the Mississippi Valley Watershed runoff ratio."  
    print

    try: 
        # Retrieve user input for year 
        year = input("Enter year (2008/2018): ")    
        print  

        # If user selects 2008 as input year 
        if year == 2008:
            
            # Retrieve sum of RUNOFF for 2008
            datafunction2008runoff = SumRunoff2008()

            # RUNOFF error handling: After conducting research on the maximum discharge of the watershed, it was 
            # found that the maximum was 730 mm in a year, so we decided that a value of 750mm is reasonable to set as 
            # the limit of range
            if datafunction2008runoff > 750:
                print "The total discharge for 2008 is very high (over 750 for the year). Please check your data."
                print "If your data is verified to be correct, enter any key to continue."
                answer = raw_input("Otherwise, enter N to abort the program. ")
                answer = answer.rstrip('\r').upper()                  
                print

                if answer == "N":
                    exit()
            
            # RUNOFF error handling: total runoff cannot be a negative number or equal to zero
            if datafunction2008runoff <= 0:
                print "The total discharge for 2008 is less than 0 - please check your data."
                print "**********************************************************************************************************************************"              
                continue

            # RUNOFF output: display total runoff for 2008
            # Rounds numbers to 2 decimal places
            print "Total Stream Runoff in year (2008): " + str(round(datafunction2008runoff,2)) + " mm"
            print

            # Retrieve sum of PRECIPITATION for 2008 
            datafunction2008precip = SumPrecipitation2008()

            # PRECIPITATION error handling: Discovered from research that total precipitation for the watershed did not exceed
            # 1500mm so we used this value as the range of limit - however, we made sure to allow for users to let the program 
            # continue if they verify that the values are correct (as there may be anomalous years)
            # http://mvc.on.ca/wp-content/uploads/2013/11/Water-Mangement-Response-to-Climate-Change_Subproject-4_NRCAN.pdf
            if datafunction2008precip > 1500:
                print "The total precipitation for 2008 is very high (over 1500 for the year). Please check your data."
                print "If your data is verified to be correct, enter any key to continue."
                answer = raw_input("Otherwise, enter N to abort the program. ")
                answer = answer.rstrip('\r').upper()                  
                print

                if answer == "N":
                    exit()  

            # PRECIPITATION error handling: Total precipitation cannot be a negative number or equal to zero 
            if datafunction2008precip <= 0:
                print "Values in precipitation cannot be zero - please check input file"
                print "**********************************************************************************************************************************"
                continue   
                
            # PRECIPITATION output: display total precipitation for 2008
            # Rounds numbers to 2 decimal places
            print "Total Precipitation in year (2008): " + str(round(datafunction2008precip,2)) + " mm"
            print

            # RUNOFF RATIO RIVER: Calculate the runoff ratio for the stream in 2008
            RunoffRatio_River2008 = RiverRunoffRatio(datafunction2008runoff, datafunction2008precip)

            # Comparison of runoff ratio of the river to the runoff ratio of the watershed  
            if (RunoffRatio_River2008 > RunoffRatio_Watershed):
                calcrra2008 = CHComparisonH()
            elif (RunoffRatio_River2008 < RunoffRatio_Watershed):
                calcrra2008 = CHComparisonL()
            elif (RunoffRatio_River2008) == (RunoffRatio_Watershed):
                calcrra2008 = CHComparisonE()

            # RUNOFF RATIO output: Display the runoff ratio for the stream, watershed, and comparison result for 2008
            # Rounds numbers to 2 decimal places
            print "Average Runoff Ratio of Mississippi River at Fergusons Falls: " + str(round(RunoffRatio_River2008,2))
            print 
            print "Average Runoff Ratio of Mississippi Valley Watershed: " + str(round(RunoffRatio_Watershed,2))
            print
            print "The stream has a " + str(calcrra2008) + " runoff ratio than average."
            print

        # If user selects 2018 as input year 
        elif year == 2018 :
            
            # Retrieve sum of RUNOFF for 2018             
            datafunction2018runoff = SumRunoff2018()

            # RUNOFF error handling: After conducting research on the maximum discharge of the watershed, it was 
            # found that the maximum was 730 mm in a year, so we decided that a value of 750mm is reasonable to set as 
            # the limit of range
            if datafunction2018runoff > 750:
                print "The total discharge for 2008 is very high (over 750 for the year). Please check your data."
                print "If your data is verified to be correct, enter any key to continue."
                answer = raw_input("Otherwise, enter N to abort the program. ")
                answer = answer.rstrip('\r').upper()                  
                print

                if answer == "N":
                    exit()
            
            # RUNOFF error handling: total runoff cannot be less than or equal to zero
            # Ends program and repeats            
            if datafunction2008runoff <= 0:
                print "The total discharge for 2008 is less than 0 - please check your data."
                print "**********************************************************************************************************************************"
                continue

            # RUNOFF output: display total stream runoff
            # Rounds numbers to 2 decimal places
            print "Total Stream Runoff in year (2018): " + str(round(datafunction2018runoff,2)) + " mm"
            print

            # Retrieve sum of PRECIPITATION for 2018
            datafunction2018precip = SumPrecipitation2018()

            # PRECIPITATION error handling: Discovered from research that total precipitation for the watershed did not exceed
            # 1500mm so we used this value as the range of limit - however, we made sure to allow for users to let the program 
            # continue if they verify that the values are correct (as there may be anomalous years)
            # http://mvc.on.ca/wp-content/uploads/2013/11/Water-Mangement-Response-to-Climate-Change_Subproject-4_NRCAN.pdf
            if datafunction2018precip > 1500:
                print "The total precipitation for 2008 is very high (over 1500 for the year). Please check your data."
                print "If your data is verified to be correct, enter any key to continue."
                answer = raw_input("Otherwise, enter N to abort the program. ")
                answer = answer.rstrip('\r').upper()                  
                print

                if answer == "N":
                    exit()              
            
            # PRECIPITATION error handling: total precipitation cannot be less than or equal to zero 
            # Ends program and repeats
            if datafunction2018precip <= 0: 
                print "Values in precipitation cannot be zero - please check input file"
                print "**********************************************************************************************************************************"
                continue   

            # PRECIPITATION output: Display total precipitation in 2018 
            print "Total Precipitation in year (2018): " + str(round(datafunction2018precip,2)) + " mm"
            print

            # Retrieve RUNOFF RATIO for RIVER
            RunoffRatio_River2018 = RiverRunoffRatio(datafunction2018runoff, datafunction2018precip)

            # Comparison of runoff ratio of the river to the runoff ratio of the watershed  
            if (RunoffRatio_River2018 > RunoffRatio_Watershed):
                calcrra2018 = CHComparisonH()
            elif (RunoffRatio_River2018 < RunoffRatio_Watershed):
                calcrra2018 = CHComparisonL()
            elif (RunoffRatio_River2018 == RunoffRatio_Watershed):
                calcrra2018 = CHComparisonE()

            # RUNOFF RATIO output: Display the runoff ratio for the stream, watershed, and comparison result for 2018 
            # Rounds numbers to 2 decimal places
            print "Average Runoff Ratio of Mississippi River at Fergusons Falls: " + str(round(RunoffRatio_River2018,2))
            print 
            print "Average Runoff Ratio of Mississippi Valley Watershed: " + str(round(RunoffRatio_Watershed,2))
            print
            print "The stream has a " + str(calcrra2018) + " runoff ratio than average."
            print

        # Data validation: if users do not enter 2008 or 2018, they will be instructed to do so
        else:
            print "Please input 2008 or 2018."
            print

        # Prompt users for repeating of program
        print "**********************************************************************************************************************************"
        print "Would you like to calculate the runoff ratio for another year?"
        question = raw_input("Enter any key to repeat the program. Enter N to stop. ")
        question=question.upper()
        question = question.rstrip('\r')  
        print "**********************************************************************************************************************************"
        print

        # Display goodbye message if users do not wish to repeat the program
        if question == "N":
            print "Thank you for using the Runoff Ratio Calculator for the Mississippi River!"
            break

    # Error handling: if users input non-numeric characters, they will be shown the message and prompted to re-enter
    # the year
    except NameError:
        print
        print "You have entered non-numeric characters - please enter 2008 or 2018 only."
        print "**********************************************************************************************************************************"

    # Error handling: if users input numeric characters that are not 2008 or 2018, they will be shown the message and 
    # prompted to re-enter the year
    except SyntaxError: 
        print 
        print "Please enter 2008 or 2018."
        print "**********************************************************************************************************************************"
