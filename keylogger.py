from pynput import keyboard

def on_press(key):
    try:
        print(f'Key pressed: {key.char}')
    except AttributeError:
        # we need to change these special keys to characters that we can understand
        print(f'Special key {key} was used')

def on_release(key):
    print(f'{key} was released')
    if key == keyboard.Key.esc:
        #Stop the listener
        return False

# we will keep the listener running until we press the Esc key
with keyboard.Listener(on_press=on_press, on_release=on_release) as l:
    l.join()


if __name__ == "__main__":
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)

    listener.start()


