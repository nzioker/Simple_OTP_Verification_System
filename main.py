import random
import smtplib
import os

EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")

# generate random number
def get_email():
    email = input("Enter your email.")
    print("Check your email for the OTP code")
    return email

def random_number():
    number = random.randint(0, 999999)
    return number

# send the random number to an email


def send_email():
    r_number = random_number()
    user_email = get_email()
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=EMAIL,
                         password=PASSWORD,)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs=user_email,
                            msg=f"Your OTP code is {r_number}. Do not share this with anyone. ")

        otp = int(input("Enter the OTP code sent to your email"))

        if otp == r_number:
            logged_in()
        else:
            print("Check your OTP again")


def logged_in():
    print("You've been logged in")

send_email()
