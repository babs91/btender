import mysql.connector as mysql

class barmanagement:
    __barName = "****BAR"

    def stockquantityINFO(self, SI_instock, JI_instock, IB_instock, IW_instock, SP_instock, BI_instock):
        self.__SI_instock = SI_instock
        self.__JI_instock = JI_instock
        self.__IB_instock = IB_instock
        self.__IW_instock = IW_instock
        self.__SP_instock = SP_instock
        self.__BI_instock = BI_instock

        conn = mysql.connect(host="localhost", user="root", password="", database="QTY_database", charset="utf8")
        cur = conn.cursor()
        query = "INSERT INTO quantity_tb(SOFT_instock, JUICE_instock, BEER_instock, WINE_instock," \
                "SPIRIT_instock, BITTER_instock)Values('%d', '%d', '%d', '%d', '%d', '%d')"\
                %(SI_instock, JI_instock, IB_instock, IW_instock, SP_instock, BI_instock)
        cur.execute(query)
        conn.commit()

    def itemINFO(self, brandl):
        self.__brandl = brandl


    def recordinfo(self, salesNUM, drinkType, Brand, actualPayment, Cost_NGN, Quantity, Amount_NGN, Balance, comment):
        if Quantity > 0:
            self.__salesNUM = salesNUM
            self.__drinkType = drinkType
            self.__Brand = Brand
            self.__actualPayment = actualPayment
            self.__Cost_NGN = Cost_NGN
            self.__Quantity = Quantity
            self.__Amount_NGN = Amount_NGN
            self.__Balance = Balance
            self.__comment = comment

            conn = mysql.connect(host="localhost", user="root", password="", database="bar_database", charset="utf8")
            cur = conn.cursor()
            query = "INSERT INTO bar_tb(drinkType, Brand, actualPayment, Cost_NGN, Quantity, Amount_NGN, Balance, comment)"\
                    "Values('%s','%s','%d','%d','%d','%d','%d','%s')"\
                    % (drinkType, Brand, actualPayment, Cost_NGN, Quantity, Amount_NGN, Balance, comment)
            cur.execute(query)
            conn.commit()

        else:
            self.__salesNUM = 0
            self.__drinkType = "not available"
            self.__Brand = "not available"
            self.__actualPayment = 0
            self.__Cost_NGN = 0
            self.__Quantity = 0
            self.__Amount_NGN = 0
            self.__Balance = 0
            self.__comment = "not available"

    def getbarName(self):
        return barmanagement.__barName

    def getSalesNUM(self):
        return self.__salesNUM

    def displayinfo(self):
        "DISPLAYING ALL RECORDS"
        print("barName:%s\nsalesNUM:%d\ndrinkType:%s\nBrand:%s\nactualPayment_NGN:%d\nCost_NGN:%d\nQuantity:%d\nAmount_NGN:%d"
              "\nBalance:%d\ncomment:%s"%(barmanagement.__barName, self.__salesNUM, self.__drinkType, self.__Brand, self.__actualPayment,
               self.__Cost_NGN, self.__Quantity, self.__Amount_NGN, self.__Balance, self.__comment))

    def stock_allanalysis(self):
        conn = mysql.connect(host="localhost", user="root", password="", database="bar_database", charset="utf8")
        cur = conn.cursor()
        query = "SELECT * FROM bar_tb"
        cur.execute(query)
        result = cur.fetchall()

        for row in result:
            print(('%d\t\%s\t\%s\t\%d\t\%d\t\%d\t\%d\t\%d\t\%s\t%s\n')\
                  % (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))
        conn.close()































































