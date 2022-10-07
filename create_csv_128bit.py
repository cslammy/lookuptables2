import csv


#use this to go from data in a CSV of initial note + freq values to an output file.
#128bit.csv is excel source files saved in CSV format
#this script is for one time use, I used this to create a dictnote.py dictionary that main.py needs.
#NOTE: for me there is some dukey to the right of C0 key.Whatever. I got rid of it w a text editor....

dict_from_csv = {}

with open('128bit.csv', mode='r') as inp:
    reader = csv.reader(inp)
    dict_from_csv = {rows[0]:rows[1] for rows in reader}

    print(dict_from_csv)
