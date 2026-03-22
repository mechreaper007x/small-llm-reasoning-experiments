def calculate_mean_and_std_dev(values):
    mean_val = sum(values) / len(values)
    std_val = (sum((x - mean_val) ** 2 for x in values) / len(values)) ** 0.5
    return mean_val, std_val

values = [12, 15, 18, 10, 22]
mean_val, std_val = calculate_mean_and_std_dev(values)
print("Mean:", mean_val, "Standard Deviation:", std_val)

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