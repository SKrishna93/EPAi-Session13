# EPAi3-Session13

## Generators and Iteration Tools

### Question - 1

#### Objective: Create a lazy iterator that will return a named tuple of the data in each row. The data types should be appropriate - i.e. if the column is a date, you should be storing dates in the named tuple, if the field is an integer, then it should be stored as an integer, etc.

##### Functions
----------------
* __tickets__ (files)
    - Create a generator object which returns one line of the file at a time
    - Input: csv file/files to be read
    - Return: None, yield after reading each line
* __formatting__ (line)
    - Formats the line returned by generator into required format
    - Input: file line returned from generator
    - Return: line - list of the comma seperated values, formatted to requirement
* __create_record__ ()
    - This function creates a collection of namedtuples by reading the csv file line by line
    - Input: None
    - Return: Collection of namedtuples stored in a list

### Question - 2

#### Objective: Calculate the number of violations by car make

* __max_violations__ (tickets_records)
    - This function returns the vehicle manufacturer with the maximum violations
    - input - tickets_records - Collection of list of named tuples
    - return - make (Vehicle manufacturer) with maximum violations and manufacturer (exhausted generator object)

__________________________________________________________________________________________________________________