import pyautogui
import webbrowser
import time

def read_urls(file_path):
    """Read URLs from a file and return them as a list."""
    with open(file_path, 'r') as file:
        return [line.strip() for line in file if line.strip()]

def open_urls_and_click(urls, load_delay, move_duration):
    """Open each URL in a new tab and simulate a click on the first article."""
    for url in urls:
        webbrowser.open_new_tab(url)
        time.sleep(load_delay)  # Wait for the page to load

        screenWidth, screenHeight = pyautogui.size()
        x_position = screenWidth / 2
        y_position = screenHeight / 4

        pyautogui.moveTo(x_position, y_position, duration=move_duration)
        pyautogui.click()

# Configuration settings
file_path = 'urls.txt'  # Specify the path to the file containing URLs
load_delay = 10  # Time in seconds to wait before moving the mouse
move_duration = 1  # Duration of the mouse movement in seconds

# Main execution
urls = read_urls(file_path)
open_urls_and_click(urls, load_delay, move_duration)
