import os
import pdfplumber
import json

# Get the current directory path
pdf_filename = "test_1.pdf"
pdf_path = os.path.join(os.getcwd(),"POC", pdf_filename)  # Use current directory

json_filename = "extracted_tables.json"
json_path = os.path.join(os.getcwd(),"POC", json_filename)  # JSON file in same directory

# Function to extract tables from a specific page range in a PDF
def extract_tables_from_pdf(pdf_path, page_range=None):
    """
    Extracts tables from a given PDF within a specified page range.

    :param pdf_path: Path to the PDF file
    :param page_range: Tuple (start_page, end_page), e.g., (2, 5) extracts pages 2 to 5
    :return: List of structured table data
    """
    extracted_data = []
    with pdfplumber.open(pdf_path) as pdf:
        total_pages = len(pdf.pages)
        
        # Define page range: Default to full PDF if no range is provided
        start_page, end_page = page_range if page_range else (1, total_pages)

        for page_num in range(start_page - 1, min(end_page, total_pages)):  # Convert to zero-based index
            page = pdf.pages[page_num]
            tables = page.extract_tables()
            for table_index, table in enumerate(tables):
                structured_table = {
                    "page": page_num + 1,
                    "table_index": table_index,
                    "data": [dict(zip(table[0], row)) for row in table[1:] if len(row) == len(table[0])],  
                }
                extracted_data.append(structured_table)
    return extracted_data


# Function to save extracted tables as JSON
def save_to_json(data, json_path):
    """
    Saves extracted table data to a JSON file.
    :param data: Extracted table data
    :param json_path: Path to save the JSON file
    """
    with open(json_path, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=2, ensure_ascii=False)
    print(f"Data successfully saved to {json_path}")

# Example Usage
page_range = (5, 6)  # Extract tables from pages 5 to 6
tables = extract_tables_from_pdf(pdf_path, page_range)

# Save extracted data to JSON
save_to_json(tables, json_path)