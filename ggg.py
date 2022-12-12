with open("data.tsv", "r") as file:
    file.readline()

    FirstYear=20000
    FirstPlace=""
    Countries=input("Enter country")
    MostSucYear=""
    YearDict={}
    Gold=0
    Bronze=0
    Silver=0



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






    BEST=""
    countBEst=-1
    countWorst=20000
    WORST=""
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
    #print("________________")
    #print("most successfull "+max(YearDict, key=YearDict.get)+","+str(max(YearDict.values())))
    #print("worst one "+min(YearDict, key=YearDict.get)+","+str(min(YearDict.values())))


