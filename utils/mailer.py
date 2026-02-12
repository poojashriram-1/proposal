# import os
# import smtplib
# from email.mime.text import MIMEText
#
# def send_mail(receiver_email, link):
#
#     sender_email = os.getenv("EMAIL_USER")
#     app_password = os.getenv("EMAIL_PASS")
#
#     body = f"""
#     💖 You received a special proposal!
#
#     Click here to open:
#     {link}
#     """
#
#     msg = MIMEText(body)
#     msg["Subject"] = "Someone Sent You a Proposal 💕"
#     msg["From"] = sender_email
#     msg["To"] = receiver_email
#
#     try:
#         server = smtplib.SMTP("smtp.gmail.com", 587)
#         server.starttls()
#         server.login(sender_email, app_password)
#         server.send_message(msg)
#         server.quit()
#         print("✅ Email sent successfully")
#
#     except Exception as e:
#         print("❌ Email failed:", e)




import os
import resend

resend.api_key = os.getenv("RESEND_API_KEY")
print("key",os.getenv("RESEND_API_KEY"))


def send_mail(to_email, link):
    try:
        response = resend.Emails.send({
            "from": "onboarding@resend.dev",
            "to": to_email,
            "subject": "Your a Proposal link 💕",
            "html": f"""
                <h2>Payment Successful 🎉</h2>
                <p>Click below to view link:</p>
                <a href="{link}">Proposal link 💕</a>
            """
        })
        print("Email sent:", response)
    except Exception as e:
        print("Email failed:", e)
