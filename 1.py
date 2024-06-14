import pandas as pd

# Create a list of effort values from 1 to 375
effort = list(range(1, 376))

# Calculate the cost as the square of effort
cost = [e**2 for e in effort]

# Create a DataFrame
df = pd.DataFrame({'effort': effort, 'cost': cost})

# Display the DataFrame
df
