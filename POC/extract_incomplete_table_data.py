import pdfplumber
import pandas as pd
import os

pdf_filename = "test_1.pdf"
pdf_path = os.path.join(os.getcwd(), "POC", pdf_filename)

def extract_tables_with_headers(pdf_path, start_page=1, end_page=None):
    tables = []  # Store extracted tables
    last_headers = None  # Store the last detected table headers

    with pdfplumber.open(pdf_path) as pdf:
        total_pages = len(pdf.pages)
        
        # Validate the range
        start_page = max(1, start_page)  # Ensure start_page is at least 1
        end_page = min(total_pages, end_page) if end_page else total_pages  # Default to last page if None

        for page_num in range(start_page - 1, end_page):  # pdfplumber uses 0-based indexing
            page = pdf.pages[page_num]
            extracted_tables = page.extract_tables()

            for table in extracted_tables:
                df = pd.DataFrame(table)

                # Identify headers (first row with meaningful data)
                if last_headers is None or (df.iloc[0].nunique() > 1):  
                    last_headers = df.iloc[0].tolist()  # Save detected headers
                    df.columns = last_headers
                    df = df[1:]  # Remove the header row from data
                else:
                    # Ensure column count matches
                    if len(df.columns) < len(last_headers):  # If fewer columns, pad with NaN
                        missing_cols = len(last_headers) - len(df.columns)
                        for _ in range(missing_cols):
                            df[_] = None  # Add missing columns
                    elif len(df.columns) > len(last_headers):  # If more columns, trim extra ones
                        df = df.iloc[:, :len(last_headers)]
                    
                    df.columns = last_headers  # Apply consistent headers

                df.reset_index(drop=True, inplace=True)
                tables.append(df)

    return tables

# Example Usage: Extract tables from pages 5 to 7
tables = extract_tables_with_headers(pdf_path, start_page=5, end_page=7)

# Print extracted tables
for i, table in enumerate(tables):
    print(f"Table {i+1}:\n", table)
