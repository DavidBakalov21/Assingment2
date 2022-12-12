import sys

Rcountries = []
RYears = []


def medals():
    counter = 0
    medalCount = [0,0,0]
    country = sys.argv[2]
    year = sys.argv[3]
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

        if sys.argv[1] == "-medals":
            if splitLine[7] == sys.argv[2] and splitLine[9] == sys.argv[3] and counter < 10:
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
    yearTotal = sys.argv[2]
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
    YearDict={}
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

choice = sys.argv[1]





with open("data.tsv", "r") as file:
    file.readline()
    if choice == "-medals":
        medals()
    elif choice == "-total":
        total()
    elif choice == "":
        pass
    elif choice == "-interactive":
        interactive()
