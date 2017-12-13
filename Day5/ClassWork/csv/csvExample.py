import csv


# C:\Users\dinram\PycharmProjects\PythonModule1\Day5\ClassWork\csv\exampleData.csv

# how to open a CSV file and read each row, as well as reference specific data on each row.
def example1():
    with open('exampleData.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            print(row)
            print(row[0])
            print(row[0], row[1], row[2], )


# how to pull out specific data from the spreadsheet and save it to a list variable:
def example2():
    with open('exampleData.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')

    dates = []
    colors = []
    for row in readCSV:
        color = row[3]
        date = row[0]

        dates.append(date)
        colors.append(color)

    print(dates)
    print(colors)

example2()
