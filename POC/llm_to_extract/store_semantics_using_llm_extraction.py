import google.generativeai as genai
import fitz
from collections import namedtuple


GEMINI_API_KEY = "AIzaSyDA7YAIjasJ7y3rOub7ISeMlc4wCN2UC2w"

genai.configure(api_key=GEMINI_API_KEY)
gemini_model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction="""
      You are a text processing agent working with pdf document's Pages to restore semantic between pages.


        Extract specified values from the source text.
        Return answer as JSON object with following fields:(Do not enclose with json markdown)
        - "table_content" <Json object based on the header> (if found else "" )
        - "is_table_in_page": <boolean> literal[True,False]
        - "table_header" [column] (if found else "" )
        - "text_extracted_other_than_table_data" <string>
        


        Do not infer any data based on previous training, strictly use only source text given below as input.
    """
    )


def ask_gemini(pdf_page_content):
    print("\nExtracting chunk using llm---started\n")

    prompt = f"context: {pdf_page_content}"

    try:
        # Use the correct method for generating text with Gemini
        response = gemini_model.generate_content(prompt)

        print("\n")
        print(f"Total_token_count:{response.usage_metadata.total_token_count}")
        print(f"prompt_token_count:{response.usage_metadata.prompt_token_count}")
        print("\n")

        print("\n")
        print("Response:\n")
        print(response.text.strip())
        print("\n")
        # return response.text.strip()
    except Exception as e:
        print(f"\nError querying Gemini: {e}\n")
        return "Error occurred while querying Gemini."
    


def generate_chunk_using_llm(file_path,page_range=None):
        import json
        
        def extract_text_from_pdf():
            text = ""
            
            with fitz.open(file_path) as pdf:
                total_pages = len(pdf)

                # Validate and adjust page range
                start_page, end_page = page_range if page_range else (1, total_pages)
                start_page = max(1, start_page)  # Ensure start_page is at least 1
                end_page = min(total_pages, end_page)  # Ensure end_page does not exceed total pages

                for page_num in range(start_page - 1, end_page):  # Convert to zero-based index
                    text += pdf[page_num].get_text() + "\n\n"

            print("\n")
            print(f"Raw_data_from_pdf_{page_range.start}_{page_range.end}:\n")
            print(text)
            print("\n")
            return text
        
        ask_gemini(extract_text_from_pdf())

        # if(json.load(single_page_chunk)["table_"])



if __name__ == "__main__":
    import os

    PageRange = namedtuple("PageRange",'start end')

    page_range = PageRange(2,2)

    pdf_filename = "test-5_33.pdf"
    pdf_path = os.path.join(os.getcwd(), "POC", "llm_to_extract" ,pdf_filename)

    # text_filename = f"chunk_by_llm_{page_range.start}_{page_range.end}.txt"
    # text_path = os.path.join(os.getcwd(), "POC", text_filename)  # File to store extracted text


    generate_chunk_using_llm(pdf_path,page_range)