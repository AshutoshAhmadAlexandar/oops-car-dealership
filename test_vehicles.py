import unittest

from dealership.vehicles import Car, Truck, Motorcycle

def test_car_creation():
    c = Car(maker='Ford', model='Mustang', year=2005,
            base_price=18000, miles=31000)

    assert c.maker == 'Ford'
    assert c.model == 'Mustang'
    assert c.year == 2005
    assert c.base_price == 18000
    assert c.miles == 31000

def test_truck_creation():
    t = Truck(maker='Chevrolet', model='Silverado', year=2014,
              base_price=29000, miles=3000)

    assert t.maker == 'Chevrolet'
    assert t.model == 'Silverado'
    assert t.year == 2014
    assert t.base_price == 29000
    assert t.miles == 3000

def test_motorcycle_creation():
    m = Motorcycle(maker='Ducati', model='Monster', year=2016,
                   base_price=18000, miles=700)

    assert m.maker == 'Ducati'
    assert m.model == 'Monster'
    assert m.year == 2016
    assert m.base_price == 18000
    assert m.miles == 700

def test_cars_sale_price():
    v1 = Car(maker='Ford', model='Mustang', year=2005,
             base_price=18000, miles=31000)
    v2 = Car(maker='Ford', model='Mustang', year=2014,
             base_price=31000, miles=11000)

    assert v1.sale_price() == 21600
    assert v2.sale_price() == 37200

def test_trucks_sale_price():
    v1 = Truck(maker='Chevrolet', model='Silverado', year=2014,
               base_price=29000, miles=3000)
    v2 = Truck(maker='Chevrolet', model='Silverado', year=2004,
               base_price=16000, miles=52000)

    assert v1.sale_price() == 46400
    assert v2.sale_price() == 25600

def test_motorcycle_sale_price():
    v1 = Motorcycle(maker='Ducati', model='Monster', year=2016,
                    base_price=18000, miles=700)
    v2 = Motorcycle(maker='Ducati', model='Monster', year=2009,
                    base_price=9000, miles=11400)

    assert v1.sale_price() == 19800
    assert v2.sale_price() == 9900


def test_cars_purchase_price():
    v1 = Car(maker='Ford', model='Mustang', year=2005,
             base_price=18000, miles=31000)
    v2 = Car(maker='Ford', model='Mustang', year=2014,
             base_price=31000, miles=11000)

    assert v1.purchase_price() == 21476
    assert v2.purchase_price() == 37156


def test_trucks_purchase_price():
    v1 = Truck(maker='Chevrolet', model='Silverado', year=2014,
               base_price=29000, miles=3000)
    v2 = Truck(maker='Chevrolet', model='Silverado', year=2004,
               base_price=16000, miles=52000)

    assert v1.purchase_price() == 46340
    assert v2.purchase_price() == 24560


def test_motorcycle_purchase_price():
    v1 = Motorcycle(maker='Ducati', model='Monster', year=2016,
                    base_price=18000, miles=700)
    v2 = Motorcycle(maker='Ducati', model='Monster', year=2009,
                    base_price=9000, miles=11400)

    assert v1.purchase_price() == 19793.7
    assert v2.purchase_price() == 9797.4
