import telebot
import fitz  # PyMuPDF for PDFs
import pytesseract  # OCR for images
from PIL import Image
import faiss
import numpy as np
import google.generativeai as genai
import openai
import logging
import os
import json
import speech_recognition as sr
import subprocess  # to call ffmpeg
 
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
 
# --------------------------------------------------------------------------
#                 BOT & API KEYS
# --------------------------------------------------------------------------
TELEGRAM_TOKEN = "7855292235:AAGl3TRW1Eou8maVjHcMOnfKVLbT9u7BqeI"  # Replace with your Telegram Bot Token
OPENAI_API_KEY = " "  # Replace with your OpenAI API key
GEMINI_API_KEY = "AIzaSyAhqjWVpPCeC1ic0wC4czZp2qSNeQnf5dI"
EMBEDDING_DIM = 768  # Replace with the embedding dimension of your text_to_embedding model

# --------------------------------------------------------------------------
#                 FAISS INDEX FILE, USER PROFILES FILE
# --------------------------------------------------------------------------
FAISS_INDEX_PATH = "faiss_index.bin"
USER_PROFILES_FILE = "user_profiles.json"
 
# --------------------------------------------------------------------------
#                 LOGGING
# --------------------------------------------------------------------------
log_file = 'bot_activity.log'
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)
 
# --------------------------------------------------------------------------
#                 CONFIGURE GEMINI & OPENAI
# --------------------------------------------------------------------------
genai.configure(api_key=GEMINI_API_KEY)
gemini_model = genai.GenerativeModel("gemini-1.5-flash")
openai.api_key = OPENAI_API_KEY
 
# --------------------------------------------------------------------------
#                 TELEGRAM BOT INIT
# --------------------------------------------------------------------------
bot = telebot.TeleBot(TELEGRAM_TOKEN)
 
# --------------------------------------------------------------------------
#                 JSON-BASED USER PROFILES
# --------------------------------------------------------------------------
def load_user_profiles():
    """Loads user profiles from JSON if it exists, else returns empty dict."""
    if os.path.exists(USER_PROFILES_FILE):
        with open(USER_PROFILES_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}
 
def save_user_profiles(user_data):
    """Saves user_data (dict) to the JSON file."""
    with open(USER_PROFILES_FILE, "w", encoding="utf-8") as f:
        json.dump(user_data, f, indent=4)
 
# In-memory user profiles
user_profiles = load_user_profiles()
 
def user_exists(user_id):
    return str(user_id) in user_profiles
 
def get_user_data(user_id):
    """Returns a dict { 'age': ..., 'education': ..., 'disability': ... } or empty."""
    return user_profiles.get(str(user_id), {})
 
def create_or_update_user(user_id, age=None, education=None, disability=None):
    """Creates or updates user info in the JSON store and saves."""
    uid = str(user_id)
    if uid not in user_profiles:
        # create an empty profile
        user_profiles[uid] = {
            "age": None,
            "education": None,
            "disability": None
        }
    if age is not None:
        user_profiles[uid]["age"] = age
    if education is not None:
        user_profiles[uid]["education"] = education
    if disability is not None:
        user_profiles[uid]["disability"] = disability
 
    save_user_profiles(user_profiles)
 
# --------------------------------------------------------------------------
#                 NEW USER REGISTRATION FLOW
# --------------------------------------------------------------------------
NEW_USER_QUESTIONS = [
    "What is your age?",
    "What is your educational qualification?",
    "Please select the type of disability from the below options"
]
 
