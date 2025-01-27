# pdf image extracted and stored in faiss db (gemini only), chosoe 2 options and ask question  works fine with multiple QA  
# showed demo for this code
import telebot
import fitz  # PyMuPDF for PDFs
import pytesseract  # OCR for images
from PIL import Image
import google.generativeai as genai
import openai
import logging
import os

# Bot and API keys
TELEGRAM_TOKEN = " replace your token"
OPENAI_API_KEY = ""  # Replace with your OpenAI API key
GEMINI_API_KEY = "replace your token"

# Configure logging
log_file = 'bot_activity.log'
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)

# Configure Google Gemini and OpenAI APIs
genai.configure(api_key=GEMINI_API_KEY)
gemini_model = genai.GenerativeModel("gemini-1.5-flash")
openai.api_key = OPENAI_API_KEY

# Initialize the Telegram bot
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# Temporary file storage directory
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# To store user files temporarily
user_files = {}

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
    logging.info(f"Querying Gemini with question: {question}")
    prompt = f"Context: {content}\nQuestion: {question}"
    try:
        # Use the correct method for generating text with Gemini
        response = genai.GenerativeModel("gemini-1.5-flash").generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        logging.error(f"Error querying Gemini: {e}")
        return "Error occurred while querying Gemini."

# Function to query ChatGPT
def ask_chatgpt(content, question):
    logging.info(f"Querying ChatGPT with question: {question}")
    prompt = f"Context: {content}\nQuestion: {question}"
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an AI assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        logging.error(f"Error querying ChatGPT: {e}")
        return "Error occurred while querying ChatGPT."

# Bot command handlers
@bot.message_handler(commands=['start','file', 'help'])
def send_welcome(message):
    bot.send_message(
        message.chat.id,
        "Welcome!\nSend me multiple PDFs or images, and I'll extract their content and answer your questions.\nChoose Gemini  for Q&A when ready.",
    )
    logging.info(f"Sent welcome message to {message.chat.id}")

