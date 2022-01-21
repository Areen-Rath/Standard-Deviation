import csv
import math

with open("data.csv") as f:
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data[0]

def mean(data):
    global length
    length = len(data)
    total = 0

    for i in data:
        total += int(i)

    mean = total/length
    return mean

square_array = []
for num in data:
    diff = int(num) - mean(data)
    square = diff**2
    square_array.append(square)

sum = 0
for i in square_array:
    sum += i

result = sum/length
sd = math.sqrt(result)
print(f"Standard deviation is {sd}")