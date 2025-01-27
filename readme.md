----------------------------informations-----------------------


1. **Hugging Face Transformers Library**: 
   - Models like `Salesforce/blip-vqa-base` (for VQA) and `deepset/roberta-base-squad2` (for text-based QA) are downloaded directly from the Hugging Face model hub without the need for an API key. 
   - These models are loaded locally onto your system when you run the code for the first time.

2. **API-Free Implementation**: 
   - The models and processors are instantiated directly via `from_pretrained`, which downloads and caches them locally.

### Why Avoid Using API Keys?
- Using API keys is typically required for **hosted inference APIs** or enterprise features on Hugging Face (e.g., when you make remote HTTP requests to Hugging Face Inference endpoints).
- Local execution with the `transformers` library is independent of these hosted services, offering flexibility and avoiding API usage limits.

### Summary
This implementation only needs access to the pre-trained models and your local system resources, meaning no Hugging Face API key is necessary. Ensure you have internet access when running the code initially so the models can download successfully.

TELEGRAM_TOKEN = "replace your token"
HUGGINGFACE_API_KEY = "replace your token"
OPENAI_API_KEY = "replace your tokens"




