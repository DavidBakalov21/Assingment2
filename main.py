import sys

Rcountries = []
RYears = []


def medals():
    counter = 0
    medalCount = 0
    country = sys.argv[2]
    year = sys.argv[3]
    while True:
        line1 = file.readline()
        if not line1:
            break
        splitLine1 = line1.split('\t')

        if splitLine1[6] == country and splitLine1[14] != "NA":
            medalCount += 1
        Rcountries.append(splitLine1[6])
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
            if splitLine[6] == sys.argv[2] and splitLine[9] == sys.argv[3] and counter < 10:
                name = splitLine[1]
                medal = splitLine[14]

                sport = splitLine[12]
                print("name:" + name)
                print("medal:" + medal)
                print("sport:" + sport)
                print("--------------")
                counter += 1

    print("Country has" + str(medalCount))


def total():
    yearTotal = sys.argv[2]
    print(yearTotal)
    while True:
        lineTotal = file.readline()
        if not lineTotal:
            break
        splitLineTotal = lineTotal.split('\t')
        if splitLineTotal[14] != "NA" and yearTotal == splitLineTotal[9]:
            name = splitLineTotal[6]
            medal = splitLineTotal[14]
            print("name:" + name)
            print("medal:" + medal)
            print("--------------")



choice = sys.argv[1]
with open("data.tsv", "r") as file:
    file.readline()
    if choice == "-medals":
        medals()
    elif choice == "-total":
        total()
    elif choice == "":
        pass
    elif choice == "":
        pass
