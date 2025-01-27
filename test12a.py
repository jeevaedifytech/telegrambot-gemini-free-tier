# pdf image extracted and stored in faiss db (gemini, chatgpt), chosoe 2 options and ask question  works fine with multiple QA  
import telebot
import fitz  # PyMuPDF for PDFs
import pytesseract  # OCR for images
from PIL import Image
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss
import google.generativeai as genai
import openai  # OpenAI integration for ChatGPT
import logging
import os

# Bot and API keys
TELEGRAM_TOKEN = "repalce your token"
OPENAI_API_KEY = " "  # Replace with your OpenAI API key
GEMINI_API_KEY = "replace your token"

# Configure logging to record in a log file
log_file = 'bot_activity.log'
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    handlers=[
        logging.FileHandler(log_file),  # Log to file
        logging.StreamHandler()          # Optionally, log to console as well
    ]
)

# Configure OpenAI API
openai.api_key = OPENAI_API_KEY
# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

# Initialize the Telegram bot
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# Initialize the Sentence-Transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# FAISS index setup
embedding_dim = 384  # Embedding dimension for 'all-MiniLM-L6-v2'
index = faiss.IndexFlatL2(embedding_dim)  # Create a flat L2 index for cosine similarity

# Temporary file storage directory
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Function to extract text from PDFs
def extract_text_from_pdf(file_path):
    text = ""
    with fitz.open(file_path) as pdf:
        for page in pdf:
            text += page.get_text()
    logging.info(f"Extracted text from PDF: {file_path}")
    return text

# Function to extract text from images
def extract_text_from_image(file_path):
    image = Image.open(file_path)
    text = pytesseract.image_to_string(image)
    logging.info(f"Extracted text from image: {file_path}")
    return text
	
# Function to upload content to Google Gemini and get a response
def ask_gemini(content, question):
    logging.info(f"Querying gpt with question: {question}")
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = f"Context: {content}\nQuestion: {question}"
    try:
        response = model.generate_content(prompt)
        logging.info("Gpt response received.")
        return response.text.strip()
    except Exception as e:
        logging.error(f"Error querying Gpt: {e}")
        return "Error occurred while querying gpt."

# Function to convert text to embedding using Sentence Transformers
def text_to_embedding(text):
    sentences = text.split('\n')  # You can adjust the splitting strategy
    embeddings = model.encode(sentences, convert_to_numpy=True)  # Get embeddings for each sentence
    document_embedding = embeddings.mean(axis=0)  # Average the embeddings of sentences to get the document embedding
    return document_embedding.astype('float32')  # Ensure it’s in the correct format for FAISS

# Function to store extracted text in FAISS
def store_text_in_faiss(text):
    embedding = text_to_embedding(text)
    
    # Ensure embedding is reshaped to (1, -1) to match FAISS input requirements (2D array)
    if embedding.ndim == 1:
        embedding = embedding.reshape(1, -1)  # Reshape to 2D if necessary

    # Normalize the embedding for FAISS
    faiss.normalize_L2(embedding)  # Normalize for cosine similarity search

    # Add the embedding to FAISS index
    index.add(np.array(embedding))  # FAISS expects a numpy array
    logging.info(f"Stored text in FAISS index.")

# Function to interact with OpenAI's ChatGPT
def ask_chatgpt(content, question):
    prompt = f"Context: {content}\nQuestion: {question}"
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use the GPT-3.5 turbo model
            messages=[{"role": "system", "content": "You are a helpful assistant."},
                      {"role": "user", "content": prompt}],
            max_tokens=200
        )
        response_text = response['choices'][0]['message']['content'].strip()
        logging.info(f"ChatGPT Response: {response_text}")
        return response_text
    except Exception as e:
        logging.error(f"Error interacting with ChatGPT: {str(e)}")
        return f"Error: {str(e)}"

# Bot command handlers
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(
        message.chat.id,
        "Welcome!\nSend me a PDF or an image, and I'll extract its content and answer your questions.\nYou can use OpenSource or ChatGPT for advanced Q&A.",
    )
    logging.info(f"Sent welcome message to {message.chat.id}")

