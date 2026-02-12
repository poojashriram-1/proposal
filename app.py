import os

from flask import Flask, render_template, request, redirect
import razorpay
import uuid
from utils.mailer import send_mail
# from utils.sms import send_sms


app = Flask(__name__)

client = razorpay.Client(
    auth=(
            os.getenv("RAZORPAY_KEY_ID"),
            os.getenv("RAZORPAY_KEY_SECRET")
        )
)

DATA = {}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/create-order", methods=["POST"])
def create_order():
    order_id = str(uuid.uuid4())

    DATA[order_id] = request.form

    order = client.order.create({
        "amount": 4900,
        "currency": "INR",
        "payment_capture": 1
    })

    return render_template("payment.html",
                           order_id=order["id"],
                           key=os.getenv("RAZORPAY_KEY_ID"),
                           custom_id=order_id)


#
# @app.route("/success/<order_id>")
# def success(order_id):
#
#     # 1️⃣ Get stored form data
#     data = DATA.get(order_id)
#
#     if not data:
#         return "Invalid Order", 404
#
#     # 2️⃣ Generate unique valentine link
#     link = f"http://localhost:5000/valentine/{order_id}"
#
#     # 3️⃣ Send Email
#     send_mail(
#         receiver_email=data["email"],
#         lover_name=data["lover_name"],
#         message=data["message"],
#         link=link
#     )
#
#     # 4️⃣ Send SMS
#     send_sms(
#         phone=data["phone"],
#         link=link
#     )
#
#     # 5️⃣ Render success page
#     return render_template("success.html")

@app.route("/success/<order_id>")
def success(order_id):
    data = DATA.get(order_id)
    # print("key", os.getenv("RESEND_API_KEY"))
    if not data:
        # print("DATA currently:", DATA)
        return "Order not found or server restarted!", 404

    link = f"http://localhost:5000/valentine/{order_id}"

    # Send Email (simple)
    print("in sucess def")
    print("link", link)
    print("email:", data.get("email"))

    send_mail(data["email"], link)

    # Send SMS (Twilio optional)
    # send_sms(data["phone"], link)

    return render_template("success.html")


@app.route("/valentine/<order_id>")
def valentine(order_id):

    data = DATA.get(order_id)

    if not data:
        return "Invalid or Expired Link 💔", 404

    return render_template(
        "valentine.html",
        name=data["lover_name"],
        message=data["message"]
    )

@app.route("/final")
def final():
    return render_template("final.html")




#
# @app.route("/success/<order_id>")
# def success(order_id):
#
#     data = DATA.get(order_id)
#
#     if not data:
#         return "Invalid or Expired Order", 404

#
# def send_mail(email, link):
#     print("Email sent to:", email)
#     print("Link:", link)

def send_sms(phone, link):
    print("SMS sent to:", phone)
    print("Link:", link)





# if __name__ == "__main__":
#     app.run(debug=True)

if __name__ == "__main__":
    app.run()
