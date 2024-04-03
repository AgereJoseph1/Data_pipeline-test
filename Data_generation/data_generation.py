import csv
from faker import Faker
import random

fake = Faker()

# Function to generate data for gold companies
def generate_gold_company_data(num_records):
    data = []
    for _ in range(num_records):
        transaction_id = fake.uuid4()
        date = fake.date_between(start_date='-1y', end_date='today')
        gold_production = random.randint(100, 10000)  # Random gold production in ounces
        exploration_activity = random.choice(["Exploration 1", "Exploration 2", "Exploration 3"])
        safety_record = random.choice(["Good", "Average", "Poor"])
        location = fake.city()
        employee_id = fake.random_int(min=1000, max=9999)
        environmental_impact = random.choice(["Yes", "No"])
        community_engagement = random.choice(["Yes", "No"])
        data.append([transaction_id, date, gold_production, exploration_activity, safety_record, location, employee_id, environmental_impact, community_engagement])
    return data

# Function to generate data for Scancom PLC (MTN Ghana)
def generate_scancom_plc_data(num_records):
    data = []
    for _ in range(num_records):
        transaction_id = fake.uuid4()
        date = fake.date_between(start_date='-1y', end_date='today')
        service_type = fake.random_element(elements=("Call", "SMS", "Data", "Roaming"))
        amount = fake.random_int(min=1, max=1000)  # Assuming the amount in local currency
        customer_id = fake.random_int(min=10000, max=99999)
        location = fake.city()
        network_performance = fake.random_element(elements=("Good", "Average", "Poor"))
        customer_feedback = fake.random_element(elements=("Satisfied", "Neutral", "Dissatisfied"))
        data.append([transaction_id, date, service_type, amount, customer_id, location, network_performance, customer_feedback])
    return data

# Function to generate data for Amanex Company Limited
def generate_amanex_company_data(num_records):
    data = []
    for _ in range(num_records):
        transaction_id = fake.uuid4()
        date = fake.date_between(start_date='-1y', end_date='today')
        product_id = fake.random_int(min=1000, max=9999)
        quantity = fake.random_int(min=1, max=100)
        amount = fake.random_int(min=10, max=1000)  # Assuming the amount in local currency
        customer_id = fake.random_int(min=10000, max=99999)
        location = fake.city()
        customer_type = fake.random_element(elements=("Individual", "Business"))
        product_quality = fake.random_element(elements=("High", "Medium", "Low"))
        data.append([transaction_id, date, product_id, quantity, amount, customer_id, location, customer_type, product_quality])
    return data

# Function to generate data for Dansword International Services Limited
def generate_dansword_international_data(num_records):
    data = []
    for _ in range(num_records):
        transaction_id = fake.uuid4()
        date = fake.date_between(start_date='-1y', end_date='today')
        service_type = fake.random_element(elements=("Consultation", "Maintenance", "Repair", "Installation"))
        amount = fake.random_int(min=10, max=1000)  # Assuming the amount in local currency
        customer_id = fake.random_int(min=10000, max=99999)
        location = fake.city()
        service_quality = fake.random_element(elements=("High", "Medium", "Low"))
        service_efficiency = fake.random_element(elements=("Fast", "Average", "Slow"))
        data.append([transaction_id, date, service_type, amount, customer_id, location, service_quality, service_efficiency])
    return data

# Function to generate data for Benso Oil Palm Plantation PLC
def generate_benso_oil_palm_data(num_records):
    data = []
    for _ in range(num_records):
        transaction_id = fake.uuid4()
        date = fake.date_between(start_date='-1y', end_date='today')
        product_id = fake.random_int(min=1000, max=9999)
        quantity = fake.random_int(min=10, max=100)
        amount = fake.random_int(min=10, max=1000)  # Assuming the amount in local currency
        customer_id = fake.random_int(min=10000, max=99999)
        location = fake.city()
        product_quality = fake.random_element(elements=("High", "Medium", "Low"))
        product_delivery_time = fake.random_element(elements=("Fast", "Average", "Slow"))
        data.append([transaction_id, date, product_id, quantity, amount, customer_id, location, product_quality, product_delivery_time])
    return data

