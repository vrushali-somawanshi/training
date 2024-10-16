import csv



# Data to write to the CSV file
data = [
    ["Name", "Age", "City"],
    ["Alice", 30, "New York"],
    ["Bob", 25, "Los Angeles"],
    ["Charlie", 35, "Chicago"]
]

# Open the file in write mode
f = open("output.csv","w")
    # Create a writer object
writer = csv.writer(f)
    
# Write each row to the CSV file
writer.writerows(data)

print("Data written to CSV file successfully.")