import asyncio
from langchain_community.document_loaders import PyPDFLoader
import os

pdf_filename = "test_1.pdf"
pdf_path = os.path.join(os.getcwd(), "POC", pdf_filename)

async def load_pdf(file_path, start_page=1, end_page=None):
    loader = PyPDFLoader(file_path)
    pages = []
    i = 0  # Initialize page counter
    async for page in loader.alazy_load():
        i += 1
        if i < start_page:
            continue
        if end_page and i > end_page:
            break
        pages.append(page)
    return pages

async def main():
    start_page = 1  # Specify start page
    end_page = 3  # Specify end page
    
    pages = await load_pdf(pdf_path, start_page, end_page)
    
    for i, page in enumerate(pages, start=start_page):
        print(f"Page {i}:")
        print(page.page_content[:500])  # Print first 500 characters of each page
        print("-" * 80)

if __name__ == "__main__":
    asyncio.run(main())
