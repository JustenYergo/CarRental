from car import Car
from customer import Customer
from daily import Daily
from rental import Rental
from weekly import Weekly


class Car_Rental:
    DB = {
        "hostname": "localhost",
        "port": 3306,
        "user": "root",
        "passwd": "",
        "database": "car_rental"
    }

    def __init__(self, name: str):
        self.__name = name
        self.__customers = []
        self.__cars = []

    @property
    def name(self):
        return self.__name

    def __str__(self):
        return """{} Car Rental with {} customers and {} cars.""".format(self.__name, len(self.__customers),
                                                                         len(self.__cars))
        pass

    # #################### LOADING DATA FROM DATABASE ####################
    # #################### CUSTOMER BLOCK ####################
    def load_all_customers(self) -> []:
        return Customer.load_all(self.DB)

    def load_customers_by_id(self, cid: str):
        return Customer.load_by_id(self.DB, cid)

    def update_customer_by_id(self, cid: str, name: str, phone: str):
        return Customer.update_customer(self.DB, cid, name, phone)

    def load_customers_by_rental(self):
        return Customer.load_by_rental(self.DB)

    def load_customers_by_daily(self):
        return Customer.load_by_daily(self.DB)

    def load_customers_by_weekly(self):
        return Customer.load_by_weekly(self.DB)

    # #################### CAR BLOCK ####################
    def load_all_cars(self):
        cars = Car.load_all(self.DB)
        return [car.to_json() for car in cars]

    def load_cars_by_make(self, model: str):
        return Car.load_all_by_make(self.DB, model)
    
    def load_cars_by_location(self, location: str):
        cars = Car.load_all_by_location(self.DB, location)
        return [car.to_json() for car in cars]

    def load_cars_by_available(self):
        return Car.load_all_available(self.DB)

    def load_cars_by_rental(self):
        return Car.load_by_rental(self.DB)

    def load_cars_by_daily(self):
        return Car.load_by_daily(self.DB)

    def load_cars_by_weekly(self):
        return Car.load_by_weekly(self.DB)

    def update_cars_by_id(self, vehicleid, year, model, isavailable, ctype, dailyrate, weeklyrate):
        return Car.update_cars(self.DB, vehicleid, year, model, isavailable, ctype, dailyrate, weeklyrate)

    # #################### RENTAL BLOCK ####################
    def load_all_rentals(self):
        return Rental.load_all(self.DB)

    def load_rentals_by_daily(self):
        return Rental.load_by_daily(self.DB)

    def load_rentals_by_weekly(self):
        return Rental.load_by_weekly(self.DB)

    # #################### DAILY BLOCK ####################
    def load_all_daily(self):
        return Daily.load_all(self.DB)

    # #################### WEEKLY BLOCK ####################
    def load_all_weekly(self):
        return Weekly.load_all(self.DB)
