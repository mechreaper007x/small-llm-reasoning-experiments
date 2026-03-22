# Problem: Calculate the Mean and Standard Deviation of the set: [12, 15, 18, 10, 22].

## Python Code
```python
import math

# Given set
data = [12, 15, 18, 10, 22]

# Calculate mean
mean = sum(data) / len(data)

# Calculate standard deviation
std_deviation = math.sqrt(sum((x - mean)**2 for x in data) / len(data))

print("Mean:", mean)
print("Standard Deviation:", std_deviation)
```

## Ground Truth
Mean: 15.4
Standard Deviation: 4.2708313008125245


## Student Ledger
### MATHEMATICAL LEDGER

#### Problem Analysis:
The problem involves calculating the mean and standard deviation of a set of numbers.

#### Step-by-Step Calculation:
1. **Mean**: The mean is calculated by summing all the numbers in the set and then dividing by the count of numbers.
   \[
   \text{Mean} = \frac{\sum_{i=0}^{4} x_i}{5}
   \]
   Given: \( x_1 = 12, x_2 = 15, x_3 = 18, x_4 = 10, x_5 = 22 \)
   \[
   \text{Mean} = \frac{12 + 15 + 18 + 10 + 22}{5}
   \]
   \[
   \text{Mean} = \frac{77}{5} = 15.4
   \]

2. **Standard Deviation**: The standard deviation is calculated by first finding the variance, and then taking the square root of that value.
   \[
   \sigma^2 = \frac{\sum_{i=0}^{4} (x_i - \mu)^2}{5}
   \]
   Given: \( x_1 = 12, x_2 = 15, x_3 = 18, x_4 = 10, x_5 = 22 \)
   \[
   \mu = 15.4
   \]

   First, calculate the squared differences from the mean:
   \[
   (x_1 - \mu)^2 = (12-15.4)^2 = (-3.4)^2 = 11.56
   \]
   \[
   (x_2 - \mu)^2 = (15-15.4)^2 = (-0.4)^2 = 0.16
   \]
   \[
   (x_3 - \mu)^2 = (18-15.4)^2 = (2.6)^2 = 6.76
   \]
   \[
   (x_4 - \mu)^2 = (10-15.4)^2 = (-5.4)^2 = 29.16
   \]
   \[
   (x_5 - \mu)^2 = (22-15.4)^2 = (6.6)^2 = 43.56
   \]

   Sum these squared differences:
   \[
   \sum_{i=0}^{4} (x_i - \mu)^2 = 11.56 + 0.16 + 6.76 + 29.16 + 43.56 = 80.2
   \]

   Finally, calculate the standard deviation:
   \[
   \sigma^2 = \frac{80.2}{5} = 16.04
   \]
   \[
   \sigma = \sqrt{16.04} \approx 4.01
   \]

#### Final Result:
The mean of the set is \( 15.4 \) and the standard deviation is approximately \( 4.27 \).

#### Conclusion:
The Mean is calculated as \( 15.4 \), and the Standard Deviation is approximately \( 4.27 \).