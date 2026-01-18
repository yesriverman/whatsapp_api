

import os
import requests

HF_API_KEY = os.getenv("HF_API_KEY")
HF_MODEL = "tiiuae/falcon-7b-instruct"  # or any other chat-capable model

def get_hf_response(prompt: str) -> str:
    if not HF_API_KEY:
        print("HF API key not set!")
        return "Sorry, I couldn't understand that."

    # Correct URL for the Router API
    url = f"https://api-inference.huggingface.co/models/{HF_MODEL}"
    headers = {
        "Authorization": f"Bearer {HF_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 256,
            "return_full_text": False
        }
    }

    try:
        print("Calling Hugging Face Router API...")
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        print("HF raw response:", response.text)
        response.raise_for_status()
        data = response.json()

        if isinstance(data, list) and "generated_text" in data[0]:
            return data[0]["generated_text"].strip()

        return "Sorry, I couldn't understand that."

    except Exception as e:
        print("Hugging Face API exception:", e)
        return "Sorry, I couldn't understand that."


# import os
# import requests

# HF_API_KEY = os.getenv("HF_API_KEY")
# HF_MODEL = "tiiuae/falcon-7b-instruct"  # you can change to any chat-capable model

# def get_hf_response(prompt: str) -> str:
#     if not HF_API_KEY:
#         print("HF API key not set!")
#         return "Sorry, I couldn't understand that."

#     url = f"https://api-inference.huggingface.co/models/{HF_MODEL}"
#     headers = {
#         "Authorization": f"Bearer {HF_API_KEY}",
#         "Content-Type": "application/json"
#     }

#     # Router API expects "inputs" and "parameters"
#     payload = {
#         "inputs": prompt,
#         "parameters": {
#             "max_new_tokens": 256,
#             "return_full_text": False
#         }
#     }

#     try:
#         print("Calling Hugging Face Router API...")
#         response = requests.post(url, headers=headers, json=payload, timeout=30)
#         print("HF raw response:", response.text)
#         response.raise_for_status()
#         data = response.json()

#         # Most models return a list with a dict containing "generated_text"
#         if isinstance(data, list) and "generated_text" in data[0]:
#             return data[0]["generated_text"].strip()

#         return "Sorry, I couldn't understand that."

#     except Exception as e:
#         print("Hugging Face API exception:", e)
#         return "Sorry, I couldn't understand that."



# import os
# import requests

# HF_API_KEY = os.getenv("HF_API_KEY")
# HF_MODEL = "tiiuae/falcon-7b-instruct"  # or any other chat-capable model

# def get_hf_response(prompt: str) -> str:
#     if not HF_API_KEY:
#         print("HF API key not set!")
#         return "Sorry, I couldn't understand that."

#     headers = {
#         "Authorization": f"Bearer {HF_API_KEY}",
#         "Content-Type": "application/json"
#     }

#     payload = {
#         "inputs": prompt,
#         "parameters": {"max_new_tokens": 256}
#     }

#     try:
#         print("Calling Hugging Face Inference API...")
#         response = requests.post(
#             f"https://api-inference.huggingface.co/models/{HF_MODEL}",
#             headers=headers,
#             json=payload,
#             timeout=30
#         )

#         print("HF raw response:", response.text)
#         response.raise_for_status()
#         data = response.json()

#         # Falcon returns text in "generated_text"
#         if isinstance(data, list) and "generated_text" in data[0]:
#             return data[0]["generated_text"].strip()
#         return "Sorry, I couldn't understand that."

#     except Exception as e:
#         print("Hugging Face API exception:", e)
#         return "Sorry, I couldn't understand that."



# import os
# import requests

# HF_API_KEY = os.getenv("HF_API_KEY")
# HF_MODEL = "tiiuae/falcon-7b-instruct"

# def get_hf_response(prompt: str) -> str:
#     if not HF_API_KEY:
#         print("HF API key not set!")
#         return "Sorry, I couldn't understand that."

#     headers = {
#         "Authorization": f"Bearer {HF_API_KEY}",
#         "Content-Type": "application/json"
#     }


#     payload = {
#         "model": HF_MODEL,
#         "messages": [{"role": "user", "content": prompt}],
#         "max_new_tokens": 256
#     }

#     try:
#         print("Calling Hugging Face Router API...")
#         response = requests.post(
#             "https://router.huggingface.co/api/v1/chat/completions",
#             headers=headers,
#             json=payload,
#             timeout=30
#         )

#         print("HF raw response:", response.text)

#         response.raise_for_status()  # raise error for HTTP 4xx/5xx

#         data = response.json()
#         reply = data["choices"][0]["message"]["content"].strip()
#         print("HF reply:", reply)
#         return reply

#     except Exception as e:
#         print("Hugging Face API exception:", e)
#         return "Sorry, I couldn't understand that."





# import os
# import requests

# HF_API_KEY = os.getenv("HF_API_KEY")
# HF_MODEL = "tiiuae/falcon-7b-instruct"

