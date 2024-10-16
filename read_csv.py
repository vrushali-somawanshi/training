import csv

# Define the path to your CSV file
# file_path = r"C:\Users\VRAMDASS\Desktop\Python\training\dats.csv"


# Open the file in read mode
# with open(file_path, 'r') as csvfile:
    # Create a reader object
    # csv_reader = csv.reader(csvfile)
    
    # Iterate over each row in the CSV file and print it
    # for row in csv_reader:
    #     print(row)

f = open(r"C:\Users\VRAMDASS\Desktop\Python\training\dats.csv","r")
reader = csv.reader(f)
for row in reader:
    print(row)