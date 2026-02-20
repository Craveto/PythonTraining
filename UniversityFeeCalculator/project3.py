# 13. Ask user to opt for courses for master degree based on the following
# L1 = [“HR”, “Finance”, “Marketing”, “DS”]
# Based on above subject there are two different streams. For example- HR is having HR core and HR analytics and Marketing is having core and Marketing analytics. Analytics is the optional subject and having added extra fees. DS is not having analytics.
# If fees for L1 is 2 lakhs for each course core subject having the same fees but analytics subject having 10% extra on 2 lakhs.
# If student opts for hostel then 2 lakhs per year is added. For food monthly 2000 .
# Transportation charges 13000 per semester. Calculate the total annual cost based on selected service.
# User will enter values as subject, analytics(Y/N), Hostel (Y/N), food(How many months?), Transportation(semester/annual) . 

# for each to streams (core and analytics )      
    

import logging

# Configure Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class UniversityFeeCalculator:
    def __init__(self):
        self.base_fee = 200000
        self.hostel_annual_fee = 200000
        self.monthly_food_rate = 2000
        self.transport_per_sem = 13000
        
    def calculate_total(self, subject, stream, hostel, food_months, transport):
        logger.info(f"calculation for Subject: {subject}, Stream: {stream}")
        
        total_cost = 0
        
        if stream == 'A' and subject != 'DS':
            course_fee = self.base_fee + (self.base_fee * 0.10)
            logger.info("Applied 10% analytics charges.")
        else:
            course_fee = self.base_fee
            if stream == 'A' and subject == 'DS':
                logger.warning("DS does not have an Analytics stream.")
        
        total_cost += course_fee
        
        # 2. Hostel Fee
        if hostel == 'Y':
            total_cost += self.hostel_annual_fee
            logger.info("Hostel fees added.")
            
        # 3. Food Fee
        food_total = food_months * self.monthly_food_rate
        total_cost += food_total
        logger.info(f"Food charges for {food_months} months added.")
        
        # 4. Transportation
        if transport == 'SEMESTER':
            total_cost += self.transport_per_sem
        elif transport == 'ANNUAL':
            total_cost += (self.transport_per_sem * 2)
            
        logger.info("Transportation calculation complete.")
        return total_cost

def main():
    try:
        print("--- Master Degree Course Selection ---")
        sub = input("Enter subject (HR/Finance/Marketing/DS): ").upper()
        stream = input("Analytics or Core (A/C): ").upper()
        stay = input("Hostel (Y/N): ").upper()
        food = int(input("Enter food months (0-12): "))
        trans = input("Transportation (SEMESTER/ANNUAL/NONE): ").upper()

        # Initialize OOP Class
        calculator = UniversityFeeCalculator()
        
        final_bill = calculator.calculate_total(sub, stream, stay, food, trans)
        
        print("\n" + "="*30)
        print(f"Total Annual Cost for {sub}: {final_bill}")
        print("="*30)
        
    except ValueError as e:
        logger.error(f"Invalid input provided: {e}")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
