from ctypes import windll, create_unicode_buffer


def active_foreground():
    window_unicode = windll.user32.GetForegroundWindow()
    active_foreground_window_title = create_unicode_buffer(window_unicode)
    windll.user32.GetWindowTextW(window_unicode, active_foreground_window_title)

    if active_foreground_window_title.value:
        return active_foreground_window_title.value
    return None
