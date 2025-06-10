# First OpenAI API Call

A simple Python script that demonstrates how to make API calls to OpenAI's GPT-3.5-turbo model.

## Features

- Makes API calls to OpenAI's GPT-3.5-turbo model
- Uses a fixed system prompt
- Takes user input via console
- Displays the assistant's response and token usage

## Setup

1. Clone this repository:
```bash
git clone https://github.com/your-username/first-openai-api-call.git
cd first-openai-api-call
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root and add your OpenAI API key:
```
OPENAI_API_KEY=your-api-key-here
```

## Running the Script

Run the script using Python:
```bash
python first_call.py
```

The script will:
1. Prompt you for your input
2. Make an API call to OpenAI
3. Display the assistant's response
4. Show the total token usage

## Note
Make sure not to commit your API key. The `.env` file is included in `.gitignore` for security. 