# webhook/openai_utils.py
import os
import openai

# Make sure the API key is loaded
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_openai_response(user_text: str) -> str:
    """
    Send user text to OpenAI and get a response
    """
    if not openai.api_key:
        print("OpenAI API key not set!")
        return "Sorry, I couldn't understand that."

    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_text}
            ],
            max_tokens=150
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print("OpenAI API error:", e)
        return "Sorry, I couldn't understand that."





# import os
# import openai

# openai.api_key = os.getenv("OPENAI_API_KEY")

# def get_openai_response(user_text: str) -> str:
#     """
#     Generate a reply using OpenAI GPT-3.5 / GPT-4
#     """
#     try:
#         response = openai.chat.completions.create(
#             model="gpt-3.5-turbo",
#             messages=[
#                 {"role": "system", "content": "You are a helpful assistant."},
#                 {"role": "user", "content": user_text}
#             ],
#             max_tokens=150
#         )
#         return response.choices[0].message.content.strip()
#     except Exception as e:
#         print("OpenAI API error:", e)
#         return "Sorry, I couldn't understand that."



# import os
# import openai

# openai.api_key = os.getenv("OPENAI_API_KEY")

# def get_openai_response(user_text):
#     """
#     Send user message to OpenAI and get a reply
#     """
#     try:
#         response = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",
#             messages=[{"role": "user", "content": user_text}],
#             max_tokens=100
#         )
#         return response.choices[0].message.content.strip()
#     except Exception as e:
#         print("OpenAI API error:", e)
#         return "Sorry, I couldn't understand that."
