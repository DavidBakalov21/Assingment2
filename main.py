Choice=input("Choose option")
counter=0
Rcountries=[]
RYears=[]
with open("athlete_events.csv", "r") as file:
    file.readline()


    Country=input("input country")
    Year=input("Input Year")
    while True:
        line1=file.readline()
        if not line1:
            break
        splitLine1=line1.split(",")
        Rcountries.append(splitLine1[6])
        RYears.append(splitLine1[9])

    file.seek(0)
    file.readline()
    if Year in RYears and Country in Rcountries:
        pass
    else:
        print("wrong")
        quit()
    while True:
        line=file.readline()
        if not line:
            break

        splitLine=line.split(",")

        if Choice=="-medals":
            if splitLine[6]==Country and splitLine[9]==Year and counter<10:
                name=splitLine[1]
                medal=splitLine[14]

                sport=splitLine[12]
                print("name:"+name)
                print("medal:"+medal)
                print("sport:"+sport)
                print("--------------")
                counter+=1


