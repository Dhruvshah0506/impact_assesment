class ElectricityBill:
    def __init__(self):
        self.rate_slabs = [
            (0, 50, 3.0),
            (51, 100, 4.5),
            (101, 200, 6.0),
            (201, float('inf'), 7.5)
        ]
        self.fixed_charges = 50.0
        self.tax_rate = 0.18
        
    def calculate_bill(self, units):
        try:
            units = float(units)
            if units < 0:
                raise ValueError("Units cannot be negative")
                
            total = self.fixed_charges
            for slab in self.rate_slabs:
                min_units, max_units, rate = slab
                if units > min_units:
                    chargeable_units = min(units, max_units) - min_units
                    total += chargeable_units * rate
            
            tax = total * self.tax_rate
            total += tax
            
            return {
                'units': units,
                'energy_charges': total - self.fixed_charges - tax,
                'fixed_charges': self.fixed_charges,
                'tax': tax,
                'total': total
            }
            
        except ValueError as e:
            print(f"Error: {e}")
            return None

def main():
    print("Electricity Bill Calculator")
    bill_calculator = ElectricityBill()
    
    while True:
        try:
            units = input("\nEnter units consumed (or 'q' to quit): ")
            if units.lower() == 'q':
                break
                
            bill = bill_calculator.calculate_bill(units)
            if bill:
                print("\nBill Details:")
                print("+----------------+-------------------+")
                print("| {:^14} | {:^17} |".format("Component", "Amount (₹)"))
                print("+----------------+-------------------+")
                print("| {:^14} | {:^17.2f} |".format("1. Units", bill['units']))
                print("| {:^14} | {:^17.2f} |".format("2. Energy", bill['energy_charges']))
                print("| {:^14} | {:^17.2f} |".format("3. Fixed", bill['fixed_charges']))
                print("| {:^14} | {:^17.2f} |".format("4. Tax (18%)", bill['tax']))
                print("+----------------+-------------------+")
                print("| {:^14} | {:^17.2f} |".format("Total", bill['total']))
                print("+----------------+-------------------+")
                
        except KeyboardInterrupt:
            print("\nProgram terminated by user.")
            break

if __name__ == "__main__":
    main()
