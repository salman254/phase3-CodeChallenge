from coffee import Coffee
from customer import Customer
from order import Order

def test_coffee_shop():
    print("=== Testing Coffee Shop System ===")
    
    try:
        
        espresso = Coffee("Espresso")
        latte = Coffee("Cafe Latte", size="large", coffee_type="latte")
        
        
        alice = Customer("Alice")
        bob = Customer("Robert Johnson")
        
        
        order1 = alice.create_order(espresso, 2.50)
        order2 = bob.create_order(latte, 4.75)
        order3 = alice.create_order(latte, 5.00)
        
        
        latte.add_extra("caramel", 0.75)
        latte.add_extra("whipped cream", 0.50)
        
        
        print("\n--- Coffee Tests ---")
        print(f"{espresso} has {espresso.num_orders()} orders")
        print(f"{latte} has {latte.num_orders()} orders")
        print(f"Average price for {latte.name}: ${latte.average_price():.2f}")
        
        print("\n--- Customer Tests ---")
        print(f"{alice.name}'s coffees: {[c.name for c in alice.coffees()]}")
        print(f"{bob.name}'s orders: {len(bob.orders())}")
        
        print("\n--- Order Tests ---")
        order1.update_status("completed")
        print(order1)
        print(order2)
        
        print("\n--- Aficionado Test ---")
        aficionado = Customer.most_aficionado(latte)
        print(f"Biggest {latte.name} fan: {aficionado}")
        
       
        print("\n--- Error Handling Tests ---")
        try:
            bad_coffee = Coffee("A")
        except ValueError as e:
            print(f"Expected error: {e}")
            
        try:
            bad_order = alice.create_order(espresso, 15.00)
        except ValueError as e:
            print(f"Expected error: {e}")
            
    except Exception as e:
        print(f"Unexpected error during testing: {e}")
    finally:
        print("\n=== Testing Complete ===")

if __name__ == "__main__":
    test_coffee_shop()