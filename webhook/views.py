import json
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .utils import send_whatsapp_message

VERIFY_TOKEN = "my_verify_token_123"

KEYWORD_RESPONSES = {
    "hello": "Hello! How can I help you today?",
    "hi": "Hi there! How can I assist?",
    "price": "Our prices start at $10.",
    "cost": "Our prices start at $10.",
    "hours": "We are open from 9am to 6pm.",
    "time": "We are open from 9am to 6pm."
}

@csrf_exempt
def whatsapp_webhook(request):
    if request.method == "POST":
        try:
            payload = json.loads(request.body.decode("utf-8"))
            print("Incoming WhatsApp message:", json.dumps(payload, indent=2))

            for entry in payload.get("entry", []):
                for change in entry.get("changes", []):
                    value = change.get("value", {})
                    messages = value.get("messages", [])

                    for msg in messages:
                        sender = msg.get("from")
                        text = msg.get("text", {}).get("body", "").lower()
                        msg_type = msg.get("type", "")

                        if sender and text and msg_type == "text":
                            # Keyword-based reply
                            reply_text = None
                            for keyword, response in KEYWORD_RESPONSES.items():
                                if keyword in text:
                                    reply_text = response
                                    break

                            # Default fallback (OpenAI)
                            if not reply_text:
                                from .openai_utils import get_openai_response
                                reply_text = get_openai_response(text)

                            response = send_whatsapp_message(sender, reply_text)
                            print(f"Reply sent to {sender}: {reply_text}")
                            print("API response:", response)

        except Exception as e:
            print("Error processing incoming message:", e)

        return JsonResponse({"status": "ok"})



# @csrf_exempt
# def whatsapp_webhook(request):
#     # GET verification
#     if request.method == "GET":
#         mode = request.GET.get("hub.mode")
#         token = request.GET.get("hub.verify_token")
#         challenge = request.GET.get("hub.challenge")

#         if mode == "subscribe" and token == VERIFY_TOKEN:
#             return HttpResponse(challenge)
#         return HttpResponse("Verification failed", status=403)

#     # POST messages
#     if request.method == "POST":
#         try:
#             payload = json.loads(request.body.decode("utf-8"))
#             print("Incoming WhatsApp message:", json.dumps(payload, indent=2))

#             # Loop through all messages
#             for entry in payload.get("entry", []):
#                 for change in entry.get("changes", []):
#                     value = change.get("value", {})
#                     messages = value.get("messages", [])

#                     for msg in messages:
#                         sender = msg.get("from")       # <-- THIS MUST BE msg["from"]
#                         text = msg.get("text", {}).get("body", "")
#                         msg_type = msg.get("type", "")

#                         # Only respond to text messages
#                         if sender and text and msg_type == "text":
#                             print(f"Sending reply to {sender}: Echo: {text}")
#                             response = send_whatsapp_message(sender, f"Echo: {text}")
#                             print("API response:", response)

#         except Exception as e:
#             print("Error processing incoming message:", e)

#         return JsonResponse({"status": "ok"})

#     return HttpResponse(status=405)

































# import json
# from django.http import JsonResponse, HttpResponse
# from django.views.decorators.csrf import csrf_exempt
# from .utils import send_whatsapp_message

# VERIFY_TOKEN = "my_verify_token_123"

# @csrf_exempt
# def whatsapp_webhook(request):
#     # 🔹 Verification (GET)
#     if request.method == "GET":
#         mode = request.GET.get("hub.mode")
#         token = request.GET.get("hub.verify_token")
#         challenge = request.GET.get("hub.challenge")

#         if mode == "subscribe" and token == VERIFY_TOKEN:
#             return HttpResponse(challenge)
#         return HttpResponse("Verification failed", status=403)

#     # 🔹 Incoming messages (POST)
#     if request.method == "POST":
#         try:
#             payload = json.loads(request.body.decode("utf-8"))
#             print("Incoming WhatsApp message:", json.dumps(payload, indent=2))

#             for entry in payload.get("entry", []):
#                 for change in entry.get("changes", []):
#                     value = change.get("value", {})
#                     messages = value.get("messages", [])
#                     contacts = value.get("contacts", [])

#                     for msg in messages:
#                         sender = msg.get("from")  # WhatsApp sender number
#                         text = msg.get("text", {}).get("body", "")

#                         if sender and text:
#                             reply_text = f"Echo: {text}"
#                             response = send_whatsapp_message(sender, reply_text)
#                             print("Reply sent. API response:", response)


#         except Exception as e:
#             print("Error processing incoming message:", e)

#         return JsonResponse({"status": "ok"})

#     return HttpResponse(status=405)




# from django.shortcuts import render

# # Create your views here.
# import json
# from django.http import JsonResponse, HttpResponse
# from django.views.decorators.csrf import csrf_exempt
# from .utils import send_whatsapp_message

# VERIFY_TOKEN = "my_verify_token_123"  # change later

# @csrf_exempt
# def whatsapp_webhook(request):
#     # 🔹 Verification (GET)
#     if request.method == "GET":
#         mode = request.GET.get("hub.mode")
#         token = request.GET.get("hub.verify_token")
#         challenge = request.GET.get("hub.challenge")

#         if mode == "subscribe" and token == VERIFY_TOKEN:
#             return HttpResponse(challenge)
#         return HttpResponse("Verification failed", status=403)



#     if request.method == "POST":
#         payload = json.loads(request.body.decode("utf-8"))
#         print("Incoming WhatsApp message:", json.dumps(payload, indent=2))

#         # Auto-reply example
#         try:
#             contacts = payload.get("entry", [])[0]["changes"][0]["value"]["contacts"]
#             msgs = payload.get("entry", [])[0]["changes"][0]["value"]["messages"]
#             for contact, msg in zip(contacts, msgs):
#                 sender = contact["wa_id"]
#                 text = msg.get("text", {}).get("body", "")
#                 # simple auto-reply
#                 send_whatsapp_message(sender, f"Echo: {text}")
#         except Exception as e:
#             print("Error processing message:", e)

#         return JsonResponse({"status": "ok"})

#     # # 🔹 Incoming messages (POST)
#     # if request.method == "POST":
#     #     payload = json.loads(request.body.decode("utf-8"))
#     #     print("Incoming WhatsApp message:", json.dumps(payload, indent=2))
#     #     return JsonResponse({"status": "ok"})

#     # return HttpResponse(status=405)


