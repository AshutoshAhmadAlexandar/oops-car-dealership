.PHONY: step_1 step_2 step_3

step_1:
	py.test test_vehicles.py --tb=short -k test_car_creation

step_2:
	py.test test_vehicles.py --tb=short -k test_truck_creation

step_3:
	py.test test_vehicles.py --tb=short -k test_motorcycle_creation

step_4:
	py.test test_vehicles.py -k test_cars_sale_price

step_5:
	py.test test_vehicles.py -k test_trucks_sale_price

step_6:
	py.test test_vehicles.py -k test_motorcycle_sale_price

step_7:
	py.test test_vehicles.py -k test_cars_purchase_price

step_8:
	py.test test_vehicles.py -k test_trucks_purchase_price

step_9:
	py.test test_vehicles.py -k test_motorcycle_purchase_price

step_10:
	py.test test_contracts.py -k test_buy_contract_creation

step_11:
	py.test test_contracts.py -k test_lease_contract_creation

step_12:
	py.test test_contracts.py -k test_buy_contract_total_value_with_customer

step_13:
	py.test test_contracts.py -k test_buy_contract_monthly_value_with_customer

step_14:
	py.test test_contracts.py -k test_buy_contract_with_employees

step_15:
	py.test test_contracts.py -k test_lease_contract_total_value_with_customer

step_16:
	py.test test_contracts.py -k test_lease_contract_monthly_value_with_customer

step_17:
	py.test test_contracts.py -k test_lease_contract_with_employee
