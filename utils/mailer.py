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



#
# import os
# import resend
#
# resend.api_key = os.getenv("RESEND_API_KEY")
# print("key",os.getenv("RESEND_API_KEY"))
#
# def send_mail(to_email, link):
#     try:
#         response = resend.Emails.send({
#             "from": "onboarding@resend.dev",
#             "to": to_email,
#             "subject": "Your a Proposal link 💕",
#             "html": f"""
#                 <h2>Payment Successful 🎉</h2>
#                 <p>Click below to view link:</p>
#                 <a href="{link}">Proposal link 💕</a>
#             """
#         })
#
#         print("Sending email to:", to_email)
#         print("Using key:", resend.api_key)
#
#         print("Email sent:", response)
#     except Exception as e:
#         print("Email failed:", e)
#


import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint

import os

# configuration.api_key['api-key'] = os.getenv("BREVO_API_KEY")


def send_mail(to_email, link):
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = os.getenv("BREVO_API_KEY")
    # configuration.api_key['api-key'] = "YOUR_BREVO_API_KEY"

    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(
        sib_api_v3_sdk.ApiClient(configuration)
    )

    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
        to=[{"email": to_email}],
        sender={"email": "noreply@brevo.com"},  # default works
        subject="Your Download Link",
        html_content=f"""
        <h2>Thank You for Payment</h2>
        <p>Click below to download:</p>
        <a href="{link}">Download Now</a>
        """
    )

    try:
        api_instance.send_transac_email(send_smtp_email)
        print("Email sent successfully")
    except ApiException as e:
        print("Exception when sending email:", e)
