import platform

def play_alarm():
    """Cross-platform alarm system."""
    if platform.system() == "Windows":
        import winsound
        winsound.Beep(2500, 1000) # Beep for 1 second
    else:
        # Mac/Linux fallback (system bell)
        print('\a')
