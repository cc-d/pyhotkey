import json
import time
from pynput import keyboard

# Load the combos from combos.json
with open('combos.json') as combos_file:
    combos = json.load(combos_file)

# Global variables to track the state
combo_keys = set()
listening = False

def on_key_press(key):
    global listening

    if key == keyboard.Key.esc:
        print("Stopping listener.")
        listening = False

    # Add pressed key to the combo_keys set
    combo_keys.add(key)

    # Check if the left control key and 'k' key are pressed simultaneously
    if all(k in combo_keys for k in [keyboard.Key.ctrl_l, keyboard.KeyCode.from_char('k')]):
        print("Starting listener.")
        combo_keys.clear()  # Clear the combo keys
        listening = True

def on_key_release(key):
    if key in combo_keys:
        combo_keys.remove(key)

def type_text(text):
    with keyboard.Controller() as controller:
        for char in text:
            controller.press(char)
            controller.release(char)
            time.sleep(0.02)

def main():
    global listening

    listener = keyboard.Listener(
        on_press=on_key_press,
        on_release=on_key_release
    )
    listener.start()

    print("Press 'ctrl+k' to start listening.")
    try:
        while True:
            if listening:
                input_key = input("Enter a combo key: ")

                if input_key == 'esc':
                    print("Stopping listener.")
                    listening = False
                    continue

                if input_key.lower() in combos:
                    print(f"Key found: {input_key}")
                    value = combos[input_key.lower()]
                    type_text(value)
                else:
                    print("Key not found in combos.json")
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()

