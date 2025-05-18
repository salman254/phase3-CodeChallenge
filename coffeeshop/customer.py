class Customer:
    
    
    def __init__(self, name):
        self._name = None
        self.name = name
        self._orders = []
        
    @property
    def name(self):
        return self._name
        
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Customer name must be a string")
        cleaned = value.strip()
        if len(cleaned) < 1:
            raise ValueError("Customer name cannot be empty")
        if len(cleaned) > 15:
            raise ValueError("Customer name cannot exceed 15 characters")
        self._name = cleaned
        
    def orders(self):
        return self._orders.copy()
    
    def coffees(self):
        return list({order.coffee for order in self._orders})
    
    def create_order(self, coffee, price):
        from coffee import Coffee
        from order import Order
        
        if not isinstance(coffee, Coffee):
            raise TypeError("Must provide a valid Coffee object")
        
        try:
            new_order = Order(self, coffee, price)
            self._orders.append(new_order)
            return new_order
        except Exception as e:
            raise ValueError(f"Failed to create order: {str(e)}")
    
    @classmethod
    def most_aficionado(cls, coffee):
        if not isinstance(coffee, coffee):
            raise TypeError("Must provide a valid Coffee object")
            
        if not coffee.orders():
            return None
            
        spending = {}
        for order in coffee.orders():
            customer = order.customer
            spending[customer] = spending.get(customer, 0) + order.price
            
        return max(spending.items(), key=lambda x: x[1])[0]
    
    def __repr__(self):
        return f"Customer(name='{self.name}')"
    
    def __str__(self):
        return f"{self.name} ({len(self.orders())} orders)"