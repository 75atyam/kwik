import pandas as pd
import time

def process_row(row):
    """Function to process each row"""
    print(f"{row['Phone Number']}")
    return row['Phone Number']  # Return phone number

def iterate_excel_rows(file_path):
    """Function to extract phone numbers into a list"""
    df = pd.read_excel(file_path)
    phone_numbers = [process_row(row) for _, row in df.iterrows()]
    return phone_numbers

