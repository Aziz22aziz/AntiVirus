import requests
import sys
import os

# ====== الإعدادات ======
TOKEN   = "8247348420:AAFPcSIhXvPEjvMgtHLF0OtF4mh6cZJ8a_4"
CHAT_ID = "7454474616"
MESSAGE = "أهلاً بك 👋"
# =======================

def send_message():
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": MESSAGE}
    try:
        requests.post(url, data=data, timeout=10)
    except Exception:
        pass

if __name__ == "__main__":
    send_message()

    # إخفاء النافذة تماماً عند التشغيل كـ EXE (بدون console)
    if getattr(sys, "frozen", False):
        sys.exit(0)