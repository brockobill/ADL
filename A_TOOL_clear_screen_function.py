
def clear_screen():
    import os
    """
    This function clears the terminal screen before program starts.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()