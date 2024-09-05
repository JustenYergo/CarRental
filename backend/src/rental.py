import mysql.connector


# #####################################################################################
class Rental:

    def __init__(self, rentalid: int, weeklyrate: int, dailyrate: int, amtdue: int, rtype: str, idno: int, vehicleid: int):
        self.__rentalid = rentalid
        self.__weeklyrate = weeklyrate
        self.__dailyrate = dailyrate
        self.__amtdue = amtdue
        self.__rtype = rtype
        self.__idno = idno
        self.__vehicleid = vehicleid

    def __str__(self):
        return f"""{self.__rentalid:<20} - {self.__weeklyrate:<20} - {self.__dailyrate:<20} - {self.__amtdue:<20} - {self.__rtype:<20} - {self.__idno:<20} - {self.__vehicleid:<20}"""

    @property
    def rentalid(self):
        return self.__rentalid

    @property
    def weeklyrate(self):
        return self.__weeklyrate

    @property
    def dailyrate(self):
        return self.__dailyrate

    @property
    def amtdue(self):
        return self.__amtdue

    @property
    def rtype(self):
        return self.__rtype

    @property
    def idno(self):
        return self.__idno

    @property
    def vehicleid(self):
        return self.__vehicleid

    # #################### LOADING DATA FROM DATABASE ####################

    # -----------------------------------------------------------------------------------------------------------------
    def load(self, db_config : dict):
        my_db = mysql.connector.connect(host=db_config["hostname"], port=db_config["port"],
                                        user=db_config["user"], password=db_config["passwd"],
                                        database=db_config["database"])

        cursor = my_db.cursor()
        cursor.execute("SELECT RentalID, WeeklyRate, DailyRate, AmtDue, RentalType, IDNo, VehicleID FROM car_rental.rentals WHERE RentalID = %s", (self.__rentalid,))
        for row in cursor.fetchall():
            self.__rentalid = row[0]
            self.__weeklyrate = row[1]
            self.__dailyrate = row[2]
            self.__amtdue = row[3]
            self.__rtype = row[4]
            self.__idno = row[5]
            self.__vehicleid = row[6]

        cursor.close()
        my_db.close()

    # -----------------------------------------------------------------------------------------------------------------
    def load_all(db_config: dict) -> []:
        rentals = []
        my_db = mysql.connector.connect(host=db_config["hostname"], port=db_config["port"],
                                        user=db_config["user"], password=db_config["passwd"],
                                        database=db_config["database"])
        cursor = my_db.cursor()

        cursor.execute("SELECT RentalID, WeeklyRate, DailyRate, AmtDue, RentalType, IDNo, VehicleID FROM car_rental.rentals")
        for row in cursor.fetchall():
            rentals.append(Rental(rentalid=row[0], weeklyrate=row[1], dailyrate=row[2], amtdue=row[3], rtype=row[4], idno=row[5], vehicleid=row[6]))
        cursor.close()

        my_db.close()
        return rentals




    # -----------------------------------------------------------------------------------------------------------------
    def load_by_daily(db_config: dict):
        rentals_by_daily = []

        my_db = mysql.connector.connect(host=db_config["hostname"], port=db_config["port"],
                                        user=db_config["user"], password=db_config["passwd"],
                                        database=db_config["database"])
        cursor = my_db.cursor()

        cursor.execute("SELECT A.RentalID, A.WeeklyRate, A.DailyRate, A.AmtDue, A.RentalType, A.IDNo, A.VehicleID FROM car_rental.rentals A WHERE (SELECT B.RentalID FROM car_rental.daily B WHERE A.RentalID LIKE B.RentalID)")
        for row in cursor.fetchall():
            rental = (Rental(rentalid=row[0], weeklyrate=row[1], dailyrate=row[2], amtdue=row[3], rtype=row[4], idno=row[5], vehicleid=row[6]))
            rental.load(db_config)
            rentals_by_daily.append(rental)

        cursor.close()
        my_db.close()
        return rentals_by_daily

    # -----------------------------------------------------------------------------------------------------------------
    def load_by_weekly(db_config: dict):
        rentals_by_weekly = []

        my_db = mysql.connector.connect(host=db_config["hostname"], port=db_config["port"],
                                            user=db_config["user"], password=db_config["passwd"],
                                            database=db_config["database"])
        cursor = my_db.cursor()

        cursor.execute(
                "SELECT A.RentalID, A.WeeklyRate, A.DailyRate, A.AmtDue, A.RentalType, A.IDNo, A.VehicleID FROM car_rental.rentals A WHERE (SELECT B.RentalID FROM car_rental.weekly B WHERE A.RentalID LIKE B.RentalID)")
        for row in cursor.fetchall():
            rental = (Rental(rentalid=row[0], weeklyrate=row[1], dailyrate=row[2], amtdue=row[3], rtype=row[4],
                                 idno=row[5], vehicleid=row[6]))
            rental.load(db_config)
            rentals_by_weekly.append(rental)

        cursor.close()
        my_db.close()
        return rentals_by_weekly

