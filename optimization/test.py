import pandas as pd
import numpy as np
from scipy.optimize import minimize

# Constants
FUEL_SAFETY_MARGIN = 600
MAX_FUEL_PURCHASED = 10000
FUEL_TANK_CAPACITY = 12000

# Sample data (replace with actual data if available)
cities = ['Los Angeles', 'Houston', 'New York', 'Miami']
outbound_segment_distance = [1500, 1700, 1300, 2700]
local_fuel_price = [0.88, 0.15, 1.05, 0.95]
fuel_quantity_purchased = [5000, 0, 0, 0]
fuel_at_landing = [600, 600, 600, 600]
fuel_at_takeoff = [600, 600, 600, 600]

# DataFrame setup
table = {
    'Outbound Segment Distance': outbound_segment_distance,
    'Local Fuel Price': local_fuel_price,
    'Fuel Quantity Purchased': fuel_quantity_purchased,
    'Fuel At Landing': fuel_at_landing,
    'Fuel At Takeoff': fuel_at_takeoff
}
df = pd.DataFrame(table, index=cities)

# Objective Function: Minimize Sum(local fuel price * fuel quantity purchased)
def objective_function(df):
    df['Local Fuel Bill'] = df['Local Fuel Price'] * df['Fuel Quantity Purchased']
    return df['Local Fuel Bill'].sum()

# Constraints
constraints = []

# Constraint 1: Fuel At Landing - FUEL_SAFETY_MARGIN >= 0
constraints.append({
    'type': 'ineq',
    'fun': lambda x: df['Fuel At Landing'].values - FUEL_SAFETY_MARGIN
})

# Constraint 2: MAX_FUEL_PURCHASED - Fuel Quantity Purchased >= 0
constraints.append({
    'type': 'ineq',
    'fun': lambda x: MAX_FUEL_PURCHASED - x
})

# Constraint 3: FUEL_TANK_CAPACITY - Fuel At Takeoff >= 0
constraints.append({
    'type': 'ineq',
    'fun': lambda x: FUEL_TANK_CAPACITY - df['Fuel At Takeoff'].values
})

# Constraint 4: Fuel At Takeoff - (Fuel at Landing + Fuel Quantity Purchased) = 0
constraints.append({
    'type': 'eq',
    'fun': lambda x: df['Fuel At Takeoff'].values - (df['Fuel At Landing'].values + x)
})

# Constraint 5: Custom constraint with wrap-around
def custom_constraint(x):
    # Initialize an array for the constraint values
    constraint_values = [0] * len(cities)

    for i in range(len(cities)):
        # Wrap-around index
        prev_index = (i - 1) % len(cities)
        
        # dpi, yi, and zpi
        dpi = outbound_segment_distance[prev_index]
        yi = df['Fuel At Landing'].values[i]
        zpi = df['Fuel At Takeoff'].values[prev_index]

        # Constraint equation
        constraint_values[i] = (1 + (dpi / 4000)) * yi - ((1 - (dpi / 4000)) * zpi - dpi)

    return constraint_values

constraints.append({
    'type': 'eq',
    'fun': custom_constraint
})

# Initial guess for fuel quantity purchased
initial_guess = df['Fuel Quantity Purchased'].values

# Run optimization
result = minimize(objective_function, initial_guess, method='SLSQP', constraints=constraints)

# Check and update DataFrame with the optimized solution
if result.success:
    df['Optimized Fuel Quantity Purchased'] = result.x
    print("Optimized Decision Variables and Total Cost:\n", df)
    print("Minimum Total Fuel Cost:", result.fun)
else:
    print("Optimization did not converge:", result.message)