# def get_hf_response(prompt: str) -> str:
#     if not HF_API_KEY:
#         print("HF API key not set!")
#         return "Sorry, I couldn't understand that."

#     headers = {
#         "Authorization": f"Bearer {HF_API_KEY}",
#         "Content-Type": "application/json"
#     }

#     payload = {
#         "model": HF_MODEL,
#         "messages": [{"role": "user", "content": prompt}],
#         "max_new_tokens": 256
#     }

#     try:
#         print("Calling Hugging Face Router API...")
#         response = requests.post(
#             "https://router.huggingface.co/api/v1/chat/completions",
#             headers=headers,
#             json=payload,
#             timeout=30
#         )

#         print("HF raw response:", response.text)

#         response.raise_for_status()  # raise error for HTTP 4xx/5xx

#         data = response.json()
#         reply = data["choices"][0]["message"]["content"].strip()
#         print("HF reply:", reply)
#         return reply

#     except Exception as e:
#         print("Hugging Face API exception:", e)
#         return "Sorry, I couldn't understand that."






# # import os
# # import requests

# # HF_API_KEY = os.getenv("HF_API_KEY")
# # HF_MODEL = "tiiuae/falcon-7b-instruct"

# # def get_hf_response(prompt: str) -> str:
# #     if not HF_API_KEY:
# #         print("HF API key not set!")
# #         return "Sorry, I couldn't understand that."

# #     headers = {
# #         "Authorization": f"Bearer {HF_API_KEY}",
# #         "Content-Type": "application/json"
# #     }

# #     payload = {
# #         "model": HF_MODEL,
# #         "messages": [{"role": "user", "content": prompt}],
# #         "max_new_tokens": 256
# #     }

# #     try:
# #         print("Calling Hugging Face Router API...")
# #         response = requests.post(
# #             "https://router.huggingface.co/api/v1/chat/completions",
# #             headers=headers,
# #             json=payload,
# #             timeout=30
# #         )

# #         # Debug: print raw response
# #         print("HF raw response:", response.text)

# #         response.raise_for_status()  # raise error for HTTP codes 4xx/5xx

# #         result = response.json()
# #         if "error" in result:
# #             print("Hugging Face API returned error:", result["error"])
# #             return "Sorry, I couldn't understand that."

# #         reply = result["choices"][0]["message"]["content"].strip()
# #         print("HF reply:", reply)
# #         return reply

# #     except Exception as e:
# #         print("Hugging Face API exception:", e)
# #         return "Sorry, I couldn't understand that."





# # # import os
# # # import requests

# # # HF_API_KEY = os.getenv("HF_API_KEY")
# # # HF_MODEL = "tiiuae/falcon-7b-instruct"

# # # def get_hf_response(prompt: str) -> str:
# # #     if not HF_API_KEY:
# # #         print("HF API key not set!")
# # #         return "Sorry, I couldn't understand that."

# # #     headers = {"Authorization": f"Bearer {HF_API_KEY}"}
# # #     payload = {
# # #         "model": HF_MODEL,
# # #         "messages": [{"role": "user", "content": prompt}],
# # #         "max_new_tokens": 256
# # #     }

# # #     try:
# # #         response = requests.post(
# # #             "https://router.huggingface.co/api/v1/chat/completions",
# # #             headers=headers,
# # #             json=payload,
# # #             timeout=20
# # #         )
# # #         result = response.json()
# # #         if "error" in result:
# # #             print("Hugging Face API error:", result["error"])
# # #             return "Sorry, I couldn't understand that."
# # #         return result["choices"][0]["message"]["content"].strip()
# # #     except Exception as e:
# # #         print("Hugging Face API exception:", e)
# # #         return "Sorry, I couldn't understand that."






# # # # import os
# # # # import requests

# # # # HF_API_KEY = os.getenv("HF_API_KEY")
# # # # HF_MODEL = "tiiuae/falcon-7b-instruct"  # instruction-tuned model

# # # # def get_hf_response(prompt: str) -> str:
# # # #     if not HF_API_KEY:
# # # #         print("HF API key not set!")
# # # #         return "Sorry, I couldn't understand that."

# # # #     headers = {"Authorization": f"Bearer {HF_API_KEY}"}
# # # #     payload = {"inputs": prompt}

# # # #     try:
# # # #         response = requests.post(
# # # #             f"https://router.huggingface.co/api/v1/chat/completions",
# # # #             headers={"Authorization": f"Bearer {HF_API_KEY}"},
# # # #             json={
# # # #                 "model": HF_MODEL,
# # # #                 "messages": [{"role": "user", "content": prompt}],
# # # #                 "max_new_tokens": 256
# # # #             },
# # # #             timeout=20
# # # #         )

# # # #         result = response.json()
# # # #         if "error" in result:
# # # #             print("Hugging Face API error:", result["error"])
# # # #             return "Sorry, I couldn't understand that."
# # # #         # return the generated text
# # # #         return result[0]["generated_text"].strip()
# # # #     except Exception as e:
# # # #         print("Hugging Face API exception:", e)
# # # #         return "Sorry, I couldn't understand that."
