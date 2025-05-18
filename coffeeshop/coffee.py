class Coffee:
   
    
    SIZE_OPTIONS = ["small", "medium", "large"]
    DRINK_TYPES = ["espresso", "americano", "latte", "cappuccino", 
                  "mocha", "macchiato", "flat white"]
    
    def __init__(self, name, size="medium", coffee_type="espresso"):
        self._name = None
        self._size = None
        self._type = None
        
        self.name = name
        self.size = size
        self.type = coffee_type
        self.extras = []
        
    @property
    def name(self):
        return self._name
        
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Coffee name must be a string")
        if len(value.strip()) < 3:
            raise ValueError("Coffee name must be at least 3 characters long")
        self._name = value.strip()
        
    @property
    def size(self):
        return self._size
        
    @size.setter
    def size(self, value):
        if not isinstance(value, str):
            raise TypeError("Size must be a string")
        if value.lower() not in self.SIZE_OPTIONS:
            raise ValueError(f"Size must be one of: {', '.join(self.SIZE_OPTIONS)}")
        self._size = value.lower()
    
    @property
    def type(self):
        return self._type
        
    @type.setter
    def type(self, value):
        if not isinstance(value, str):
            raise TypeError("Coffee type must be a string")
        if value.lower() not in self.DRINK_TYPES:
            raise ValueError(f"Type must be one of: {', '.join(self.DRINK_TYPES)}")
        self._type = value.lower()
        
    def _validate_extra(self, extra_name, extra_price):
        """Helper method to validate extra inputs."""
        if not isinstance(extra_name, str):
            raise TypeError("Extra name must be a string")
        if not isinstance(extra_price, (int, float)):
            raise TypeError("Extra price must be a number")
        if extra_price < 0:
            raise ValueError("Extra price cannot be negative")
        
    def add_extra(self, extra_name, extra_price):
        self._validate_extra(extra_name, extra_price)
        self.extras.append({
            "name": extra_name.strip(),
            "price": round(float(extra_price), 2)
        })
        
    def remove_extra(self, extra_name):
        if not isinstance(extra_name, str):
            raise TypeError("Extra name must be a string")
        initial_count = len(self.extras)
        self.extras = [e for e in self.extras if e["name"].lower() != extra_name.lower()]
        return len(self.extras) < initial_count
    
    def get_extras_total(self):
        return sum(extra["price"] for extra in self.extras)
    
    def orders(self):
        from order import Order
        return [order for order in Order.all_orders if order.coffee == self]
        
    def customers(self):
        seen = set()
        return [order.customer for order in reversed(self.orders()) 
                if not (order.customer in seen or seen.add(order.customer))]
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        orders = self.orders()
        if not orders:
            raise ValueError("Cannot calculate average price - coffee has no orders")
        return round(sum(order.price for order in orders) / len(orders), 2)
    
    def __repr__(self):
        return f"Coffee(name='{self.name}', size='{self.size}', type='{self.type}')"
    
    def __str__(self):
        extras = ", ".join(e["name"] for e in self.extras)
        return f"{self.size} {self.type} '{self.name}'" + (f" with {extras}" if extras else "")