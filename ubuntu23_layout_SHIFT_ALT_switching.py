from pynput import keyboard
import pyautogui

pressed_keys = set()
SHIFT_VCODE = 65505
ALT_VCODE = 65513
ALT_sh_VCODE = 65511
combos = ({SHIFT_VCODE, ALT_VCODE}, {SHIFT_VCODE, ALT_sh_VCODE})
alt_vk_codes= (ALT_VCODE, ALT_sh_VCODE)

#COMBO = {keyboard.Key.shift, keyboard.Key.alt_l}  # alt_l is left Alt, can also use Key.alt_r

#65513 alt, 65505 shift, 65511 - SHIFTED_ALt


def on_press(key):
    key_vk = None
    if key.__dict__.get("vk"):
        key_vk = key.__dict__.get("vk")
        if key_vk == 65511:
            pressed_keys.add(65511)
            print("sh_ALT pressed")
    elif key.__dict__.get("_value_"):
        key_vk = key.__dict__.get("_value_").vk
        if key_vk == SHIFT_VCODE:
            pressed_keys.add(key_vk)
            print("SHIFT pressed")
        elif key_vk == ALT_VCODE:
            pressed_keys.add(key_vk)
            print("ALT pressed")

    print(f"{pressed_keys=}")
    if pressed_keys in combos:
        print("KOMBO 1!")
        pyautogui.hotkey('winleft', 'space')


def on_release(key):
    key_vk = None
    if key.__dict__.get("vk"):
        key_vk = key.__dict__.get("vk")
    elif key.__dict__.get("_value_"):
        key_vk = key.__dict__.get("_value_").vk
    else:
        print("ELSE block")
    print(f"{key_vk=}")
    if key_vk and key_vk in alt_vk_codes:
        if ALT_VCODE in pressed_keys:
            pressed_keys.remove(ALT_VCODE)
        if ALT_sh_VCODE in pressed_keys:
            pressed_keys.remove(ALT_sh_VCODE)
    if key_vk == SHIFT_VCODE:
        if key_vk in pressed_keys:
            pressed_keys.remove(SHIFT_VCODE)

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
