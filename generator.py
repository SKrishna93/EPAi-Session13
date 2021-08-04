#Importing packages

from collections import namedtuple, Counter
from datetime import date

files = "nyc_parking_tickets_extract.csv"

# Generator Object
def tickets(files: "csv file")-> "Genrator object":
    '''
    Create a generator object which returns one line of the file at a time
    #### Input:
        csv file/files to be read
    #### Return
        None, yield after reading each line
    '''
    count = 0
    with open(files, encoding='utf8', errors='ignore') as f:
        for line in f:
            if count == 0:
                count += 1
                yield line
            else:
                yield formatting(line)

# Formatting function
def formatting(line: str)-> list:
    '''
    Formats the line returned by generator into required format
    #### Input:
        file line returned from generator
    #### Return:
        line - list of the comma seperated values, formatted to requirement
    '''
    line = line.strip().split(',')
    line[0] = int(line[0])
    date_list = [int(x) for x in line[4].split('/')]
    line[4] = date(date_list[2], date_list[0], date_list[1])
    line[5] = int(line[5])
    return line

def create_record()-> list:
    '''
    This function creates a collection of namedtuples by reading the csv file line by line
    #### Input:
        None
    #### Return:
        Collection of namedtuples stored in a list
    '''
    tickets_records = []
    count = 0
    records = tickets(files)

    #Creating a NamedTuple
    parking_violations = namedtuple('parking_violations',['Summons_Number','Plate_ID','Registration_State','Plate_Type','Issue_Date','Violation_Code','Vehicle_Body_Type','Vehicle_Make','Violation_Description'])
    for violation in records:
        if count == 0:
            count =+ 1
            column_names = violation
        else:
            p = parking_violations(*violation)
            tickets_records.append(p)
    return tickets_records, records

def max_violations(tickets_records: list)-> "Max violations by car manufacturer":
    '''
    This function returns the vehicle manufacturer with the maximum violations
    #### input:
        tickets_records - Collection of list of named tuples
    #### return:
        make (Vehicle manufacturer) with maximum violations and manufacturer (exhausted generator object)
    '''
    manufacturer = (x.Vehicle_Make for x in tickets_records)
    make = Counter(manufacturer).most_common(1)[0]
    return make, manufacturer