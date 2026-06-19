# Purpose:    Script is for automatically generating mock-up customers for demo purposes.
# Author:     Gemini and Tien PHAN
# Version:    0.1

import pandas as pd
import random
import unidecode

# Before running the script, you need to install required modules based on your local environment.
# pip3 install pandas 
# pip3 install unidecode
# pip3 install openpyxl

# 1. Initialize a list of sample data for merging.
last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzales", "Wilson", "Anderson"]
first_names = [
    "James", "Michael", "John", "Robert", "David", "William", "Richard", "Joseph", "Thomas", "Christopher", "Charles", "Daniel", 
    "Joe", "Mason", "Lucas", "Randy", "Willie", "Wayne", "Vincent", "Caleb", "Albert", "Luke", "Isaac", "Bradley", "Cameron"
]

# DECLARE YOUR REQUIRED FIELDS HERE
# Change mobile prefixes here. 
phone_prefixes = ["090", "091", "098", "096", "097", "032", "035", "070", "077", "083", "085"]
# Change mail domain here.
domains = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com"]
# Change segments here. You can create a new variable.
segments = ["B2B", "B2C"]
# Change tour types here. You can create a new variable. 
tour_types = ["Accommodations", "Cruises", "Domestic Tour", "Inbound Tour"]

data = []

# 2. The loop generates 500 lines of data. You can use your own number, e.g., 200 or number you want.
for _ in range(500):
    last = random.choice(last_names)
    first = random.choice(first_names)
    
    # Combine full name to create an email address.
    full_first_name = f"{first} {last}"
    
    # Change the name to one without accents to create a standard email address.
    last_clean = unidecode.unidecode(last).lower().replace(" ", "")
    first_clean = unidecode.unidecode(first).lower().replace(" ", "")
    email = f"{last_clean}.{first_clean}{random.randint(10, 99)}@{random.choice(domains)}"
    
    phone = random.choice(phone_prefixes) + "".join([str(random.randint(0, 9)) for _ in range(7)])
    segment = random.choice(segments)
    tour = random.choice(tour_types)

# DECLARE YOUR REQUIRED FIELD HERE    
# The data structure will appear in the Excel file.
    data.append({
        "Last Name": last,
        "First Name": full_first_name,
        "Email": email,
        "Phone": phone,
        "Segmentation": segment,
        "Tour Types": tour
    })

# 3. Create a DataFrame and export the file.
df = pd.DataFrame(data)

# Export to Excel file
df.to_excel("mock_data_tourism_500.xlsx", index=False)
print("The file 'mock_data_tourism_500.xlsx' with 500 lines of data has been successfully created!")
