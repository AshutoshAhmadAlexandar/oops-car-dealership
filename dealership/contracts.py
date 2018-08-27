class Contract(object):
    def __init__(self, vehicle, customer):
        self.vehicle = vehicle
        self.customer = customer

    def total_value(self):
        value = self._real_total_value()

        if self.customer.is_employee():
            return value * .9
        return value

    def monthly_value(self):
        return self.total_value() / getattr(self, self.MONTHLY_ATTR_NAME)


class BuyContract(Contract):
    MONTHLY_ATTR_NAME = 'monthly_payments'
    
    def __init__(self, vehicle, customer, monthly_payments):
        super().__init__(vehicle, customer)
        self.monthly_payments = monthly_payments
        
    def _real_total_value(self):
        price = self.vehicle.sale_price()
        value = price + (self.vehicle.INTEREST_RATE * self.monthly_payments * price / 100)
        return value
        
    def _get_monthly_representation(self):
        return self.monthly_payments


class LeaseContract(Contract):
    MONTHLY_ATTR_NAME = 'length_in_months'
    
    def __init__(self, vehicle, customer, length_in_months):
        super().__init__(vehicle, customer)
        self.length_in_months = length_in_months

    def _real_total_value(self):
        price = self.vehicle.sale_price()
        value = price + (price * self.vehicle.LEASE_MULTIPLIER / self.length_in_months)
        return value

    def _get_monthly_representation(self):
        return self.length_in_months