DISABILITY_OPTIONS = [
    "Blindness (B / VI)",
    "Low Vision (LV / VI)",
    "Leprosy Cured Persons (LCP)",
    "Hearing Impairment (HI)",
    "Locomotor Disability (LD / OH)",
    "Dwarfism (DW)",
    "Intellectual Disability (ID)",
    "Mental Illness (MI)",
    "Autism Spectrum Disorder (ASD)",
    "Cerebral Palsy (CP)",
    "Muscular Dystrophy (MD)",
    "Chronic Neurological Conditions (CNC)",
    "Specific Learning Disabilities (SLD)",
    "Multiple Sclerosis (MS)",
    "Speech & Language Disability (Sp&LD)",
    "Thalassemia (TH)",
    "Hemophilia (HEM)",
    "Sickle Cell Disease (SCD)",
    "Multiple Disabilities (MultiD)",
    "Acid Attack Victims (AAV)",
    "Parkinson’s Disease (PD)"
]
DISABILITY_OPTIONS_CLEAN = {opt.lower() for opt in DISABILITY_OPTIONS}
 
# Track which question index a user is on
new_user_question_index = {}
 
# --------------------------------------------------------------------------
#                 FILE STORAGE / FAISS INDEX
# --------------------------------------------------------------------------
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)
 
user_files = {}  # { user_id: [file paths] }
 
def load_faiss_index():
    if os.path.exists(FAISS_INDEX_PATH):
        logging.info("Loading existing FAISS index...")
        return faiss.read_index(FAISS_INDEX_PATH)
    logging.info("Creating new FAISS index...")
    return faiss.IndexFlatL2(EMBEDDING_DIM)
 
index = load_faiss_index()
 
def save_faiss_index():
    faiss.write_index(index, FAISS_INDEX_PATH)
    logging.info("FAISS index saved.")
 
def text_to_embedding(text):
    # Replace with your own embedding logic
    emb = np.random.rand(EMBEDDING_DIM).astype(np.float32)
    return emb
 
def store_text_in_faiss(text):
    try:
        emb = text_to_embedding(text)
        emb = emb.reshape(1, -1)
        faiss.normalize_L2(emb)
        index.add(emb)
        save_faiss_index()
        logging.info("Text stored in FAISS successfully.")
    except Exception as e:
        logging.error(f"Error storing text in FAISS: {str(e)}")
 
# PDF / Image extraction
def extract_text_from_pdf(file_path):
    text = ""
    with fitz.open(file_path) as pdf:
        for page in pdf:
            text += page.get_text()
    return text
 
def extract_text_from_image(file_path):
    image = Image.open(file_path)
    return pytesseract.image_to_string(image)
 
# --------------------------------------------------------------------------
#                 Q&A (Gemini / ChatGPT)
# --------------------------------------------------------------------------
def ask_gemini(content, question):
    logging.info(f"Querying Gemini with question: {question}")
    prompt = f"Context: {content}\nQuestion: {question}"
    try:
        response = gemini_model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        logging.error(f"Error querying Gemini: {e}")
        return "Error occurred while querying Gemini."
 
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
        return response.choices[0].message.content.strip()
    except Exception as e:
        logging.error(f"Error querying ChatGPT: {e}")
        return "Error occurred while querying ChatGPT."
 
# --------------------------------------------------------------------------
#                 USER SESSION STATES (Q&A Flow)
# --------------------------------------------------------------------------
user_sessions = {}  
# e.g. user_sessions[user_id] = {
#   'content': <string of extracted text>,
#   'workflow': 'gemini' or 'chatgpt',
#   'awaiting_question': bool,
#   'awaiting_yes_no': bool
# }
 
# --------------------------------------------------------------------------
#                 HANDLERS: START, HELP
# --------------------------------------------------------------------------
@bot.message_handler(commands=['start','help'])
def send_welcome(message):
    user_id = str(message.chat.id)
    logging.info(f"User {user_id} triggered /start or /help")
 
    # If user isn't in JSON yet, we ask new user Q's
    if not user_exists(user_id):
        create_or_update_user(user_id)  # create empty
        new_user_question_index[user_id] = 0
        bot.send_message(message.chat.id, "Welcome! Before we proceed, I need some information from you.")
        ask_new_user_question(message)
    else:
        # Already registered
        show_main_menu(message)
 
