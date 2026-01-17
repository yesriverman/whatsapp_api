from django.shortcuts import render

# Create your views here.
import json
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

VERIFY_TOKEN = "my_verify_token_123"  # change later

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
        payload = json.loads(request.body.decode("utf-8"))
        print("Incoming WhatsApp message:", json.dumps(payload, indent=2))
        return JsonResponse({"status": "ok"})

    return HttpResponse(status=405)


