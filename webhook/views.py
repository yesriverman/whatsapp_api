import json
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .utils import send_whatsapp_message

VERIFY_TOKEN = "my_verify_token_123"

@csrf_exempt
def whatsapp_webhook(request):
    # 🔹 Verification (GET)
    if request.method == "GET":
        mode = request.GET.get("hub.mode")
        token = request.GET.get("hub.verify_token")
        challenge = request.GET.get("hub.challenge")

        if mode == "subscribe" and token == VERIFY_TOKEN:
            return HttpResponse(challenge)
        return HttpResponse("Verification failed", status=403)

    # 🔹 Incoming messages (POST)
    if request.method == "POST":
        try:
            payload = json.loads(request.body.decode("utf-8"))
            print("Incoming WhatsApp message:", json.dumps(payload, indent=2))

            # Extract messages
            entries = payload.get("entry", [])
            for entry in entries:
                changes = entry.get("changes", [])
                for change in changes:
                    value = change.get("value", {})
                    contacts = value.get("contacts", [])
                    messages = value.get("messages", [])

                    for contact, msg in zip(contacts, messages):
                        sender = contact.get("wa_id")
                        text = msg.get("text", {}).get("body", "")

                        if sender and text:
                            reply_text = f"Echo: {text}"  # You can customize this
                            response = send_whatsapp_message(sender, reply_text)
                            print("Reply API response:", response)

        except Exception as e:
            print("Error processing incoming message:", e)

        return JsonResponse({"status": "ok"})

    return HttpResponse(status=405)




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