@bot.message_handler(content_types=['document', 'photo'])
def handle_file_upload(message):
    if message.document:
        # Handle PDF upload
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        file_path = os.path.join(UPLOAD_DIR, message.document.file_name)
        with open(file_path, 'wb') as f:
            f.write(downloaded_file)
        logging.info(f"Received and saved PDF: {file_path}")

        if file_path.lower().endswith('.pdf'):
            process_pdf(message, file_path)
        else:
            bot.send_message(message.chat.id, "Please upload a valid PDF or image.")
            logging.warning(f"Invalid file uploaded: {file_path}")

    elif message.photo:
        # Handle image upload
        file_info = bot.get_file(message.photo[-1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        file_path = os.path.join(UPLOAD_DIR, f"image_{message.chat.id}.jpg")
        with open(file_path, 'wb') as f:
            f.write(downloaded_file)
        logging.info(f"Received and saved image: {file_path}")
        process_image(message, file_path)

# Process PDFs
def process_pdf(message, file_path):
    bot.send_message(message.chat.id, "Extracting text from the PDF...")
    text = extract_text_from_pdf(file_path)
    if text.strip():
        store_text_in_faiss(text)  # Store text in FAISS
        ask_question(message, text, "PDF")
    else:
        bot.send_message(message.chat.id, "Could not extract any text from the PDF.")
        logging.error(f"Could not extract text from PDF: {file_path}")

# Process Images
def process_image(message, file_path):
    bot.send_message(message.chat.id, "Extracting text from the image...")
    text = extract_text_from_image(file_path)
    if text.strip():
        store_text_in_faiss(text)  # Store text in FAISS
        ask_question(message, text, "Image")
    else:
        bot.send_message(message.chat.id, "Could not extract any text from the image.")
        logging.error(f"Could not extract text from image: {file_path}")

# Ask questions based on extracted content
def ask_question(message, content, file_type):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    qa_btn = telebot.types.KeyboardButton(f"Use OpenSource")
    chatgpt_btn = telebot.types.KeyboardButton(f"Use ChatGPT")
    markup.add(qa_btn, chatgpt_btn)

    bot.send_message(
        message.chat.id, "Text extraction complete. Choose an option:", reply_markup=markup
    )
    logging.info(f"User {message.chat.id} completed text extraction, waiting for choice.")

    # Store content temporarily for this user
    bot.register_next_step_handler(
        message, handle_user_choice, content
    )

# Handle user choice between QA and ChatGPT
def handle_user_choice(message, content):
    if "Use OpenSource" in message.text:
        msg = bot.send_message(message.chat.id, "What would you like to ask?")
        bot.register_next_step_handler(msg, answer_user_query, content, "opensource")  # Register next step
        logging.info(f"User {message.chat.id} selected OpenSource QA")
    elif "Use ChatGPT" in message.text:
        msg = bot.send_message(message.chat.id, "What would you like to ask ChatGPT?")
        bot.register_next_step_handler(msg, ask_chatgpt_query, content, "chatgpt")  # Register next step
        logging.info(f"User {message.chat.id} selected ChatGPT")
    else:
        bot.send_message(message.chat.id, "Please choose a valid option.")
        logging.warning(f"User {message.chat.id} selected an invalid option.")

# Answer user query based on extracted content using FAISS
def answer_user_query(message, content, workflow):
    question = message.text
    # Convert the user's question into an embedding using the same SentenceTransformer model
    question_embedding = text_to_embedding(question)
    
    # Check if question_embedding is 1D, and reshape to 2D (1, embedding_dim)
    if question_embedding.ndim == 1:
        question_embedding = question_embedding.reshape(1, -1)
    
    # Normalize the question embedding (FAISS works with normalized vectors)
    faiss.normalize_L2(question_embedding)
    
    # Perform a search in the FAISS index to find the most relevant documents (retrieve k results)
    k = 1  # Retrieve the top 1 most relevant documents
    D, I = index.search(np.array(question_embedding), k=k)
    
    # If the search returns results, we extract the corresponding document text
    answers = []
    for i in range(k):
        # If a result is found (FAISS returns -1 for no result)
        if I[0][i] != -1:
            # Extract the content related to the most similar embedding (i.e., document snippet)
            # Get a snippet from the original content based on the position of the found result
            # For simplicity, assume that content[i] corresponds to the document text at index I[0][i]
            
            # Calculate the position in the document to extract a relevant snippet around it
            start_pos = max(0, I[0][i] - 100)  # Start a bit before the match
            end_pos = min(len(content), I[0][i] + 400)  # Extend the snippet 400 chars after the match
            
            snippet = content[start_pos:end_pos]  # Extract a snippet from the content
            answers.append(f"Result {i+1}:\n{snippet}...\n{'-'*20}")
        else:
            answers.append(f"Result {i+1}: No relevant content found.")

    # Combine all the answers into a single message (with a check for length)
    full_answer = "\n\n".join(answers)

    # Handle long answers by splitting into multiple messages
    MAX_MESSAGE_LENGTH = 4096  # Telegram message character limit
    if len(full_answer) > MAX_MESSAGE_LENGTH:
        # Split the message into multiple parts
        for i in range(0, len(full_answer), MAX_MESSAGE_LENGTH):
            bot.send_message(message.chat.id, full_answer[i:i + MAX_MESSAGE_LENGTH])
    else:
        # Send the full answer in a single message
        bot.send_message(message.chat.id, full_answer)
    
    # Ask if the user wants to continue
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    yes_btn = telebot.types.KeyboardButton("Yes")
    no_btn = telebot.types.KeyboardButton("No")
    markup.add(yes_btn, no_btn)

    msg = bot.send_message(message.chat.id, "Do you have another question?", reply_markup=markup)
    bot.register_next_step_handler(msg, continue_workflow, content, workflow)

    logging.info(f"Answered user query in {workflow} workflow: {question}")

# Ask Google Gemini a question
def ask_gemini_query(message, content):
    question = message.text
    response = ask_gemini(content, question)
    logging.info(f"User {message.chat.id} asked gpt: {question}")
    bot.send_message(message.chat.id, f"gpt Response: {response}")


# Ask ChatGPT a question
def ask_chatgpt_query(message, content, workflow):
    question = message.text
    # Get ChatGPT's response
    response = ask_chatgpt(content, question)
    bot.send_message(message.chat.id, f"ChatGPT Response: {response}")
    logging.info(f"ChatGPT responded to user query: {question}")
    
    # Ask if the user wants to continue with another question
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    yes_btn = telebot.types.KeyboardButton("Yes")
    no_btn = telebot.types.KeyboardButton("No")
    markup.add(yes_btn, no_btn)
    
    msg = bot.send_message(message.chat.id, "Do you have another question?", reply_markup=markup)
    # Register next step handler to continue workflow based on user's choice
    bot.register_next_step_handler(msg, continue_workflow, content, workflow)

    logging.info(f"Answered user query in {workflow} workflow: {question}")

# Continue the workflow or stop
def continue_workflow(message, content, workflow):
    if message.text.lower() == 'yes':
        # If the user wants to continue, ask for the next question
        msg = bot.send_message(message.chat.id, "Ask your next question:")
        # Register the next step based on the selected workflow (opensource or chatgpt)
        if workflow == "opensource":
            bot.register_next_step_handler(msg, answer_user_query, content, workflow)
        else:
            bot.register_next_step_handler(msg, ask_chatgpt_query, content, workflow)
        logging.info(f"User {message.chat.id} chose to continue asking questions.")
    elif message.text.lower() == 'no':
        # If the user wants to stop, prompt for a new file upload
        bot.send_message(message.chat.id, "Welcome back! Please upload a PDF or an image.")
        logging.info(f"User {message.chat.id} chose 'No', returning to welcome message.")
    else:
        # Handle invalid responses
        bot.send_message(message.chat.id, "Please select 'Yes' or 'No'.")
        logging.warning(f"User {message.chat.id} selected an invalid option after query.")

# Start the bot polling
bot.polling(none_stop=True)
