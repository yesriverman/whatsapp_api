import os
import requests

HF_API_KEY = os.getenv("HF_API_KEY")
HF_MODEL = "tiiuae/falcon-7b-instruct"

def get_hf_response(prompt: str) -> str:
    if not HF_API_KEY:
        print("HF API key not set!")
        return "Sorry, I couldn't understand that."

    headers = {"Authorization": f"Bearer {HF_API_KEY}"}
    payload = {
        "model": HF_MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "max_new_tokens": 256
    }

    try:
        response = requests.post(
            "https://router.huggingface.co/api/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=20
        )
        result = response.json()
        if "error" in result:
            print("Hugging Face API error:", result["error"])
            return "Sorry, I couldn't understand that."
        return result["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print("Hugging Face API exception:", e)
        return "Sorry, I couldn't understand that."






# import os
# import requests

# HF_API_KEY = os.getenv("HF_API_KEY")
# HF_MODEL = "tiiuae/falcon-7b-instruct"  # instruction-tuned model

# def get_hf_response(prompt: str) -> str:
#     if not HF_API_KEY:
#         print("HF API key not set!")
#         return "Sorry, I couldn't understand that."

#     headers = {"Authorization": f"Bearer {HF_API_KEY}"}
#     payload = {"inputs": prompt}

#     try:
#         response = requests.post(
#             f"https://router.huggingface.co/api/v1/chat/completions",
#             headers={"Authorization": f"Bearer {HF_API_KEY}"},
#             json={
#                 "model": HF_MODEL,
#                 "messages": [{"role": "user", "content": prompt}],
#                 "max_new_tokens": 256
#             },
#             timeout=20
#         )

#         result = response.json()
#         if "error" in result:
#             print("Hugging Face API error:", result["error"])
#             return "Sorry, I couldn't understand that."
#         # return the generated text
#         return result[0]["generated_text"].strip()
#     except Exception as e:
#         print("Hugging Face API exception:", e)
#         return "Sorry, I couldn't understand that."
