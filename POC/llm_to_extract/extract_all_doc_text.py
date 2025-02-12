# import sys, pathlib, pymupdf
import os
import pymupdf4llm
# # get document filename

pdf_filename = "test-5_33.pdf"
pdf_path = os.path.join(os.getcwd(), "POC", "llm_to_extract", pdf_filename)

extracted_text = "extracted_text.txt"
extracted_text_path = os.path.join(os.getcwd(), "POC", "llm_to_extract", extracted_text)

# with pymupdf.open(pdf_path) as doc:  # open document
#     text = chr(12).join([page.get_text() for page in doc])
# # write as a binary file to support non-ASCII characters
# pathlib.Path(extracted_text_path).write_bytes(text.encode())



# import pdfplumber
# with pdfplumber.open(pdf_path) as pdf:
#     # iterate over each page
#     for page in pdf.pages:
#         print(page.extract_tables())


md_text = pymupdf4llm.to_markdown(pdf_path)

with open(extracted_text, "w", encoding="utf-8") as file:
    file.write(md_text)
