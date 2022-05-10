import math
import pandas as pd


population = pd.read_csv("archive/losses_russia.csv")


# Creating sample dataset

# sample = pd.DataFrame({
#     "losses_total": population['losses_total'].head(50),
# })
# sample.to_csv('sample.csv')

# Z Test calculations

sample = pd.read_csv("sample.csv")
alpha = 0.05


sample_mean = population['losses_total'].mean()
population_mean = sample['losses_total'].mean()
population_std = population['losses_total'].std()

z = (sample_mean-population_mean)/(population_std/ math.sqrt(50))

table_z = {
    0.05: 1.96,
    0.01: 2.576,
    0.001: 3.291
}

print("\nz = ", z)
if abs(z) < table_z[0.05]:
    print("Retain H0,")
else:
    print("Reject H0")
print('\n')
