from drink_module import barmanagement

drinks = barmanagement()
BarDB = {}

AMOUNTLIST = []
QTY = []
BRANDS = []

sqa = [0, ]
Soft_instock = [0, ]

jqa = [0, ]
Juice_instock = [0, ]

bqa = [0, ]
BEER_instock = [0, ]

wqa = [0, ]
WINE_instock = [0, ]

spqa = [0, ]
SPIRITS_instock = [0, ]

btqa = [0, ]
BITTERS_instock = [0, ]

InitialQuantity_instock = [0, ]

while True:
    print("\nADD ITEMS= 1\nRECORD SALES ENTER= 2\nVIEW SALES INFO ENTER = 3\nVIEW TOTAL SALES =4\nCUSTOMERS RECEIPT=5")
    brandlist = ["coke", "fanta", "sprite", "originzero", "sevenup", "mirinda", "teem", "maltina",
                 "amstelmalta", "maltaguiness", "dubicmalt", "fivealive", "fuman", "chivitanecta", "chivitaapple",
                 "star", "gulder", "lifebeer", "guinessbeer", "stout", "trophy", "heineken", "tigerbeer", "boudweiser",
                 "starradler", "alomobitters", "adonkobitters", "campari", "eva", "champagne", "spamante", "veleta",
                 "chelsea", "originbitters", "squardron", "londonbest", "amarula", "baileys", "americanhoney", "pepsi",
                 "origin", "goldberg", "harp", "brandy"]

    Dict = {"coke": 200, "fanta": 200, "sprite": 200, "amstelmalta": 400, "originzero": 250, "sevenup": 200,
            "mirinda": 200, "teem": 200, "maltina": 400, "maltaguiness": 300, "dubicmalt": 300, "fivealive": 400,
            "fuman": 400, "chivitanecta": 400, "chivitaapple": 400, "star": 500, "gulder": 500, "lifebeer": 500,
            "guinessbeer": 500, "stout": 500, "trophy": 500, "heineken": 500, "tigerbeer": 500, "boudweiser": 500,
            "starradler": 500, "alomobitters": 250, "adonkobitters": 250, "campari": 2000, "eva": 2000, "pepsi": 200,
            "champagne": 20000, "spamante": 2000, "veleta": 2000, "chelsea": 1500, "originbitters": 250,
            "squardron": 2500, "londonbest": 2000, "amarula": 5000, "baileys": 20000, "american honey": 2000,
            "origin": 500, "goldberg": 500, "harp": 500, "brandy": 15000}

    i = input("\ndo you want to confirm item cost?:yes/no:")
    if i == "yes" and i != "no":
        br = input("\nBrand:")
        b = br in Dict
        while b == False:
            print("Sorry brand does not exist...")
            br = input("\nBrand:")
            b = br in Dict
        else:
            pass
        br = Dict[br]
        print("Cost:NGN{}".format(br))
    elif i == "no" and i != "yes":
        pass

    reply = input("\n proceed? yes/no:")
    if reply == "yes" and reply != "no":
        pass
    elif reply != "yes" and reply == "no":
        continue

    option = input("\nEnter Option:")
    if option == "1":
        print('INPUT ZERO IF QUANTITY IN STOCK REQUIRES NO ADJUSTMENT\n'
              'FOR REDUCTION ENTER A NEGATIVE INTEGER=-n')
        SI_instock = int(input("SOFT in stock:"))
        Soft_instock.append(SI_instock)
        JI_instock = int(input("JUICE in stock:"))
        Juice_instock.append(JI_instock)
        IB_instock = int(input("BEER in stock:"))
        BEER_instock.append(IB_instock)
        IW_instock = int(input("WINE in stock:"))
        WINE_instock.append(IW_instock)
        SP_instock = int(input("SPIRITS in stock:"))
        SPIRITS_instock.append(SP_instock)
        BI_instock = int(input("BITTERS in stock:"))
        BITTERS_instock.append(BI_instock)

        LISTTOTAL = [SI_instock, JI_instock, IB_instock, IW_instock, SP_instock, BI_instock]
        szlt = len(LISTTOTAL)
        sumszlt = sum(LISTTOTAL[0:szlt])
        print('TOTAL:{}'.format(sumszlt))

        InitialQuantity_instock = [0, ]
        print('INSERT NEW TOTAL STOCK QTY')
        IQ_instock = int(input("IQ_instock:"))
        InitialQuantity_instock.append(IQ_instock)

        if IQ_instock != sumszlt:
            print('WRONG ENTRY/YOU CANNOT GO FURTHER')
            continue
        elif IQ_instock == 0:
            print('EMPTY STOCK')
            continue
        else:
            pass

        drinks.stockquantityINFO(SI_instock, JI_instock, IB_instock, IW_instock, SP_instock, BI_instock)

    elif option == "2":
        brandlist = []
        brandl = input("enter brand:")
        brandlist.append(brandl)
        drinks.itemINFO(brandl)

    elif option == "3":
        sz = len(brandlist)
        print("No. of brands are:{}".format(sz))
        sz = len(AMOUNTLIST)
        if sz == 1 or sz == 0:
            print("No. OF SALES MADE:{}SALE".format(sz))
        elif sz > 1:
            print("No. OF SALES MADE:{}SALES".format(sz))
        drinklist = ["SOFT", "JUICE", "BEER", "WINE", "SPIRITS", "BITTERS"]
        print("\nDRINK TYPES:", drinklist)
        sN = int(input("Sales Number:"))
        print('ENTER IN UPPERCASE')
        dT = input("drink type:")
        if dT in drinklist:
            pass

        elif dT not in drinklist:
            print("DRINK TYPE NOT IN STOCK \nPLEASE RE-ENTER DRINK TYPE")
            dT = input("drink type:")
            if dT not in drinklist:
                print("WRONG AGAIN...")
                continue

        print('ENTER IN LOWERCASE')
        bR = input("brand:")
        if bR in brandlist:
            BRANDS.append(bR)
            pass
        elif bR not in brandlist:
            print("BRAND NOT IN STOCK\nPLEASE RE-ENTER DRINK TYPE IN LOWERCASE")
            bR = input("brand:")
            if bR in brandlist:
                BRANDS.append(bR)
                pass
            elif bR not in brandlist:
                print("WRONG AGAIN...")
                continue
        br = input("\nCONFIRM Brand:")
        if br == bR:
            pass
        else:
            print("CONFIRMATION ERROR!!!")
            continue
        br = Dict[br]

        cT = int(input("Cost_NGN:"))
        if cT == br:
            pass
        else:
            print("WRONG ENTRY PLEASE CONFIRM PRICE")
            cT = int(input("Cost_NGN:"))
            if cT == br:
                pass
            else:
                continue

        qA = int(input("Quantity:"))
        QTY.append(qA)
        aM = cT * qA
        print("Amount_NGN:{:.2f}".format(aM))
        aM = int(input("Amount_NGN:"))
        AMOUNTLIST.append(aM)
        aP = int(input("Actual payment by customer:"))
        bL = aP - aM
        print("Balance_NGN:{:.2f}".format(bL))
        if bL < 0:
            print("THE CUSTOMER HAS UNDER PAID\n ASK FOR BALANCE")
        bL = int(input("Balance_NGN:"))
        cO = input("Comment:")

        drinks.recordinfo(sN, dT, bR, aP, cT, qA, aM, bL, cO)

        if sN not in BarDB:
            BarDB[sN] = drinks
        else:
            print("Sales Number already exist in database\n please edit entry\n OR info may not be callable")
        print("\n***STOCK CONTROL***")
        szq = len(QTY)
        SQ = sum(QTY[0:szq])
        IQZ = len(InitialQuantity_instock)
        Q = sum(InitialQuantity_instock[0:IQZ])
        CurrentQTY_instock = Q - SQ
        if Q >= SQ and Q >= qA:
            print("TOTAL Volumes Sold:{}".format(SQ))
            print("CurrentQTY in stock:{:.2f}".format(CurrentQTY_instock))
        elif CurrentQTY_instock <= (0.25 * Q) or CurrentQTY_instock == 0:
            print("75%+ SHORT\nPLEASE RE-STOCK")

        if dT == "SOFT":
            szi = len(Soft_instock)
            Qs = sum(Soft_instock[0:szi])
            sqa.append(qA)
            szqa = len(sqa)
            ssqa = sum(sqa[0:szqa])
            qs = Qs - ssqa
            if Qs >= ssqa:
                print("Quantity of Soft in stock:{}".format(qs))
            elif qs <= (0.25 * Qs) or qs == 0:
                print("PLEASE RESTOCK\n75%+ OF SOFT IN STOCK SOLD")

        elif dT == "JUICE":
            szj = len(Juice_instock)
            Qj = sum(Juice_instock[0:szj])
            jqa.append(qA)
            szja = len(jqa)
            sjqa = sum(jqa[0:szja])
            qj = Qj - sjqa
            if Qj >= sjqa:
                print("Quantity of Juice in stock:{}".format(qj))
            elif qj <= (0.25 * Qj) or qj == 0:
                print("PLEASE RESTOCK\n75% OR MORE OF JUICE IN STOCK SOLD")

        elif dT == "BEER":
            szb = len(BEER_instock)
            Qb = sum(BEER_instock[0:szb])
            bqa.append(qA)
            szbq = len(bqa)
            ssbq = sum(bqa[0:szbq])
            qb = Qb - ssbq
            if Qb >= ssbq:
                print("Quantity of BEER in stock:{}".format(qb))
            elif qb <= (0.25 * Qb) or qb == 0:
                print("PLEASE RESTOCK\n75% OR MORE OF BEER IN STOCK SOLD")

        elif dT == "WINE":
            szi = len(WINE_instock)
            Qi = sum(WINE_instock[0:szi])
            wqa.append(qA)
            szw = len(wqa)
            swqa = sum(wqa[0:szw])
            qi = Qi - swqa
            if Qi >= swqa:
                print("Quantity of WINE in stock:{}".format(qi))
            elif qi <= (0.25 * Qi) or qi == 0:
                print("PLEASE RESTOCK\n75% OR MORE OF WINE IN STOCK SOLD")

        elif dT == "SPIRITS":
            szp = len(SPIRITS_instock)
            Qsp = sum(SPIRITS_instock[0:szp])
            spqa.append(qA)
            szzp = len(spqa)
            sspqa = sum(spqa[0:szzp])
            qsp = Qsp - sspqa
            if Qsp >= sspqa:
                print("Quantity of SPIRITS in sock:{}".format(qsp))
            elif qsp <= (0.25 * Qsp) or qsp == 0:
                print("PLEASE RESTOCK\n75% OR MORE OF SPIRITS IN STOCK SOLD")

        elif dT == "BITTERS":
            szbi = len(BITTERS_instock)
            Qbi = sum(BITTERS_instock[0:szbi])
            btqa.append(qA)
            szbt = len(btqa)
            sszbt = sum(btqa[0:szbt])
            qbi = Qbi - sszbt
            if Qbi >= sszbt:
                print("Quantity of BITTERS in stock:{}".format(qbi))
            elif qbi <= (0.25 * Qbi) or qbi == 0:
                print("PLEASE RESTOCK\n75% OR MORE OF BITTERS IN STOCK SOLD")

    elif option == "4":
        print("***WELCOME***\n")
        sN = int(input("Sales Number:"))
        print("\n***DISPLAYING SALES INFO***")
        drinkss = BarDB[sN]
        drinkss.displayinfo()

    elif option == "5":
        print("****SALES ANALYSIS***")
        drinks.stock_allanalysis()
        print("\nCURRENT QUANTITY SOLD BASED ON DRINK TYPES:")
        print('SOFT DRINKS')
        szqa = len(sqa)
        for qA in sqa[0:szqa]:
            print('quantity sold:{}'.format(qA))
        ssqa = sum(sqa[0:szqa])
        print('TOTAL SOFT SOLD:{}'.format(ssqa))
        print('\nJUICE')
        szja = len(jqa)
        for qA in jqa[0:szja]:
            print("quantity sold:{}".format(qA))
        sjqa = sum(jqa[0:szja])
        print('TOTAL JUICE SOLD:{}'.format(sjqa))
        print('\nBEER')
        szbq = len(bqa)
        for qA in bqa[0:szbq]:
            print('quantity sold:{}'.format(qA))
        ssbq = sum(bqa[0:szbq])
        print('TOTAL BEER SOLD:{}'.format(ssbq))
        print('\nWINE')
        szw = len(wqa)
        for qA in wqa[0:szw]:
            print('quantity SOLD:{}'.format(qA))
        swqa = sum(wqa[0:szw])
        print('TOTAL WINE SOLD:{}'.format(swqa))
        print('\nSPIRITS')
        szzp = len(spqa)
        for qA in spqa[0:szzp]:
            print('quantity SOLD:{}'.format(qA))
        sspqa = sum(spqa[0:szzp])
        print('TOTAL SPIRITS SOLD:{}'.format(sspqa))
        print('\nBITTERS')
        szbt = len(btqa)
        for qA in btqa[0:szbt]:
            print('quantity SOLD:{}'.format(qA))
        sszbt = sum(btqa[0:szbt])
        print('TOTAL BITTERS SOLD:{}'.format(sszbt))
        szq = len(QTY)
        SC = sum(QTY[0:szq])

        sz = len(AMOUNTLIST)
        j = sum(AMOUNTLIST[0:sz])
        print("TOTAL AMOUNT AS AT CURRENT TIME AND DATE:NGN{}".format(j))
        print("\nTOTAL Volumes in stock Sold:{}".format(SC))














