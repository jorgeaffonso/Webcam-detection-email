import smtplib
from email.message import EmailMessage
import imghdr

PASSWORD = "cvkkstapumgxslrq"
SENDER = "jorgemail.affonso@gmail.com"
RECEIVER = "jorgemail.affonso@gmail.com"
def send_email(image_path):
    email_message = EmailMessage()   # Act as a dictionary
    email_message["Subject"] = "New costumer showed up!"
    email_message.set_content("Hey, we just saw a new costumer")

    with open(image_path,"rb") as file:
        content = file.read()

    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()


if __name__ == "__main__":
    send_email(image_path="images/cat.png")

