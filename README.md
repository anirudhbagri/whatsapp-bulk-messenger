# Whatsapp-Bulk-Messenger

Whatsapp Bulk Messenger automates sending of messages via Whatsapp Web. The tool can you used to send whatsapp message in bulk. Program uses runs through a list of numbers provided in numbers.txt and then tries to send a prediefined (but templated) message to each number in the list. It can also read other columns from the number csv to populate template specific words and then send out a personalized message to the number

Note: The current program is limited to sending only TEXT messages


# Requirements

*  Python >= 3.6
*  Chrome headless is installed by the program automatically

# Setup

1. Install python - >=v3.6
2. Run "pip install -r requirements.txt"

# Steps
I have created a UI for this as well.
1. Run "Send Messages.bat" file
2. Enter your numbers in the first tab. Then click next.
3. Enter the message you want to send.
4. Click send messages button.
5. Once the program starts, you'll see the message in message.txt and count of numbers in the numbers.txt file.
6. After a while, Chrome should pop-up and open web.whatsapp.com.
7. Scan the QR code to login into whatsapp.
8. Press `Enter` to start sending out messages.
9. Sit back and relax!

