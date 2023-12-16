import gradio as gr
import requests
import os

def generate_story(message):
    # Get API key from environment variable
    api_key = os.getenv('MY_API_KEY')

    # API URL
    url = 'https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent'

    # Request body
    data = {
        "contents": [{
            "parts": [{
                "text": message  # Use message from user
            }]
        }]
    }

    # Request header
    headers = {'Content-Type': 'application/json'}

    # Send API request and get response
    response = requests.post(url, headers=headers, json=data, params={'key': api_key})

    # If response is in JSON format, use response.json() to get data
    if response.status_code == 200:
        try:
            # Extract necessary data from JSON response
            return response.json()["candidates"][0]["content"]["parts"][0]["text"]
        except (KeyError, IndexError) as e:
            return f"Error processing response: {e}"
    else:
        return f"Error: {response.status_code}\n{response.text}"

# Create chat interface for Gradio
chat = gr.ChatInterface(
    fn=generate_story
)

# Start the interface
chat.queue().launch()
