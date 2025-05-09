# SpoofMaster
SpoofMaster  is a professional email spoofing and logging tool designed for security professionals and penetration testers. It allows users to send spoofed emails using Gmail's SMTP server, with a colorful and user-friendly interface. For educational and testing purposes only. Always get permission before use.



# **SpoofMaster** - Advanced Professional Email Spoofing & Logging Tool ✨🚀

**SpoofMaster** is the **pinnacle of email spoofing and logging technology**. Designed for **penetration testers**, **ethical hackers**, and **security researchers**, this tool provides a **comprehensive solution** for conducting safe and educational **email spoofing attacks**. With a **sleek, modern, and intuitive UI**, SpoofMaster is more than just a tool—it's a complete, high-performance platform for understanding **email security vulnerabilities**.

Whether you're performing **pen testing**, **educational demonstrations**, or studying the **inner workings of email security**, **SpoofMaster** is your essential toolkit. With **next-level customization**, **advanced features**, and a focus on **user experience**, this tool guarantees that every test is as **efficient** and **secure** as possible.

> **"SpoofMaster: Empowering Ethical Hackers to Test, Learn, and Secure!"**



## 🎯 **Key Features**:

- **Advanced Email Spoofing**: Create and send fully customized spoofed emails with fake sender information. Perfect for **ethical hacking** and **security testing**.
  
- **Gmail SMTP Integration**: Use Gmail’s secure SMTP servers with **App Password** authentication, ensuring privacy and reliability in your spoofing operations.

- **Email Logging**: All spoofed emails are automatically logged, capturing critical details such as:
  - Sender & recipient
  - Email subject & body
  - Time sent & IP address of the sender
  - And more...

- **Colorful and Interactive UI**: A vibrant, **interactive terminal-based UI** that offers **dynamic feedback**, beautiful ASCII art, and clear step-by-step instructions for easy use.

- **Customizable Templates**: The tool allows you to create custom email templates with rich formatting, dynamic placeholders, and HTML support. This feature makes it **easy to design sophisticated emails** for your penetration tests.

- **Multi-Language Support**: SpoofMaster is fully **localized in Turkish** and **English**. Future versions will include additional language support.

- **Extensive Security Features**: The tool is **designed with security in mind**, ensuring **ethical use** and providing functionality to simulate realistic spoofing attacks.

- **Automated Email Testing**: SpoofMaster includes a built-in **email testing mechanism**, automatically checking for **deliverability**, **SMTP errors**, and **common vulnerabilities**.



## 🖥️ **System Requirements**:

### Hardware:
- **CPU**: Modern multi-core processor (Intel i3 or better recommended).
- **RAM**: Minimum of **2GB RAM**, but 4GB or more is recommended for optimal performance.
- **Disk Space**: At least **500MB** of free disk space.

### Software:
- **Operating System**: Linux (Ubuntu, Kali), macOS, Windows with WSL (Windows Subsystem for Linux), or Termux on Android.
- **Python**: Version **3.8 or higher** is required.

### Dependencies:
- **Python Packages**:
  - `colorama` - For colorful terminal output.
  - `pyfiglet` - For ASCII art rendering.
  - `smtplib` - For secure email sending via Gmail's SMTP.
  - `email` - For constructing email content (HTML and plain text).
  - `requests` - For handling HTTP requests (future versions may include web-based configurations).



## 🛠️ **Installation Guide**:

### Step 1: Clone the Repository
Begin by cloning the repository to your local machine:

```bash
git clone https://github.com/leronru/SpoofMaster.git
cd SpoofMaster
```
Step 2: Install Dependencies

Run the following command to install all necessary Python dependencies:
```bash
pip install -r requirements.txt
```
Step 3: Set Up Gmail SMTP Credentials

1. Enable Gmail 
2. 2-Step Verification:

Navigate to your Google Account.
https://myaccount.google.com/security

Enable 2-Step Verification for added security.



2. Generate an App Password:

Go to the App Passwords section.

Generate a new app password specifically for SpoofMaster (you will need this in the next step).



3. Save the App Password securely**. You will be prompted to enter it when sending emails through SpoofMaster.






📧 Using SpoofMaster:

Step 1: Launch SpoofMaster

After completing the installation, start SpoofMaster by running the following command:
```bash
python spoofmaster.py
```
Step 2: Enter Email Information

When prompted, provide the following information:

1. Fake Sender Email: The email address you want to spoof (e.g., fakeemail@example.com).


2. Recipient Email: The target email address (this is the email address you want to send the spoofed email to).


3. Email Subject: The subject line of the spoofed email.


4. Email Body: The body of the email. This can be plain text or HTML.



Step 3: Authentication

You will be prompted to enter your Gmail App Password for authentication. This allows SpoofMaster to securely send emails via Gmail’s SMTP server.

Step 4: Email Sending & Logging

After filling in the details, SpoofMaster will send the email. Every spoofed email sent will be logged into a text file called spoof_log.txt. You can view the logs by using the command:

cat spoof_log.txt

The logs will contain:

Sender Email

Recipient Email

Subject

Message Preview

Time Sent

Sender IP Address





🔒 Security and Legal Disclaimer:

Warning: This tool is intended for ethical hacking and educational purposes only. Unauthorized use of SpoofMaster is illegal and unethical.

Always obtain explicit permission from the target organization or individual before performing any penetration tests.

Ensure compliance with all applicable laws before using this tool. Misuse of this tool could lead to legal consequences.

Use responsibly: SpoofMaster is not intended for malicious use or illegal activities.


> "Ethical hackers use their skills for good, to improve security and protect users."






🛠️ Contributing:

SpoofMaster is an open-source project, and contributions are always welcome! If you would like to enhance the tool, contribute to the codebase, or suggest new features, follow these steps:

1. Fork this repository.


2. Clone your fork to your local machine.


3. Make changes (add features, fix bugs, improve documentation).


4. Push your changes and create a pull request.



Reporting Issues:

If you find any bugs or issues, please open a new issue on the GitHub Issues page. We welcome feedback and suggestions!





📄 License:

This project is licensed under the MIT License. See the LICENSE file for details.




📈 Roadmap:

v51: Support for additional email providers (Yahoo, Outlook, etc.).

v52: Web-based configuration and interactive GUI.

v53: Extended logging capabilities (including IP geolocation).

v54: Real-time email spoofing simulations and advanced SMTP testing.





🌐 GitHub Repository:

Check out the SpoofMaster GitHub repository for more details and updates:

Visit SpoofMaster on GitHub




📱 Contact & Support:

For further questions or support:

Report Issues: Open an issue on the GitHub Issues page.

Email: leronru33@gmail.com

GitHub: Follow @leronru for updates.

instagram:https://www.instagram.com/leronru?igsh=ZGZiNTNhcWlvMm9u


📜 Acknowledgments:

Python Community for their amazing support.

Gmail Developers for providing a reliable and secure email service.

Ethical Hacking Community for continually sharing knowledge and improving security.





🌟 Join the Ethical Hacking Movement! 🌟

Ethical hacking is about making the internet a safer place for everyone. Let’s work together to make the digital world more secure with tools like SpoofMaster.




💡 Credits:

Developer: leronru

Special Thanks: To the amazing ethical hacking community, contributors, and testers who’ve supported this project.

