#import sys
import argparse
Rcountries = []
RYears = []

parser=argparse.ArgumentParser()
parser.add_argument('-C',"--command", required=True)
#parser.add_argument("--total", action="store_true", required=False)
#parser.add_argument("--interactive", action="store_true", required=False)
parser.add_argument('-Coun',"--Country")
parser.add_argument('-F', "--File", required=True)
parser.add_argument('-Y',"--Year", type=str )

#parser.add_argument('-Y',"--Year", type=str)
parser.add_argument('-OV',"--List", nargs='+')

args=parser.parse_args()
print(args)




def overall():
    countBEst=-1
    YearDict=dict()
    CountryList=args.List
    print(CountryList)
    BEST=""
    for i in CountryList:
        while True:
            line1 = file.readline()
            if not line1:
                break
            splitLine1 = line1.split('\t')

            if splitLine1[7] == i:
                if splitLine1[8] not in YearDict:
                    YearDict[splitLine1[8]] = 0
                if splitLine1[14]!="NA\n" and splitLine1[14]!="NA":
                    YearDict[splitLine1[8]]+=1
        for u in YearDict:
            if YearDict[u]>countBEst:
                countBEst=YearDict.get(u)
                BEST=u

        print(BEST+":"+str(countBEst))
        BEST=""
        countBEst=-1
        YearDict.clear()
        file.seek(0)






def medals():
    counter = 0
    medalCount = [0,0,0]
    country = args.Country
    year = args.Year
    while True:
        line1 = file.readline()
        if not line1:
            break
        splitLine1 = line1.split('\t')

        if splitLine1[7] == country:
            if splitLine1[14]=="Gold\n":
                medalCount[0] += 1
            elif splitLine1[14]=="Silver\n":
                medalCount[1]+=1
            elif splitLine1[14]=="Bronze\n":
                medalCount[2]+=1
        Rcountries.append(splitLine1[7])
        RYears.append(splitLine1[9])

    file.seek(0)
    file.readline()
    if year in RYears and country in Rcountries:
        pass
    else:
        print("wrong")
        quit()
    while True:
        line = file.readline()
        if not line:
            break

        splitLine = line.split('\t')

        if args.command == "medals":
            if splitLine[7] == args.Country and splitLine[9] ==args.Year and counter < 10:
                if splitLine[14]!="NA\n" and splitLine[14]!="NA":
                    name = splitLine[1]
                    medal = splitLine[14]

                    sport = splitLine[12]
                    print("name:" + name)
                    print("medal:" + medal)
                    print("sport:" + sport)
                    print("--------------")
                    counter += 1

    print("Country has:" + str(medalCount[0])+" Gold, "+ str(medalCount[1])+" Silver, "+str(medalCount[2])+" Bronze")


def total():
    yearTotal = args.Year
    print(yearTotal)
    CountrieData={}
    while True:
        lineTotal = file.readline()
        if not lineTotal:
            break
        splitLineTotal = lineTotal.split('\t')
        name = splitLineTotal[7]
        if yearTotal == splitLineTotal[9]:
            if splitLineTotal[14]!="NA\n" and splitLineTotal[14]!="NA":
                if str(name) not in CountrieData:
                    CountrieData.update({str(name):[0,0,0]})
                if splitLineTotal[14]=="Gold\n":
                    CountrieData[str(name)][0]+=1
                elif splitLineTotal[14]=="Bronze\n":
                    CountrieData[str(name)][1]+=1
                elif splitLineTotal[14]=="Silver\n":
                    CountrieData[str(name)][2]+=1

    for i in CountrieData:
        print(i+str(CountrieData[i]))

def interactive():
    FirstYear=20000
    FirstPlace=""
    Countries=input("Enter country")
    YearDict=dict()
    Gold=0
    Bronze=0
    Silver=0

    BEST=""
    countBEst=-1
    countWorst=20000
    WORST=""

    Olympcount=[]
    while True:
        lineI = file.readline()
        if not lineI:
            break
        splitLineI = lineI.split('\t')
        if splitLineI[7]==Countries:
            if splitLineI[8] not in Olympcount:
                Olympcount.append(splitLineI[8])

            if FirstYear>int(splitLineI[9]):
                FirstYear=int(splitLineI[9])
                FirstPlace=splitLineI[11]

            if splitLineI[8] not in YearDict:
                YearDict[splitLineI[8]] = 0
            if splitLineI[14]!="NA\n" and splitLineI[14]!="NA":
                YearDict[splitLineI[8]]+=1

            if splitLineI[14]=="Gold\n":
                Gold += 1
            elif splitLineI[14]=="Silver\n":
                Silver+=1
            elif splitLineI[14]=="Bronze\n":
                Bronze+=1

    for i in YearDict:
        if YearDict[i]>countBEst:
            countBEst=YearDict.get(i)
            BEST=i
    for j in YearDict:
        if YearDict[j]<countWorst:
            countWorst=YearDict.get(j)
            WORST=j
    print("First place is "+FirstPlace)
    print("First year is "+str(FirstYear))
    print("most successfull "+BEST)
    print("Worst "+WORST)
    print("Average Gold is:"+str(Gold//len(Olympcount)))
    print("Average Silver is:"+str(Silver//len(Olympcount)))
    print("Average Bronze is:"+str(Bronze//len(Olympcount)))

#choice = sys.argv[1]





with open(args.File, "r") as file:
    file.readline()
    if args.command == "medals":
        medals()
    elif args.command == "total":
        total()
    elif args.command == "overall":
        overall()
    elif args.command == "interactive":
        interactive()
