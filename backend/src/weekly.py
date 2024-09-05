import mysql.connector


# #####################################################################################
class Weekly:

    def __init__(self, rentalid: int, noofweeks: int, startdate: int, returndate: int):
        self.__rentalid = rentalid
        self.__noofweeks = noofweeks
        self.__startdate = startdate
        self.__returndate = returndate

    def __str__(self):
        return f"""{self.__rentalid:<20} - {self.__noofweeks:<20} - {self.__startdate:<20} - {self.__returndate:<20}"""

    @property
    def rentalid(self):
        return self.__rentalid

    @property
    def noofweeks(self):
        return self.__noofweeks

    @property
    def startdate(self):
        return self.__startdate

    @property
    def returndate(self):
        return self.__returndate

    # #################### LOADING DATA FROM DATABASE ####################

    # -----------------------------------------------------------------------------------------------------------------
    def load(self, db_config : dict):
        my_db = mysql.connector.connect(host=db_config["hostname"], port=db_config["port"],
                                        user=db_config["user"], password=db_config["passwd"],
                                        database=db_config["database"])

        cursor = my_db.cursor()
        cursor.execute("SELECT RentalID, NoOfWeeks, StartDate, ReturnDate FROM car_rental.weekly WHERE id = %s", (self.__rentalid,))
        for row in cursor.fetchall():
            self.__rentalid = row[0]
            self.__noofweeks = row[1]
            self.__startdate = row[2]
            self.__returndate = row[3]

        cursor.close()
        my_db.close()

    # -----------------------------------------------------------------------------------------------------------------
    def load_all(db_config: dict) -> []:
        weeklys = []
        my_db = mysql.connector.connect(host=db_config["hostname"], port=db_config["port"],
                                        user=db_config["user"], password=db_config["passwd"],
                                        database=db_config["database"])
        cursor = my_db.cursor()

        cursor.execute("SELECT RentalID, NoOfWeeks, StartDate, ReturnDate FROM car_rental.weekly")
        for row in cursor.fetchall():
            weeklys.append(Weekly(rentalid=row[0], noofweeks=row[1], startdate=row[2], returndate=row[3]))
        cursor.close()

        my_db.close()
        return weeklys
