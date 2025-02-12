import fitz  # PyMuPDF
import os

# Set PDF path
pdf_filename = "test-5_33.pdf"
pdf_path = os.path.join(os.getcwd(), "POC", "html_markdown", pdf_filename)

def extract_pdf_as_html(pdf_file, start_page=1, end_page=None):
    """Extracts text from a PDF within a given range, preserving HTML structure."""
    doc = fitz.open(pdf_file)  # Open the PDF
    html_content = ""

    # Ensure the end_page does not exceed total pages
    total_pages = len(doc)
    end_page = min(end_page or total_pages, total_pages)  

    for page_num in range(start_page - 1, end_page):  # PyMuPDF uses 0-based index
        html_content += doc[page_num].get_text("html")  # Extract text with HTML formatting

    return html_content

# Example: Extract pages 2 to 5
html_output = extract_pdf_as_html(pdf_path, start_page=1, end_page=2)

# Save extracted text as an HTML file
output_file = os.path.join(os.getcwd(), "POC", "html_markdown", "extracted_pdf.html")
with open(output_file, "w", encoding="utf-8") as f:
    f.write(html_output)

print(f"Extracted HTML content , saved to {output_file}")
