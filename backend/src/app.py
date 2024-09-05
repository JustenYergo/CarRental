from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
from car_rental import Car_Rental

app = Flask(__name__)
CORS(app)

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {"message": "Hello from Flask!"}
    return jsonify(data)


# # ----------------------------------------------------------------------------------------------------------------------
# @app.route('/')
# def home():
#     return render_template('home.html')


# # ----------------------------------------------------------------------------------------------------------------------
# @app.route('/customers_all')
# def customers_all():
#     report_title = "List of All Customers"
#     customers = car_rental.load_all_customers()
#     return render_template('customers.html', report_title=report_title, customers=customers)


# # ----------------------------------------------------------------------------------------------------------------------
# @app.route('/customers_search')
# def customers_search():
#     if request.args.get('idNO'):
#         report_title = "All Customers"
#         customers = car_rental.load_customers_by_id(request.args.get('idNO'))
#         return render_template('customers.html', report_title=report_title, customers=customers)
#     else:
#         return render_template('customer_search.html')


# # ----------------------------------------------------------------------------------------------------------------------
# @app.route('/customer_update')
# def customer_update():
#     if request.args.get('name'):
#         report_title = "All Customers"
#         customers = car_rental.update_customer_by_id(request.args.get('idNO'), request.args.get('name'), request.args.get('phone'))
#         return render_template('customers.html', report_title=report_title, customers=customers)
#     else:
#         return render_template('customer_update.html')


# # ----------------------------------------------------------------------------------------------------------------------
# @app.route('/cars_all')
# def cars_all():
#     report_title = "List of All Cars"
#     cars = car_rental.load_all_cars()
#     return render_template('cars.html', report_title=report_title, cars=cars)


# # ----------------------------------------------------------------------------------------------------------------------
# @app.route('/cars_available')
# def cars_available():
#     report_title = "List of All Available Cars"
#     cars = car_rental.load_cars_by_available()
#     return render_template('cars.html', report_title=report_title, cars=cars)


# # ----------------------------------------------------------------------------------------------------------------------
# @app.route('/car_search')
# def car_search():
#     if request.args.get('model'):
#         report_title = "All Cars"
#         cars = car_rental.load_cars_by_model(request.args.get('model'))
#         return render_template('cars.html', report_title=report_title, cars=cars)
#     else:
#         return render_template('car_search.html')


# # ----------------------------------------------------------------------------------------------------------------------
# @app.route('/car_update')
# def car_update():
#     if request.args.get('CarYear'):
#         report_title = "All Cars"
#         cars = car_rental.update_cars_by_id(request.args.get('VehicleID'), request.args.get('CarYear'), request.args.get('Model'), request.args.get('IsAvailable'), request.args.get('CarType'), request.args.get('DailyRate'), request.args.get('WeeklyRate'))
#         return render_template('cars.html', report_title=report_title, cars=cars)
#     else:
#         return render_template('car_update.html')


# # ----------------------------------------------------------------------------------------------------------------------
# @app.route('/rentals_all')
# def rentals_all():
#     report_title = "List of ALL Rentals"
#     rentals = car_rental.load_all_rentals()
#     customers = car_rental.load_customers_by_rental()
#     cars = car_rental.load_cars_by_rental()
#     return render_template('rentals.html', report_title=report_title, rentals=rentals, customers=customers, cars=cars)


# # ----------------------------------------------------------------------------------------------------------------------
# @app.route('/daily_all')
# def daily_all():
#     report_title = "List of ALL Daily Rentals"
#     dailys = car_rental.load_all_daily()
#     rentals = car_rental.load_rentals_by_daily()
#     customers = car_rental.load_customers_by_daily()
#     cars = car_rental.load_cars_by_daily()
#     return render_template('daily.html', report_title=report_title, dailys=dailys, rentals=rentals, customers=customers, cars=cars)


# # ----------------------------------------------------------------------------------------------------------------------
# @app.route('/weekly_all')
# def weekly_all():
#     report_title = "List of ALL Weekly Rentals"
#     weeklys = car_rental.load_all_weekly()
#     rentals = car_rental.load_rentals_by_weekly()
#     customers = car_rental.load_customers_by_weekly()
#     cars = car_rental.load_cars_by_weekly()
#     return render_template('weekly.html', report_title=report_title, weeklys=weeklys, rentals=rentals, customers=customers, cars=cars)

# # ######################################################################################################################
# # ######################################################################################################################
if __name__ == '__main__':
    app.run(debug=True)
