import pyautogui
import time
import threading

# Lock to ensure messages are sent one at a time if timers collide
message_lock = threading.Lock()


# Function to type and send a message in Discord
def send_message(message):
    with message_lock:  # Ensure one message is sent at a time
        pyautogui.typewrite(message)
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.press('enter')


# Function to handle the message sending intervals
def send_work_message():
    while True:
        send_message("/work")
        time.sleep(600)  # Wait 10 minutes (600 seconds)


def send_tips_message():
    while True:
        send_message("/tips")
        time.sleep(300)  # Wait 5 minutes (300 seconds)


def send_overtime_message():
    while True:
        send_message("/overtime")
        time.sleep(1800)  # Wait 30 minutes (1800 seconds)


# Function to start the threads for all messages
def start_sending_messages():
    # Start each message sending in separate threads
    threading.Thread(target=send_work_message, daemon=True).start()
    time.sleep(5)
    threading.Thread(target=send_tips_message, daemon=True).start()
    time.sleep(5)
    threading.Thread(target=send_overtime_message, daemon=True).start()
    time.sleep(5)


# Test script: Immediately start the message sending
if __name__ == "__main__":
    print("Starting script...")
    time.sleep(5)  # Wait a bit to focus Discord before the script starts
    start_sending_messages()

    # Keep the script running so threads can keep sending messages
    while True:
        time.sleep(1)
