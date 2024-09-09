import mysql.connector

class Car:
    def __init__(self, vehicleid: int, year: int, model: str, isavailable: int, ctype: str, dailyrate: int,
                 weeklyrate: int, location: str):
        self.__vehicleid = vehicleid
        self.__year = year
        self.__model = model
        self.__isavailable = isavailable
        self.__ctype = ctype
        self.__dailyrate = dailyrate
        self.__weeklyrate = weeklyrate
        self.__location = location

    def __str__(self):
        return f"""{self.vehicleid:<20} - {self.year:^10} - {self.model:<50} - {self.isavailable:<20} - {self.ctype:<50} - {self.dailyrate:<50} - {self.weeklyrate:<50} - {self.location:<255}"""

    @property
    def vehicleid(self):
        return self.__vehicleid

    @property
    def year(self):
        return self.__year

    @property
    def model(self):
        return self.__model

    @property
    def isavailable(self):
        return self.__isavailable

    @property
    def ctype(self):
        return self.__ctype

    @property
    def dailyrate(self):
        return self.__dailyrate

    @property
    def weeklyrate(self):
        return self.__weeklyrate
    
    @property
    def location(self):
        return self.__location

    # #################### LOADING DATA FROM DATABASE ####################
    # -----------------------------------------------------------------------------------------------------------------
    def load(self, db_config: dict):
        my_db = mysql.connector.connect(host=db_config["hostname"], port=db_config["port"],
                                        user=db_config["user"], password=db_config["passwd"],
                                        database=db_config["database"])

        cursor = my_db.cursor()
        cursor.execute(
            "SELECT VehicleID, CarYear, Model, IsAvailable, CarType, DailyRate, WeeklyRate, Location FROM car_rental.car WHERE VehicleID = %s",
            (self.__vehicleid,))
        for row in cursor.fetchall():
            self.__vehicleid = row[0]
            self.__year = row[1]
            self.__model = row[2]
            self.__isavailable = row[3]
            self.__ctype = row[4]
            self.__dailyrate = row[5]
            self.__weeklyrate = row[6]
            self.__location = row[7]

        cursor.close()
        my_db.close()

    # -----------------------------------------------------------------------------------------------------------------
    def load_all(db_config: dict) -> []:
        cars = []

        my_db = mysql.connector.connect(host=db_config["hostname"], port=db_config["port"],
                                        user=db_config["user"], password=db_config["passwd"],
                                        database=db_config["database"])

        cursor = my_db.cursor()
        cursor.execute(
            "SELECT VehicleID, CarYear, Model, IsAvailable, CarType, DailyRate, WeeklyRate, Location FROM car_rental.car")
        for row in cursor.fetchall():
            cars.append(
                Car(vehicleid=row[0], year=row[1], model=row[2], isavailable=row[3], ctype=row[4], dailyrate=row[5],
                    weeklyrate=row[6], location=row[7]))

        cursor.close()
        my_db.close()
        return cars

    # -----------------------------------------------------------------------------------------------------------------
    def load_all_by_model(db_config: dict, model: str) -> []:
        cars_by_model = []
        my_db = mysql.connector.connect(host=db_config["hostname"], port=db_config["port"],
                                        user=db_config["user"], password=db_config["passwd"],
                                        database=db_config["database"])

        cursor = my_db.cursor()
        cursor.execute(
            "SELECT VehicleID, CarYear, Model, IsAvailable, CarType, DailyRate, WeeklyRate, Location FROM car_rental.car WHERE upper(Model) like %s",
            (model,))
        for row in cursor.fetchall():
            car = (Car(vehicleid=row[0], year=row[1], model=row[2], isavailable=row[3], ctype=row[4], dailyrate=row[5],
                    weeklyrate=row[6], location=row[7]))
            car.load(db_config)
            cars_by_model.append(car)
        cursor.close()
        my_db.close()
        return cars_by_model
    
    # -----------------------------------------------------------------------------------------------------------------
    def load_all_by_location(db_config: dict, location: str) -> []:
        cars_by_location = []
        my_db = mysql.connector.connect(host=db_config["hostname"], port=db_config["port"],
                                        user=db_config["user"], password=db_config["passwd"],
                                        database=db_config["database"])

        cursor = my_db.cursor()
        cursor.execute(
            "SELECT VehicleID, CarYear, Model, IsAvailable, CarType, DailyRate, WeeklyRate, Location FROM car_rental.car WHERE Location like %s",
            (location,))
        for row in cursor.fetchall():
            car = (Car(vehicleid=row[0], year=row[1], model=row[2], isavailable=row[3], ctype=row[4], dailyrate=row[5],
                    weeklyrate=row[6], location=row[7]))
            car.load(db_config)
            cars_by_location.append(car)
        cursor.close()
        my_db.close()
        return cars_by_location

    # -----------------------------------------------------------------------------------------------------------------\
    def load_all_available(db_config: dict):
        cars_available = []

        my_db = mysql.connector.connect(host=db_config["hostname"], port=db_config["port"],
                                        user=db_config["user"], password=db_config["passwd"],
                                        database=db_config["database"])

        cursor = my_db.cursor()
        cursor.execute(
            "SELECT VehicleID, CarYear, Model, IsAvailable, CarType, DailyRate, WeeklyRate, Location FROM car_rental.car WHERE isAvailable like 1")
        for row in cursor.fetchall():
            car = (Car(vehicleid=row[0], year=row[1], model=row[2], isavailable=row[3], ctype=row[4], dailyrate=row[5],
                    weeklyrate=row[6], location=row[7]))
            car.load(db_config)
            cars_available.append(car)
        cursor.close()
        my_db.close()
        return cars_available

    # -----------------------------------------------------------------------------------------------------------------\
    def load_by_rental(db_config: dict):
        cars_by_rental = []

        my_db = mysql.connector.connect(host=db_config["hostname"], port=db_config["port"],
                                        user=db_config["user"], password=db_config["passwd"],
                                        database=db_config["database"])

        cursor = my_db.cursor()
        cursor.execute(
            "SELECT A.VehicleID, A.CarYear, A.Model, A.IsAvailable, A.CarType, A.DailyRate, A.WeeklyRate A.Location FROM car_rental.car A WHERE (SELECT B.VehicleID FROM car_rental.rentals B WHERE A.VehicleID like B.VehicleID)")
        for row in cursor.fetchall():
            car = (Car(vehicleid=row[0], year=row[1], model=row[2], isavailable=row[3], ctype=row[4], dailyrate=row[5],
                       weeklyrate=row[6], location=row[7]))
            car.load(db_config)
            cars_by_rental.append(car)
        cursor.close()
        my_db.close()
        return cars_by_rental

    # -----------------------------------------------------------------------------------------------------------------\
    def load_by_daily(db_config: dict):
        cars_by_daily = []

        my_db = mysql.connector.connect(host=db_config["hostname"], port=db_config["port"],
                                        user=db_config["user"], password=db_config["passwd"],
                                        database=db_config["database"])

        cursor = my_db.cursor()
        cursor.execute("SELECT A.VehicleID, A.CarYear, A.Model, A.IsAvailable, A.CarType, A.DailyRate, A.WeeklyRate, A.Location FROM car_rental.car A WHERE (SELECT B.VehicleID FROM car_rental.rentals B WHERE A.VehicleID like B.VehicleID AND RentalType LIKE 'Daily')")
        for row in cursor.fetchall():
            car = (Car(vehicleid=row[0], year=row[1], model=row[2], isavailable=row[3], ctype=row[4], dailyrate=row[5],
                       weeklyrate=row[6], location=row[7]))
            car.load(db_config)
            cars_by_daily.append(car)
        cursor.close()
        my_db.close()
        return cars_by_daily

    # -----------------------------------------------------------------------------------------------------------------\
    def load_by_weekly(db_config: dict):
        cars_by_weekly = []

        my_db = mysql.connector.connect(host=db_config["hostname"], port=db_config["port"],
                                            user=db_config["user"], password=db_config["passwd"],
                                            database=db_config["database"])

        cursor = my_db.cursor()
        cursor.execute(
                "SELECT A.VehicleID, A.CarYear, A.Model, A.IsAvailable, A.CarType, A.DailyRate, A.WeeklyRate, A.Location FROM car_rental.car A WHERE (SELECT B.VehicleID FROM car_rental.rentals B WHERE A.VehicleID like B.VehicleID AND RentalType LIKE 'Weekly')")
        for row in cursor.fetchall():
            car = (
                    Car(vehicleid=row[0], year=row[1], model=row[2], isavailable=row[3], ctype=row[4], dailyrate=row[5],
                        weeklyrate=row[6], location=row[7]))
            car.load(db_config)
            cars_by_weekly.append(car)
        cursor.close()
        my_db.close()
        return cars_by_weekly

    # -----------------------------------------------------------------------------------------------------------------\
    def update_cars(db_config: dict, vehicleid: str, year: str, model: str, isavailable: str, ctype: str, dailyrate: str, weeklyrate: str, location: str):
        cars = []
        vehicleid = int(vehicleid)
        year = int(year)
        isavailable = int(isavailable)
        dailyrate = int(dailyrate)
        weeklyrate = int(weeklyrate)

        my_db = mysql.connector.connect(host=db_config["hostname"], port=db_config["port"],
                                        user=db_config["user"], password=db_config["passwd"],
                                        database=db_config["database"])
        cursor = my_db.cursor()
        query = """UPDATE car_rental.car SET CarYear = %s, Model = %s, IsAvailable = %s, CarType = %s, DailyRate = %s, WeeklyRate = %s, Location = %s WHERE VehicleID = %s"""
        input = (year, model, isavailable, ctype, dailyrate, weeklyrate, vehicleid)
        cursor.execute(query, input)
        my_db.commit()

        cursor.execute(
            "SELECT VehicleID, CarYear, Model, IsAvailable, CarType, DailyRate, WeeklyRate, Location FROM car_rental.car")
        for row in cursor.fetchall():
            car = (
                Car(vehicleid=row[0], year=row[1], model=row[2], isavailable=row[3], ctype=row[4], dailyrate=row[5],
                    weeklyrate=row[6], location=row[7]))
            car.load(db_config)
            cars.append(car)

        cursor.close()
        my_db.close()
        return cars  
      
    # -----------------------------------------------------------------------------------------------------------------\
    def to_json(self):
        return {
            'vehicleid': self.vehicleid,
            'year': self.year,
            'model': self.model,
            'isavailable': self.isavailable,
            'ctype': self.ctype,
            'dailyrate': self.dailyrate,
            'weeklyrate': self.weeklyrate,
            'location': self.location
        }
