import fitz  # PyMuPDF
import os

# Set up paths
# pdf_filename = "test_1.pdf"
# pdf_filename = "test-5_33-landscape.pdf"
pdf_filename = "test-5_33-landscape-pages.pdf"
# pdf_filename = "test-5_33-portrait.pdf"
pdf_path = os.path.join(os.getcwd(), "POC", pdf_filename)

text_filename = "extracted_text_fitz.txt"
text_path = os.path.join(os.getcwd(), "POC", text_filename)  # File to store extracted text


# Function to extract text from a given PDF within a specified page range
def extract_text_from_pdf(file_path, page_range=None):
    """
    Extracts text from a given PDF within a specified page range.

    :param file_path: Path to the PDF file
    :param page_range: Tuple (start_page, end_page), e.g., (2, 5) extracts pages 2 to 5
    :return: Extracted text as a string
    """
    text = ""
    
    with fitz.open(file_path) as pdf:
        total_pages = len(pdf)

        # Validate and adjust page range
        start_page, end_page = page_range if page_range else (1, total_pages)
        start_page = max(1, start_page)  # Ensure start_page is at least 1
        end_page = min(total_pages, end_page)  # Ensure end_page does not exceed total pages

        for page_num in range(start_page - 1, end_page):  # Convert to zero-based index
            print(f"\npage-orientaion_{pdf_filename}_{page_num}:{pdf[page_num].rotation}\n")
            # pdf[page_num].set_rotation(0) # set page orientation to portrait always.
            text += pdf[page_num].get_text() + "\n\n"

    return text


# Function to save extracted text to a file
def save_text_to_file(text, file_path):
    """
    Saves extracted text to a separate text file.

    :param text: Extracted text
    :param file_path: Path to save the text file
    """
    with open(file_path, "w", encoding="utf-8") as text_file:
        text_file.write(text)
    print(f"Extracted text successfully saved to {file_path}")


# Example Usage
# page_range = (33, 79)  # Extract text from pages 3 to 6
page_range = (1, 2)  # Extract text from pages 3 to 6
extracted_text = extract_text_from_pdf(pdf_path, page_range)

# Save extracted text to a file
save_text_to_file(extracted_text, text_path)
