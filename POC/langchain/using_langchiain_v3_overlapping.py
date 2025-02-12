from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

# Load the PDF
pdf_filename = "test-5_33.pdf"
pdf_path = os.path.join(os.getcwd(), "POC", "langchain", pdf_filename)
loader = PyPDFLoader(file_path=pdf_path)
docs = loader.load()  # Load all pages

# Combine all pages into a single text while keeping page metadata
all_text = []
metadata_list = []

for doc in docs:
    page_text = doc.page_content
    page_number = doc.metadata.get("page", "Unknown")
    
    all_text.append(page_text)
    metadata_list.append(f"Page {page_number}")

# Create a combined document
combined_text = "\n".join(all_text)

# Initialize RecursiveCharacterTextSplitter with overlap
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=5000,  # Adjust chunk size based on average page length
    chunk_overlap=2000  # Ensures 3-page overlap (tunable)
)

chunks = text_splitter.split_text(combined_text)

# Write extracted overlapping text chunks to a file
output_file = os.path.join(os.getcwd(), "POC", "langchain", "extracted_text_overlapped.txt")

with open(output_file, "w", encoding="utf-8") as f:
    for idx, chunk in enumerate(chunks):
        f.write(f"Chunk {idx+1}:\n")
        f.write(chunk)
        f.write("\n" + "="*80 + "\n")
