import pytest
from argparse import Namespace

from dealership.contracts import BuyContract, LeaseContract
from dealership.customers import Customer, Employee
from dealership.vehicles import Car, Truck, Motorcycle


@pytest.fixture
def fixtures():
    fix = Namespace()

    fix.car = Car(maker='Ford', model='Mustang', year=2005,
                   base_price=18000, miles=31000)
    fix.truck = Truck(maker='Chevrolet', model='Silverado', year=2014,
                       base_price=29000, miles=3000)
    fix.bike = Motorcycle(maker='Ducati', model='Monster',
                           year=2016, base_price=18000, miles=700)

    fix.customer = Customer('John', 'Doe', 'john@example.com')
    fix.employee = Employee('Jane', 'Doe', 'jane@example.com')
    return fix


def test_buy_contract_creation(fixtures):
    car_contract = BuyContract(
        vehicle=fixtures.car, customer=fixtures.customer, monthly_payments=6)

    assert car_contract.vehicle == fixtures.car
    assert car_contract.customer == fixtures.customer
    assert car_contract.monthly_payments == 6

    truck_contract = BuyContract(
        vehicle=fixtures.truck, customer=fixtures.customer, monthly_payments=12)

    assert truck_contract.vehicle == fixtures.truck
    assert truck_contract.customer == fixtures.customer
    assert truck_contract.monthly_payments == 12

    bike_contract = BuyContract(
        vehicle=fixtures.bike, customer=fixtures.customer, monthly_payments=36)

    assert bike_contract.vehicle == fixtures.bike
    assert bike_contract.customer == fixtures.customer
    assert bike_contract.monthly_payments == 36

def test_lease_contract_creation(fixtures):
    car_contract = LeaseContract(
        vehicle=fixtures.car, customer=fixtures.customer, length_in_months=12)

    assert car_contract.vehicle == fixtures.car
    assert car_contract.customer == fixtures.customer
    assert car_contract.length_in_months == 12

    truck_contract = LeaseContract(
        vehicle=fixtures.truck, customer=fixtures.customer, length_in_months=24)

    assert truck_contract.vehicle == fixtures.truck
    assert truck_contract.customer == fixtures.customer
    assert truck_contract.length_in_months == 24

    bike_contract = LeaseContract(
        vehicle=fixtures.bike, customer=fixtures.customer, length_in_months=36)

    assert bike_contract.vehicle == fixtures.bike
    assert bike_contract.customer == fixtures.customer
    assert bike_contract.length_in_months == 36

def test_buy_contract_total_value_with_customer(fixtures):
    # Buy contract with a Car
    car_contract = BuyContract(
        vehicle=fixtures.car, customer=fixtures.customer, monthly_payments=6)
    assert round(car_contract.total_value(), 2) == 22986.72

    truck_contract = BuyContract(
        vehicle=fixtures.truck, customer=fixtures.customer, monthly_payments=12)
    assert round(truck_contract.total_value(), 2) == 52580.48

    bike_contract = BuyContract(
        vehicle=fixtures.bike, customer=fixtures.customer, monthly_payments=36)
    assert round(bike_contract.total_value(), 2) == 27141.84

def test_buy_contract_monthly_value_with_customer(fixtures):
    # Buy contract with a Car
    car_contract = BuyContract(
        vehicle=fixtures.car, customer=fixtures.customer, monthly_payments=6)
    assert round(car_contract.monthly_value(), 2) == 3831.12

    truck_contract = BuyContract(
        vehicle=fixtures.truck, customer=fixtures.customer, monthly_payments=12)
    assert round(truck_contract.monthly_value(), 2) == 4381.71

    bike_contract = BuyContract(
        vehicle=fixtures.bike, customer=fixtures.customer, monthly_payments=36)
    assert round(bike_contract.monthly_value(), 2) == 753.94

def test_buy_contract_with_employees(fixtures):
    car_contract = BuyContract(
        vehicle=fixtures.car, customer=fixtures.employee, monthly_payments=6)

    assert round(car_contract.total_value(), 2) == 20688.05
    assert round(car_contract.monthly_value(), 2) == 3448.01

    truck_contract = BuyContract(
        vehicle=fixtures.truck, customer=fixtures.employee, monthly_payments=12)

    assert round(truck_contract.total_value(), 2) == 47322.43
    assert round(truck_contract.monthly_value(), 2) == 3943.54

    bike_contract = BuyContract(
        vehicle=fixtures.bike, customer=fixtures.employee, monthly_payments=36)

    assert round(bike_contract.total_value(), 2) == 24427.66
    assert round(bike_contract.monthly_value(), 2) == 678.55


def test_lease_contract_total_value_with_customer(fixtures):
    car_contract = LeaseContract(
        vehicle=fixtures.car, customer=fixtures.customer, length_in_months=12)
    assert round(car_contract.total_value(), 2) == 23760.0

    truck_contract = LeaseContract(
        vehicle=fixtures.truck, customer=fixtures.customer, length_in_months=24)
    assert round(truck_contract.total_value(), 2) == 49686.67

    bike_contract = LeaseContract(
        vehicle=fixtures.bike, customer=fixtures.customer, length_in_months=36)
    assert round(bike_contract.total_value(), 2) == 20350

def test_lease_contract_monthly_value_with_customer(fixtures):
    car_contract = LeaseContract(
        vehicle=fixtures.car, customer=fixtures.customer, length_in_months=12)
    assert round(car_contract.monthly_value(), 2) == 1980.0

    truck_contract = LeaseContract(
        vehicle=fixtures.truck, customer=fixtures.customer, length_in_months=24)
    assert round(truck_contract.monthly_value(), 2) == 2070.28

    bike_contract = LeaseContract(
        vehicle=fixtures.bike, customer=fixtures.customer, length_in_months=36)
    assert round(bike_contract.monthly_value(), 2) == 565.28


def test_lease_contract_with_employee(fixtures):
    car_contract = LeaseContract(
        vehicle=fixtures.car, customer=fixtures.employee, length_in_months=12)
    assert round(car_contract.total_value(), 2) == 21384
    assert round(car_contract.monthly_value(), 2) == 1782

    truck_contract = LeaseContract(
        vehicle=fixtures.truck, customer=fixtures.employee, length_in_months=24)
    assert round(truck_contract.total_value(), 2) == 44718
    assert round(truck_contract.monthly_value(), 2) == 1863.25

    bike_contract = LeaseContract(
        vehicle=fixtures.bike, customer=fixtures.employee, length_in_months=36)
    assert round(bike_contract.total_value(), 2) == 18315
    assert round(bike_contract.monthly_value(), 2) == 508.75
