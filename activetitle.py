"""
Функции получают название активного окна. Используются как заглушки.
Вместо них будем использовать расширение, для получения URL из браузера.
"""

import subprocess
import re


# for Linux
# https://stackoverflow.com/a/42404044
def get_active_foreground_title():
    root = subprocess.Popen(['xprop', '-root', '_NET_ACTIVE_WINDOW'], stdout=subprocess.PIPE)
    stdout, stderr = root.communicate()

    m = re.search(br'^_NET_ACTIVE_WINDOW.* ([\w]+)$', stdout)
    if m is not None:
        window_id = m.group(1)
        window = subprocess.Popen(['xprop', '-id', window_id, 'WM_NAME'],
                                  stdout=subprocess.PIPE)
        stdout, stderr = window.communicate()
    else:
        return None

    match = re.match(br"WM_NAME\(\w+\) = (?P<name>.+)$", stdout)
    if match is not None:
        return match.group("name").strip(b'"')
    return None

# from ctypes import windll, create_unicode_buffer


# for Windows
# def get_active_foreground_title():
#     window_unicode = windll.user32.GetForegroundWindow()
#     active_foreground_window_title = create_unicode_buffer(window_unicode)
#     windll.user32.GetWindowTextW(window_unicode, active_foreground_window_title)
#
#     if active_foreground_window_title.value:
#         return active_foreground_window_title.value
#     return None
