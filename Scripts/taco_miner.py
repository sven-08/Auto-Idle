import pyautogui
import time
import threading
import pyperclip
import keyboard
import queue

# Queue to store commands in order
command_queue = queue.Queue()


# Worker function that processes the command queue
def process_commands():
    while True:
        command = command_queue.get()  # Get the next command from the queue
        if command is None:
            break  # Exit if None is received (not needed here)
        send_command(command)
        time.sleep(5)  # Ensure 5s delay before processing the next command


# Start the worker thread
worker_thread = threading.Thread(target=process_commands, daemon=True)
worker_thread.start()


# Function to type and send a message in Discord using copy-paste
def send_command(command):
    pyperclip.copy(command)
    keyboard.press_and_release('ctrl+v')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')


# Function to schedule commands at specific intervals
def schedule_command(command, interval):
    while True:
        command_queue.put(command)  # Add command to the queue
        time.sleep(interval)


# Commands for Idle Tacos
def start_tacos():
    threading.Thread(target=schedule_command, args=("/work", 600), daemon=True).start()  # Every 10 mins
    threading.Thread(target=schedule_command, args=("/tips", 300), daemon=True).start()  # Every 5 mins
    threading.Thread(target=schedule_command, args=("/overtime", 1800), daemon=True).start()  # Every 30 mins


# Commands for Idle Miner
def start_miner():
    threading.Thread(target=schedule_command, args=("/hunt", 300), daemon=True).start()  # Every 5 mins
    threading.Thread(target=schedule_command, args=("/fish", 300), daemon=True).start()  # Every 5 mins
    threading.Thread(target=schedule_command, args=("/sell", 20), daemon=True).start()  # Every 20 sec
    threading.Thread(target=schedule_command, args=("/upgrade item: pickaxe amount: all", 22), daemon=True).start()
    threading.Thread(target=schedule_command, args=("/upgrade item: backpack amount: all", 22), daemon=True).start()
    threading.Thread(target=schedule_command, args=("/harvest area: all", 1161), daemon=True).start()  # Every ~19.35 mins
    threading.Thread(target=schedule_command, args=("/plant area: all crop: pu", 1161), daemon=True).start()  # Every ~19.35 mins
    threading.Thread(target=schedule_command, args=("/claimall", 600), daemon=True).start()  # Every 10 mins
    threading.Thread(target=schedule_command, args=("/rebirth", 600), daemon=True).start()  # Every 10 mins


# Function to start all commands
def start_commands():
    start_tacos()
    start_miner()


# Start the script
if __name__ == "__main__":
    print("Starting script...")
    time.sleep(5)  # Wait before starting
    start_commands()

    # Keep the script running
    while True:
        time.sleep(1)
