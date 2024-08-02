import csv


def csv_thing():
    with open('src\Test.csv', mode='r')as file:

        csvFile = csv.DictReader(file)
        a = []

        for lines in csvFile:
            b = (lines['Translated Indications'].split(","))
            for i in range(len(b)):
                b[i] = b[i].strip().lower()

            a.append(b)
    return (a)

def meds():
    with open('src\Test.csv', mode='r')as file:

        csvFile = csv.DictReader(file)
        a = []

        for lines in csvFile:
            b = (lines['Name of Medicine\nMedicine'].split(","))
            for i in range(len(b)):
                b[i] = b[i].strip().lower()

            a.append(b)
    return (a)

def content():
    with open('src\Test.csv', mode='r')as file:

        csvFile = csv.DictReader(file)
        a = []

        for lines in csvFile:
            b = (lines['Content'].split(","))
            for i in range(len(b)):
                b[i] = b[i].strip().lower()

            a.append(b)
    return (a)

def dose():
    with open('src\Test.csv', mode='r')as file:

        csvFile = csv.DictReader(file)
        a = []

        for lines in csvFile:
            b = (lines['Dose'].split(","))
            for i in range(len(b)):
                b[i] = b[i].strip().lower()

            a.append(b)
    return (a)

def precaution():
    with open('src\Test.csv', mode='r')as file:

        csvFile = csv.DictReader(file)
        a = []

        for lines in csvFile:
            b = (lines['Precaution/Contraindication'].split(","))
            for i in range(len(b)):
                b[i] = b[i].strip().lower()

            a.append(b)
    return (a)

def reference():
    with open('src\Test.csv', mode='r')as file:

        csvFile = csv.DictReader(file)
        a = []

        for lines in csvFile:
            b = (lines['Reference Text'].split(","))
            for i in range(len(b)):
                b[i] = b[i].strip().lower()

            a.append(b)
    return (a)

