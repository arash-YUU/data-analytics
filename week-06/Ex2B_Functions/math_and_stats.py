# Programmer: Arash
# Date: 11-18-2026
# Purpose: Use random, math, and statistics functions
# Instructor: Deodat Sharma

import random
import math
import statistics

vals_1_100 = range(1, 101)  # range leaves out the stop value, so 101 includes 100
vals_sample = random.sample(vals_1_100, 75)
vals_choices = random.choices(vals_1_100, k=200)  # choices allows repeated numbers
radius = random.randint(3, 10)
pi = math.pi

sample_sum = sum(vals_sample)
sample_average = statistics.mean(vals_sample)
sample_median = statistics.median(vals_sample)
choices_average = statistics.mean(vals_choices)
choices_median = statistics.median(vals_choices)
choices_mode = statistics.mode(vals_choices)  # If several values tie, mode returns the first one it finds
choices_deviation = statistics.stdev(vals_choices)  # Measure how spread out the values are
choices_variance = statistics.variance(vals_choices)
circle_area = pi * radius ** 2
area_up = math.ceil(circle_area)  # Round up even when the decimal part is small
area_down = math.floor(circle_area)  # Round down to the whole number below the area

print("_Experimenting with a subset of integers 1-100:")
print(f"Sum of 75 sample values from 1 to 100: {sample_sum}")
print(f"Average of 75 sample values: {sample_average:.2f}")
print(f"Median of 75 sample values: {sample_median}")
print('\n')
print("_Experimenting with a superset of 200 values, integers 1-100:")
print(f"Average of 200 values: {choices_average:.2f}")
print(f"Median of 200 values: {choices_median}")
print(f"Mode of 200 values: {choices_mode}")
print(f"Standard deviation of 200 values: {choices_deviation:.2f}")
print(f"Variance of 200 values: {choices_variance:.2f}")
print('\n')
print("_Modeling a random circle:")
print(f"Radius = {radius}, area = {area_up} (rounded up to the nearest integer)")
print(f"Radius = {radius}, area = {area_down} (rounded down to the nearest integer)")
