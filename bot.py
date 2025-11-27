import imaplib
import email
import time
from telebot import TeleBot

BOT_TOKEN = "8304198199:AAGrKy7jeKnP3hWCHPxWCx5nuNO9m0IwXMs"

GMAIL_USER = "kawaifelix1@gmail.com"
GMAIL_PASS = "ngiq gpvr gytf fswo"

bot = TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Bot OTP Gmail berhasil aktif 🔥\nKode OTP akan dikirim otomatis ke sini.")

def check_mail():
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(GMAIL_USER, GMAIL_PASS)
    mail.select("inbox")

    result, data = mail.search(None, "UNSEEN")
    mail_ids = data[0].split()

    for x in mail_ids:
        status, msg_data = mail.fetch(x, "(RFC822)")
        for response in msg_data:
            if isinstance(response, tuple):
                msg = email.message_from_bytes(response[1])
                subject = msg["subject"]

                bot.send_message(YOUR_CHAT_ID, f"Kode OTP masuk 📩\nSubject: {subject}")

while True:
    check_mail()
    time.sleep(5)
