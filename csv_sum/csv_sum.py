import pathlib
import csv

path = pathlib.Path.cwd().joinpath("data").glob("*/*.csv")

result = 0
for file in path:
    with file.open(mode="r") as file:
        csv_reader = csv.reader(file)
        
        for row in csv_reader:
            result += sum([int(num) for num in row])

print(result)
