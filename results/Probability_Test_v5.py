mean_val = (12 + 15 + 18 + 10 + 22) / 5
std_dev_val = ((12 - mean_val)**2 + (15 - mean_val)**2 + (18 - mean_val)**2 + (10 - mean_val)**2 + (22 - mean_val)**2) ** 0.5

mean_val, std_dev_val

# --- VERIFIER ---
import math

data = [12, 15, 18, 10, 22]

# Calculate mean
mean_val = sum(data) / len(data)

# Calculate standard deviation
squared_diffs = [(x - mean_val) ** 2 for x in data]
variance = sum(squared_diffs) / len(data)
std_val = math.sqrt(variance)

# Assertions to verify correctness
assert abs(mean_val - 15.6) < 0.01, "Mean calculation failed"
assert abs(std_val - 4.717) < 0.01, "Standard deviation calculation failed"