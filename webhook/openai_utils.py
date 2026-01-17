import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_openai_response(user_text):
    """
    Send user message to OpenAI and get a reply
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_text}],
            max_tokens=100
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print("OpenAI API error:", e)
        return "Sorry, I couldn't understand that."