# --------------------------------------------------------------------------
#                 NEW USER QUESTIONS
# --------------------------------------------------------------------------
def ask_new_user_question(message):
    user_id = str(message.chat.id)
    idx = new_user_question_index.get(user_id, 0)
 
    if idx < len(NEW_USER_QUESTIONS):
        question = NEW_USER_QUESTIONS[idx]
        # For the 3rd question, let's show disability options as buttons
        if idx == 2:
            markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
            row = []
            for i, option in enumerate(DISABILITY_OPTIONS, start=1):
                row.append(KeyboardButton(option))
                if i % 3 == 0:
                    markup.add(*row)
                    row = []
            if row:
                markup.add(*row)
            msg = bot.send_message(user_id, question, reply_markup=markup)
            bot.register_next_step_handler(msg, store_new_user_answer)
        else:
            msg = bot.send_message(user_id, question)
            bot.register_next_step_handler(msg, store_new_user_answer)
    else:
        bot.send_message(user_id, "Thank you! Your information has been recorded.")
        show_main_menu(message)
 
def store_new_user_answer(message):
    user_id = str(message.chat.id)
    idx = new_user_question_index.get(user_id, 0)
    user_answer = message.text.strip() if message.text else ""
 
    # 1) Age must be digit
    if idx == 0:
        if not user_answer.isdigit():
            bot.send_message(user_id, "Age must be a number. Try again.")
            ask_new_user_question(message)
            return
        create_or_update_user(user_id, age=user_answer)
   
    # 2) Education (no special validation)
    elif idx == 1:
        create_or_update_user(user_id, education=user_answer)
   
    # 3) Disability => must be in DISABILITY_OPTIONS
    elif idx == 2:
        if user_answer.lower() not in DISABILITY_OPTIONS_CLEAN:
            bot.send_message(user_id, "Please select a valid disability option.")
            ask_new_user_question(message)
            return
        create_or_update_user(user_id, disability=user_answer)
 
    new_user_question_index[user_id] = idx + 1
    ask_new_user_question(message)
 
