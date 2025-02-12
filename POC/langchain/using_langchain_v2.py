# from langchain_community.document_loaders import PyPDFLoader
# import os

# pdf_filename = "test-5_33.pdf"
# pdf_path = os.path.join(os.getcwd(), "POC","langchain", pdf_filename)

# loader = PyPDFLoader(
#     file_path = pdf_path,
#     # headers = None
#     # password = None,
#     # mode = 'single',
#     # pages_delimiter = ""
#     )



# docs = []
# docs_lazy = loader.lazy_load()

# for doc in docs_lazy:
#     docs.append(doc)

# print(docs[0].page_content[:100])
# print(docs[0].metadata)



from langchain_community.document_loaders import PyPDFLoader
import os

pdf_filename = "test-5_33.pdf"
pdf_path = os.path.join(os.getcwd(), "POC", "langchain", pdf_filename)

# Load the PDF
loader = PyPDFLoader(file_path=pdf_path)

docs = list(loader.lazy_load())

# Write the extracted text to a file
output_file = os.path.join(os.getcwd(),"POC", "langchain", "extracted_text.txt")

with open(output_file, "w", encoding="utf-8") as f:
    for doc in docs:
        f.write(f"Page {doc.metadata.get('page', 'Unknown')}:\n")
        f.write(doc.page_content)
        f.write("\n" + "-"*80 + "\n")

print(f"Extracted text written to {output_file}")
