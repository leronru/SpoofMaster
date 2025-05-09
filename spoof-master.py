import smtplib
from email.message import EmailMessage
import os
import time
from colorama import Fore, Style, init
import pyfiglet

init(autoreset=True)

# Clear terminal
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Banner
def banner():
    clear()
    print(Fore.CYAN + pyfiglet.figlet_format("SpoofMaster", font="slant"))
    print(Fore.YELLOW + "Professional Email Spoofing & Logging Tool")
    print(Fore.MAGENTA + "GitHub: https://github.com/leronru/SpoofMaster")
    print(Fore.GREEN + "-" * 60)

# Input email spoof details
def input_details():
    print(Fore.LIGHTMAGENTA_EX + "\nEnter the spoofed email information:\n")
    name = input(Fore.BLUE + "Sender Name: ")
    fake_email = input(Fore.BLUE + "Fake Sender Email: ")
    recipient = input(Fore.BLUE + "Recipient Email: ")
    subject = input(Fore.GREEN + "Subject: ")
    content = input(Fore.GREEN + "Message Content: ")
    return name, fake_email, recipient, subject, content

# SMTP login info
def smtp_credentials():
    print(Fore.RED + "\nEnter your real Gmail credentials:")
    real_email = input(Fore.YELLOW + "Your Gmail Address: ")
    password = input(Fore.YELLOW + "App Password (from Google): ")
    return real_email, password

# Send email
def send_email(name, fake_email, recipient, subject, content, real_email, password):
    msg = EmailMessage()
    msg['From'] = f"{name} <{fake_email}>"
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.set_content(content)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(real_email, password)
            smtp.send_message(msg)
            print(Fore.GREEN + "\n[✔] Email successfully sent!")
            with open("spoof_log.txt", "a") as log:
                log.write(f"To: {recipient}, From: {fake_email}, Subject: {subject}\n")
    except smtplib.SMTPAuthenticationError:
        print(Fore.RED + "\n[!] Authentication Error! Check your Gmail credentials.")
    except Exception as e:
        print(Fore.RED + "\n[!] Failed to send email:", e)

# View logs
def view_logs():
    clear()
    print(Fore.YELLOW + "[!] Email Send Logs:\n")
    if os.path.exists("spoof_log.txt"):
        with open("spoof_log.txt", "r") as f:
            print(Fore.WHITE + f.read())
    else:
        print(Fore.RED + "No logs found.")
    input(Fore.CYAN + "\nPress Enter to return to the main menu...")

# Main menu
def main_menu():
    while True:
        banner()
        print(Fore.LIGHTBLUE_EX + "1. Send Spoofed Email")
        print(Fore.LIGHTCYAN_EX + "2. View Logs")
        print(Fore.RED + "3. Exit\n")
        choice = input(Fore.YELLOW + "Select an option (1-3): ")

        if choice == "1":
            name, fake_email, recipient, subject, content = input_details()
            real_email, password = smtp_credentials()
            send_email(name, fake_email, recipient, subject, content, real_email, password)
            input(Fore.CYAN + "\nPress Enter to return to main menu...")
        elif choice == "2":
            view_logs()
        elif choice == "3":
            print(Fore.LIGHTGREEN_EX + "Goodbye!")
            break
        else:
            print(Fore.RED + "Invalid choice! Please select between 1-3.")
            time.sleep(1)

# Run
main_menu()