# Function to generate data for First National Bank Ghana Limited
def generate_first_national_bank_data(num_records):
    data = []
    for _ in range(num_records):
        transaction_id = fake.uuid4()
        date = fake.date_between(start_date='-1y', end_date='today')
        transaction_type = fake.random_element(elements=("Deposit", "Withdrawal", "Transfer", "Payment"))
        amount = fake.random_int(min=10, max=10000)  # Assuming the amount in local currency
        customer_id = fake.random_int(min=10000, max=99999)
        location = fake.city()
        account_type = fake.random_element(elements=("Savings", "Current", "Loan"))
        transaction_channel = fake.random_element(elements=("Branch", "ATM", "Mobile", "Online"))
        data.append([transaction_id, date, transaction_type, amount, customer_id, location, account_type, transaction_channel])
    return data

# Save data to CSV file
def save_data_to_csv(company_name, data):
    filename = f"generated_data/{company_name}.csv"  # Save to the 'data' directory
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(get_header(company_name))  # Write header
        writer.writerows(data)

# Get header based on company name
def get_header(company_name):
    if "gold" in company_name.lower():
        return ["Transaction_ID", "Date", "Gold_Production", "Exploration_Activity", "Safety_Record", "Location", "Employee_ID", "Environmental_Impact", "Community_Engagement"]
    elif company_name == "Scancom PLC (MTN Ghana)":
        return ["Transaction_ID", "Date", "Service_Type", "Amount", "Customer_ID", "Location", "Network_Performance", "Customer_Feedback"]
    elif company_name == "Amanex Company Limited":
        return ["Transaction_ID", "Date", "Product_ID", "Quantity", "Amount", "Customer_ID", "Location", "Customer_Type", "Product_Quality"]
    elif company_name == "Dansword International Services Limited":
        return ["Transaction_ID", "Date", "Service_Type", "Amount", "Customer_ID", "Location", "Service_Quality", "Service_Efficiency"]
    elif company_name == "Benso Oil Palm Plantation PLC":
        return ["Transaction_ID", "Date", "Product_ID", "Quantity", "Amount", "Customer_ID", "Location", "Product_Quality", "Product_Delivery_Time"]
    elif company_name == "First National Bank Ghana Limited":
        return ["Transaction_ID", "Date", "Transaction_Type", "Amount", "Customer_ID", "Location", "Account_Type", "Transaction_Channel"]

# Generate data for each company and save to CSV
companies = [
    "Newmont Ghana Gold Limited", 
    "Gold Fields Ghana Limited", 
    "Newmont Golden Ridge Limited", 
    "AngloGold Ashanti Iduapriem Mine", 
    "Abosso Goldfields Limited", 
    "Scancom PLC (MTN Ghana)",
    "Amanex Company Limited",
    "Dansword International Services Limited",
    "Benso Oil Palm Plantation PLC",
    "First National Bank Ghana Limited"
]

# Generate 100,000 records for each company
for company in companies:
    if "gold" in company.lower():
        company_data = generate_gold_company_data(100000)
    elif company == "Scancom PLC (MTN Ghana)":
        company_data = generate_scancom_plc_data(100000)
    elif company == "Amanex Company Limited":
        company_data = generate_amanex_company_data(100000)
    elif company == "Dansword International Services Limited":
        company_data = generate_dansword_international_data(100000)
    elif company == "Benso Oil Palm Plantation PLC":
        company_data = generate_benso_oil_palm_data(100000)
    elif company == "First National Bank Ghana Limited":
        company_data = generate_first_national_bank_data(100000)
    else:
        company_data = []  # For other companies, no specific data generation function is defined
    save_data_to_csv(company, company_data)