@bot.message_handler(content_types=['document', 'photo'])
def handle_file_upload(message):
    user_id = message.chat.id
    user_files.setdefault(user_id, [])

    if message.document:
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        file_path = os.path.join(UPLOAD_DIR, message.document.file_name)
        with open(file_path, 'wb') as f:
            f.write(downloaded_file)
        logging.info(f"Received and saved file: {file_path}")

        user_files[user_id].append(file_path)
        bot.send_message(user_id, f"File '{message.document.file_name}' uploaded. Send more files or type 'done' to process.")

    elif message.photo:
        file_info = bot.get_file(message.photo[-1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        file_path = os.path.join(UPLOAD_DIR, f"image_{user_id}_{len(user_files[user_id]) + 1}.jpg")
        with open(file_path, 'wb') as f:
            f.write(downloaded_file)
        logging.info(f"Received and saved image: {file_path}")

        user_files[user_id].append(file_path)
        bot.send_message(user_id, "Image uploaded. Send more files or type 'done' to process.")

@bot.message_handler(func=lambda message: message.text.lower() == 'done')
def process_uploaded_files(message):
    user_id = message.chat.id
    if user_id not in user_files or not user_files[user_id]:
        bot.send_message(user_id, "No files uploaded. Please upload files first.")
        return

    bot.send_message(user_id, "Processing files and extracting text...")
    combined_text = ""

    for file_path in user_files[user_id]:
        if file_path.lower().endswith('.pdf'):
            combined_text += extract_text_from_pdf(file_path)
        else:
            combined_text += extract_text_from_image(file_path)

    if combined_text.strip():
        bot.send_message(user_id, "Text extraction complete.")
        ask_question(message, combined_text)
    else:
        bot.send_message(user_id, "Could not extract any text from the files.")

    # Clear the user's file list after processing
    user_files[user_id] = []

def ask_question(message, content):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    gemini_btn = telebot.types.KeyboardButton("Use Gemini")
    # chatgpt_btn = telebot.types.KeyboardButton("Use ChatGPT")
    # markup.add(gemini_btn, chatgpt_btn)
    markup.add(gemini_btn)
    bot.send_message(
        message.chat.id, "Choose an option for Q&A:", reply_markup=markup
    )

    bot.register_next_step_handler(
        message, handle_user_choice, content
    )

def handle_user_choice(message, content):
    if "Use Gemini" in message.text:
        msg = bot.send_message(message.chat.id, "What would you like to ask Gemini?")
        bot.register_next_step_handler(msg, ask_gemini_query, content)
    elif "Use ChatGPT" in message.text:
        msg = bot.send_message(message.chat.id, "What would you like to ask ChatGPT?")
        bot.register_next_step_handler(msg, ask_chatgpt_query, content)
    else:
        bot.send_message(message.chat.id, "Please choose a valid option.")

# Ask Google Gemini a question
def ask_gemini_query(message, content):
    question = message.text
    response = ask_gemini(content, question)
    logging.info(f"User {message.chat.id} asked Gemini: {question}")
    bot.send_message(message.chat.id, f"Gemini Response: {response}")
    
    # Now, prompt the user for another question
    ask_another_question(message, content, "gemini")

# Ask ChatGPT a question
def ask_chatgpt_query(message, content, workflow):
    question = message.text
    # Get ChatGPT's response
    response = ask_chatgpt(content, question)
    bot.send_message(message.chat.id, f"ChatGPT Response: {response}")
    logging.info(f"ChatGPT responded to user query: {question}")
    
    # Now, prompt the user for another question
    ask_another_question(message, content, workflow)

# Ask if the user has another question
def ask_another_question(message, content, workflow):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    yes_btn = telebot.types.KeyboardButton("Yes")
    no_btn = telebot.types.KeyboardButton("No")
    markup.add(yes_btn, no_btn)
    
    msg = bot.send_message(message.chat.id, "Do you have another question?", reply_markup=markup)
    bot.register_next_step_handler(msg, continue_workflow, content, workflow)
    logging.info(f"Prompted user {message.chat.id} for another question.")
# Continue the workflow or stop
# Define a wrapper function to pass content and workflow along with the message
def ask_chatgpt_with_args(message, content, workflow):
    return ask_chatgpt_query(message, content, workflow)

def continue_workflow(message, content, workflow):
    if message.text.lower() == 'yes':
        # If the user wants to continue, ask for the next question
        msg = bot.send_message(message.chat.id, "Ask your next question:")
        if workflow == "gemini":
            bot.register_next_step_handler(msg, ask_gemini_query, content)
        else:
            bot.register_next_step_handler(msg, ask_chatgpt_with_args, content, workflow)
        logging.info(f"User {message.chat.id} chose to continue asking questions.")
    elif message.text.lower() == 'no':
        # If the user wants to stop, prompt for a new file upload
        bot.send_message(message.chat.id, "Welcome back! Please upload a PDF or an image.")
        logging.info(f"User {message.chat.id} chose 'No', returning to welcome message.")
    else:
        # Handle invalid responses and re-prompt
        bot.send_message(message.chat.id, "Invalid response. Please select 'Yes' or 'No'.")
        logging.warning(f"User {message.chat.id} selected an invalid option: {message.text}. Re-prompting.")
        
        # Re-prompt the user with the same question
        markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        yes_btn = telebot.types.KeyboardButton("Yes")
        no_btn = telebot.types.KeyboardButton("No")
        markup.add(yes_btn, no_btn)

        msg = bot.send_message(
            message.chat.id,
            "Do you have another question? Please choose 'Yes' or 'No'.",
            reply_markup=markup
        )
        bot.register_next_step_handler(msg, continue_workflow, content, workflow)

# Start the bot polling
bot.polling(none_stop=True)
