import numpy
from scipy import stats
import csv

ages = []

with open('data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        ages.append(int(row['Age']))

ages_array = numpy.array(ages)

print("Mean age:", numpy.mean(ages_array))
print("Median age:", numpy.median(ages_array))
print("Mode age:", stats.mode(ages_array, keepdims=True).mode[0])