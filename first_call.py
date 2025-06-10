import os
import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set OpenAI API key
api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    raise ValueError("No OpenAI API key found. Please check your .env file.")

openai.api_key = api_key

# Define the system prompt
SYSTEM_PROMPT = """You are a helpful AI assistant that provides clear and concise responses 
to user queries. Your responses should be informative yet brief."""

def get_completion(user_prompt):
    """
    Make an API call to OpenAI and return the response and token usage.
    """
    try:
        # Make the API call
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt}
            ]
        )
        
        # Extract the response and token usage
        assistant_response = response['choices'][0]['message']['content']
        total_tokens = response['usage']['total_tokens']
        
        return assistant_response, total_tokens
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None, None

def main():
    print("\nWelcome to the OpenAI API Test!")
    print("--------------------------------")
    
    # Get user input
    user_prompt = input("\nEnter your prompt: ")
    
    print("\nSending request to OpenAI...")
    response, tokens = get_completion(user_prompt)
    
    if response:
        print("\nAssistant's Response:")
        print("--------------------")
        print(response)
        print("\nToken Usage:")
        print(f"Total tokens used: {tokens}")

if __name__ == "__main__":
    main() 