# --------------------------------------------------------------------------
#                 MAIN MENU
# --------------------------------------------------------------------------
def show_main_menu(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    upload_button = KeyboardButton("Upload New Files")
    continue_button = KeyboardButton("Continue Chat")
    markup.add(upload_button, continue_button)
 
    bot.send_message(
        message.chat.id,
        "Welcome!\nSend me PDFs or images, and I'll extract their content. Then ask me questions about them!\n\n"
        "1) Upload new files\n"
        "2) Continue chat\n",
        reply_markup=markup
    )
 
# --------------------------------------------------------------------------
#                 "UPLOAD NEW FILES" HANDLER
# --------------------------------------------------------------------------
@bot.message_handler(func=lambda m: m.text == "Upload New Files")
def handle_upload_option(message):
    bot.send_message(
        message.chat.id,
        "Great! Upload PDF or image files. Send them one at a time, then type 'done' when finished."
    )
 
# --------------------------------------------------------------------------
#                 "CONTINUE CHAT" HANDLER
# --------------------------------------------------------------------------
@bot.message_handler(func=lambda m: m.text == "Continue Chat")
def handle_continue_chat_option(message):
    user_id = message.chat.id
    if (user_id not in user_sessions) or (not user_sessions[user_id].get('content')):
        bot.send_message(user_id, "No previous chat found. Please upload new files first.")
    else:
        bot.send_message(user_id, "Resuming previous chat. Ask your question or type 'Use Gemini' / 'Use ChatGPT'.")
 
# --------------------------------------------------------------------------
#                 FILE UPLOAD HANDLER
# --------------------------------------------------------------------------
@bot.message_handler(content_types=['document','photo'])
def handle_file_upload(message):
    user_id = message.chat.id
    user_files.setdefault(user_id, [])
 
    # If user sends a document
    if message.document:
        file_name = message.document.file_name.lower()
        if not (file_name.endswith('.pdf') or file_name.endswith('.jpg') or file_name.endswith('.jpeg')):
            bot.send_message(user_id, "⚠ Invalid format! Only PDF or JPG allowed.")
            return
 
        file_info = bot.get_file(message.document.file_id)
        downloaded = bot.download_file(file_info.file_path)
        file_path = os.path.join(UPLOAD_DIR, file_name)
        with open(file_path, 'wb') as f:
            f.write(downloaded)
 
        # If PDF, check page count
        if file_name.endswith('.pdf'):
            try:
                with fitz.open(file_path) as pdf:
                    if pdf.page_count > 200:
                        bot.send_message(user_id, "⚠ This PDF exceeds 200 pages limit!")
                        os.remove(file_path)
                        return
            except Exception as e:
                bot.send_message(user_id, "Error reading PDF. Please re-upload a valid PDF.")
                return
 
        user_files[user_id].append(file_path)
        bot.send_message(user_id, f"✅ '{file_name}' uploaded. Upload more or type 'done'.")
 
    # If user sends a photo
    elif message.photo:
        file_info = bot.get_file(message.photo[-1].file_id)
        downloaded = bot.download_file(file_info.file_path)
        file_path = os.path.join(UPLOAD_DIR, f"image_{user_id}_{len(user_files[user_id]) + 1}.jpg")
        with open(file_path, 'wb') as f:
            f.write(downloaded)
 
        user_files[user_id].append(file_path)
        bot.send_message(user_id, "✅ Image uploaded. Upload more or type 'done'.")
    else:
        bot.send_message(user_id, "⚠ Unsupported file type! Only PDF or JPG allowed.")
 
# --------------------------------------------------------------------------
#                 "DONE" => PROCESS UPLOADED FILES
# --------------------------------------------------------------------------
@bot.message_handler(func=lambda m: m.text and m.text.lower() == 'done')
def process_uploaded_files(message):
    user_id = message.chat.id
 
    if user_id not in user_files or not user_files[user_id]:
        bot.send_message(user_id, "No files uploaded. Please upload first.")
        return
 
    bot.send_message(user_id, "Processing files...")
    combined_text = ""
 
    for fp in user_files[user_id]:
        if fp.lower().endswith('.pdf'):
            combined_text += extract_text_from_pdf(fp)
        else:
            combined_text += extract_text_from_image(fp)
 
    if combined_text.strip():
        bot.send_message(user_id, "Text extraction done.")
        store_text_in_faiss(combined_text)
        user_sessions[user_id] = {
            'content': combined_text,
            'workflow': 'gemini',  # default
            'awaiting_question': False,
            'awaiting_yes_no': False
        }
        ask_which_qa(message)
    else:
        bot.send_message(user_id, "No text found in the files.")
 
    user_files[user_id] = []  # clear the list after processing
 
def ask_which_qa(message):
    markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    gemini_btn = KeyboardButton("Use Gemini")
    chatgpt_btn = KeyboardButton("Use ChatGPT")
    markup.add(gemini_btn, chatgpt_btn)
 
    bot.send_message(
        message.chat.id,
        "Choose a Q&A method:",
        reply_markup=markup
    )
 
# --------------------------------------------------------------------------
#                 VOICE HANDLER
# --------------------------------------------------------------------------
@bot.message_handler(content_types=['voice'])
def handle_voice_message(message):
    user_id = message.chat.id
    file_info = bot.get_file(message.voice.file_id)
 
    # Save .ogg
    ogg_path = os.path.join(UPLOAD_DIR, f"voice_{user_id}_{message.message_id}.ogg")
    downloaded = bot.download_file(file_info.file_path)
    with open(ogg_path, 'wb') as f:
        f.write(downloaded)
 
    # Convert to .wav
    wav_path = ogg_path.replace('.ogg', '.wav')
    cmd = ["ffmpeg", "-y", "-i", ogg_path, wav_path]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
 
    # Transcribe
    recognizer = sr.Recognizer()
    with sr.AudioFile(wav_path) as source:
        audio_data = recognizer.record(source)
 
    try:
        recognized_text = recognizer.recognize_google(audio_data, language="en-US").strip()
        bot.send_message(user_id, f"🎤 Voice transcription: {recognized_text}")
 
        # We fake a text message for the same logic
        pseudo_msg = message
        pseudo_msg.text = recognized_text
        interpret_user_message(pseudo_msg)
 
    except sr.UnknownValueError:
        bot.send_message(user_id, "Sorry, couldn't understand the audio.")
    except sr.RequestError as e:
        bot.send_message(user_id, "Speech recognition error, please try again.")
 
# --------------------------------------------------------------------------
#                 FALLBACK TEXT => interpret
# --------------------------------------------------------------------------
@bot.message_handler(func=lambda m: True, content_types=['text'])
def fallback_text_handler(message):
    interpret_user_message(message)
 
# --------------------------------------------------------------------------
#                 INTERPRET USER MESSAGE
# --------------------------------------------------------------------------
def interpret_user_message(message):
    user_id = message.chat.id
    text_in = (message.text or "").strip().lower()
 
    # 1) If user is in the new user registration flow
    if user_id in new_user_question_index and new_user_question_index[user_id] < len(NEW_USER_QUESTIONS):
        store_new_user_answer(message)
        return
 
    # 2) Common commands
    if text_in in ["upload new files", "upload files", "upload"]:
        handle_upload_option(message)
        return
    if text_in == "done":
        process_uploaded_files(message)
        return
    if text_in in ["continue chat", "continue", "chat"]:
        handle_continue_chat_option(message)
        return
 
    # "Use Gemini" or "Use ChatGPT"
    if "use gemini" in text_in:
        user_sessions.setdefault(user_id, {})
        user_sessions[user_id]['workflow'] = 'gemini'
        user_sessions[user_id]['awaiting_question'] = True
        user_sessions[user_id]['awaiting_yes_no'] = False
        bot.send_message(user_id, "What would you like to ask Gemini?")
        return
 
    if "use chatgpt" in text_in:
        user_sessions.setdefault(user_id, {})
        user_sessions[user_id]['workflow'] = 'chatgpt'
        user_sessions[user_id]['awaiting_question'] = True
        user_sessions[user_id]['awaiting_yes_no'] = False
        bot.send_message(user_id, "What would you like to ask ChatGPT?")
        return
 
    # 3) If user is in Q&A flow
    if user_id in user_sessions:
        session = user_sessions[user_id]
        # If user is awaiting a question (Gemini or ChatGPT)
        if session.get('awaiting_question'):
            question = message.text.strip()
            content = session.get('content', "")
            workflow = session.get('workflow', 'gemini')
 
            # Ask Gemini or ChatGPT
            if workflow == "gemini":
                response = ask_gemini(content, question)
                bot.send_message(user_id, f"Gemini Response: {response}")
            else:
                response = ask_chatgpt(content, question)
                bot.send_message(user_id, f"ChatGPT Response: {response}")
 
            # Now ask if they have another question, but show Yes/No buttons
            session['awaiting_question'] = False
            session['awaiting_yes_no'] = True
 
            yes_no_markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
            yes_btn = KeyboardButton("Yes")
            no_btn = KeyboardButton("No")
            yes_no_markup.add(yes_btn, no_btn)
 
            bot.send_message(
                user_id,
                "Do you have another question? (Yes/No)",
                reply_markup=yes_no_markup
            )
            return
 
        # If user is awaiting a yes/no answer
        if session.get('awaiting_yes_no'):
            if text_in == "yes":
                # Continue Q&A => ask for next question
                session['awaiting_question'] = True
                session['awaiting_yes_no'] = False
                bot.send_message(user_id, "Please ask your next question:")
                return
            elif text_in == "no":
                # Stop Q&A => show main menu (or any other flow)
                session['awaiting_question'] = False
                session['awaiting_yes_no'] = False
                show_main_menu(message)
                return
            else:
                # If invalid response, re-prompt yes/no
                bot.send_message(user_id, "Invalid response. Please say 'Yes' or 'No'.")
                return
 
    # 4) Otherwise, show main menu
    show_main_menu(message)
 
# --------------------------------------------------------------------------
#                 START BOT
# --------------------------------------------------------------------------
bot.polling(none_stop=True)