class Order:
    
    
    STATUS_OPTIONS = ["pending", "preparing", "ready", "completed", "cancelled"]
    all_orders = []
    
    def __init__(self, customer, coffee, price):
        self._customer = None
        self._coffee = None
        self._price = None
        self._status = None
        
        self.customer = customer
        self.coffee = coffee
        self.price = price
        self.status = "pending"
        Order.all_orders.append(self)
        
    @property
    def customer(self):
        return self._customer
        
    @customer.setter
    def customer(self, value):
        from customer import Customer
        if not isinstance(value, Customer):
            raise TypeError("Customer must be a Customer instance")
        self._customer = value
        
    @property
    def coffee(self):
        return self._coffee
        
    @coffee.setter
    def coffee(self, value):
        from coffee import Coffee
        if not isinstance(value, Coffee):
            raise TypeError("Coffee must be a Coffee instance")
        self._coffee = value
        
    @property
    def price(self):
        return self._price
        
    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Price must be a number")
        if not 1.0 <= float(value) <= 10.0:
            raise ValueError("Price must be between 1.0 and 10.0")
        self._price = round(float(value), 2)
    
    @property
    def status(self):
        return self._status
        
    @status.setter
    def status(self, value):
        if not isinstance(value, str):
            raise TypeError("Status must be a string")
        if value.lower() not in self.STATUS_OPTIONS:
            raise ValueError(f"Status must be one of: {', '.join(self.STATUS_OPTIONS)}")
        self._status = value.lower()
    
    def update_status(self, new_status):
        self.status = new_status
    
    def __repr__(self):
        return (f"Order(customer={repr(self.customer)}, "
                f"coffee={repr(self.coffee)}, price={self.price})")
    
    def __str__(self):
        return (f"Order #{len(self.all_orders)}: {self.coffee.name} "
                f"for {self.customer.name} (${self.price:.2f}, {self.status})")