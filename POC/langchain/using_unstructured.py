from langchain_unstructured import UnstructuredLoader
import os

pdf_filename = "test-5_33.pdf"
pdf_path = os.path.join(os.getcwd(), "POC", "langchain", pdf_filename)

def extract_text_with_langchain_pdf(pdf_file):
    loader = UnstructuredLoader(pdf_file)
    documents = loader.load()
    pdf_pages_content = "\n".join(doc.page_content for doc in documents)

    print("\nResponse:\n")
    print(pdf_pages_content)
    print("\n")

    return pdf_pages_content

extract_text_with_langchain_pdf(pdf_path)
