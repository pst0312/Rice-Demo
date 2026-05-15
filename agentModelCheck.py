import os
from dotenv import load_dotenv
from openai import OpenAI

# 1. Load the specific env file
load_dotenv("info.env") 

# 2. Pull the variable
api_key = os.getenv("SUPER_SECRET_API_KEY")

if not api_key:
    print("0 - API Key not found!")
else:
    print("1 - API Key loaded.")
    
    # 3. Initialize client ONLY if the key exists
    try:
        client = OpenAI(api_key=api_key)
        
        # 4. Fetch and print models
        models = client.models.list()
        for model in models.data:
            print(model.id)
            
    except Exception as e:
        print(f"An error occurred: {e}")