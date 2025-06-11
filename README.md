# First OpenAI API Call

A Python application that demonstrates how to interact with OpenAI's GPT-3.5-turbo model through their API. This project serves as a simple example of integrating OpenAI's powerful language model into your applications.

## Features

- 🤖 Connects to OpenAI's GPT-3.5-turbo model
- 💬 Uses a customizable system prompt
- 📝 Takes user input via console
- 📊 Displays detailed token usage statistics
- 🔒 Secure API key handling using environment variables

## Prerequisites

Before running this project, make sure you have:

- Python 3.6 or higher installed
- An OpenAI API key (get one at [OpenAI's platform](https://platform.openai.com/api-keys))
- pip (Python package manager)

## Installation

1. Clone this repository:

```bash
git clone https://github.com/devendra684/first-openai-api-call.git
cd first-openai-api-call
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root directory and add your OpenAI API key:

```
OPENAI_API_KEY=your-api-key-here
```

## Usage

Run the script using Python:

```bash
python first_call.py
```

The application will:

1. Prompt you to enter your question or message
2. Send your input to OpenAI's API
3. Display the AI's response
4. Show the total number of tokens used

## Example Interaction

```
Welcome to the OpenAI API Test!
--------------------------------

Enter your prompt: What is artificial intelligence?

Sending request to OpenAI...

Assistant's Response:
--------------------
[AI's response will appear here]

Token Usage:
Total tokens used: [number]
```

## Security Notes

- Never commit your `.env` file or expose your API key
- The `.env` file is included in `.gitignore` for security
- Keep your API key confidential and rotate it if compromised

## Contributing

Feel free to fork this repository and submit pull requests. You can also open issues for any bugs or feature requests.

## License

This project is open source and available under the MIT License.

## Acknowledgments

- OpenAI for providing the API
- Python-dotenv for environment variable management
