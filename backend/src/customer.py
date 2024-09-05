import mysql.connector


# #####################################################################################
class Customer:

    def __init__(self, id: int, name: str, phone: str):
        self.__id = id
        self.__name = name
        self.__phone = phone

    def __str__(self):
        return f"""{self.name:<20} - {self.id:^10} - {self.phone:<50}"""

    @property
    def name(self):
        return self.__name

    @property
    def phone(self):
        return self.__phone

    @property
    def id(self):
        return self.__id

    # #################### LOADING DATA FROM DATABASE ####################

    # -----------------------------------------------------------------------------------------------------------------
    def load(self, db_config: dict):
        my_db = mysql.connector.connect(host=db_config["hostname"], port=db_config["port"],
                                        user=db_config["user"], password=db_config["passwd"],
                                        database=db_config["database"])

        cursor = my_db.cursor()
        cursor.execute("SELECT idNO, name, phone FROM car_rental.customer WHERE idNO = %s", (self.__id,))
        for row in cursor.fetchall():
            self.__id = row[0]
            self.__name = row[1]
            self.__phone = row[2]

        cursor.close()
        my_db.close()

    # -----------------------------------------------------------------------------------------------------------------
    def load_all(db_config: dict) -> []:
        customers = []
        my_db = mysql.connector.connect(host=db_config["hostname"], port=db_config["port"],
                                        user=db_config["user"], password=db_config["passwd"],
                                        database=db_config["database"])
        cursor = my_db.cursor()

        cursor.execute("SELECT idNO, name, phone FROM car_rental.customer")
        for row in cursor.fetchall():
            customer = (Customer(id=row[0], name=row[1], phone=row[2]))
            customer.load(db_config)
            customers.append(customer)
        cursor.close()

        my_db.close()
        return customers

    # -----------------------------------------------------------------------------------------------------------------
    def load_by_id(db_config: dict, cid: str) -> []:
        customers_by_id = []
        cid = int(cid)

        my_db = mysql.connector.connect(host=db_config["hostname"], port=db_config["port"],
                                        user=db_config["user"], password=db_config["passwd"],
                                        database=db_config["database"])

        cursor = my_db.cursor()

        cursor.execute("SELECT idNO, name, phone FROM car_rental.customer WHERE idNO like %s", (cid,))
        for row in cursor.fetchall():
            customer = (Customer(id=row[0], name=row[1], phone=row[2]))
            customer.load(db_config)
            customers_by_id.append(customer)

        cursor.close()
        my_db.close()
        return customers_by_id

    # -----------------------------------------------------------------------------------------------------------------
    def load_by_rental(db_config: dict):
        customers_by_rental = []

        my_db = mysql.connector.connect(host=db_config["hostname"], port=db_config["port"],
                                        user=db_config["user"], password=db_config["passwd"],
                                        database=db_config["database"])

        cursor = my_db.cursor()

        cursor.execute(
            "SELECT A.idNO, A.name, A.phone FROM car_rental.customer A WHERE A.idNO in (SELECT B.idNO FROM car_rental.rentals B WHERE A.idNO LIKE B.idNO) ")
        for row in cursor.fetchall():
            customer = (Customer(id=row[0], name=row[1], phone=row[2]))
            customer.load(db_config)
            customers_by_rental.append(customer)

        cursor.close()
        my_db.close()
        return customers_by_rental

    # -----------------------------------------------------------------------------------------------------------------
    def load_by_daily(db_config: dict):
        customers_by_daily = []

        my_db = mysql.connector.connect(host=db_config["hostname"], port=db_config["port"],
                                        user=db_config["user"], password=db_config["passwd"],
                                        database=db_config["database"])

        cursor = my_db.cursor()

        cursor.execute(
            "SELECT A.idNO, A.name, A.phone FROM car_rental.customer A WHERE A.idNO in (SELECT B.idNO FROM car_rental.rentals B WHERE A.idNO LIKE B.idNO AND RentalType LIKE 'Daily') ")
        for row in cursor.fetchall():
            customer = (Customer(id=row[0], name=row[1], phone=row[2]))
            customer.load(db_config)
            customers_by_daily.append(customer)

        cursor.close()
        my_db.close()
        return customers_by_daily

    # -----------------------------------------------------------------------------------------------------------------
    def load_by_weekly(db_config: dict):
        customers_by_weekly = []

        my_db = mysql.connector.connect(host=db_config["hostname"], port=db_config["port"],
                                        user=db_config["user"], password=db_config["passwd"],
                                        database=db_config["database"])
        cursor = my_db.cursor()

        cursor.execute(
            "SELECT A.idNO, A.name, A.phone FROM car_rental.customer A WHERE A.idNO in (SELECT B.idNO FROM car_rental.rentals B WHERE A.idNO LIKE B.idNO AND RentalType LIKE 'Weekly') ")
        for row in cursor.fetchall():
            customer = (Customer(id=row[0], name=row[1], phone=row[2]))
            customer.load(db_config)
            customers_by_weekly.append(customer)

        cursor.close()
        my_db.close()
        return customers_by_weekly

    # -----------------------------------------------------------------------------------------------------------------
    def update_customer(db_config: dict, cid: str, name: str, phone: str):
        customers = []
        cid = int(cid)

        my_db = mysql.connector.connect(host=db_config["hostname"], port=db_config["port"],
                                        user=db_config["user"], password=db_config["passwd"],
                                        database=db_config["database"])
        cursor = my_db.cursor()
        query = """UPDATE car_rental.customer SET Name = %s, Phone = %s WHERE idNO = %s"""
        input = (name, phone, cid)
        cursor.execute(query, input)
        my_db.commit()

        cursor.execute("SELECT idNO, name, phone FROM car_rental.customer")
        for row in cursor.fetchall():
            customer = (Customer(id=row[0], name=row[1], phone=row[2]))
            customer.load(db_config)
            customers.append(customer)
        cursor.close()

        my_db.close()
        return customers
