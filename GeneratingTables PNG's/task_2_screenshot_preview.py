import os
import pyautogui
import time
import pygetwindow as gw
from pygetwindow import getWindowsWithTitle

# Base directory to save screenshots
base_dir = "C:/Users/danig/OneDrive/Desktop/Tables/Table_PNG"
file_name = "C:/Users/danig/OneDrive/Desktop/Tables/all_table.pptm"


# Function to take and save a screenshot of a specific window
def screenshot_window(title, save_path):
    window = getWindowsWithTitle(title)[0]  # Find the window with the specific title
    if window:
        window.activate()  # Focus on the window to bring it to the front
        time.sleep(1)  # Wait a bit for the window to fully activate
        screenshot = pyautogui.screenshot(region=(window.left, window.top, window.width, window.height))
        print("snapshot taken")
        time.sleep(1)  # Wait a bit for the window to fully activate
        screenshot.save(save_path)
        return True
    else:
        print(f"No window with title '{title}' found.")
        return False




def main():
    # Define the base structure for the filenames
    base_name = "T2_DS{}_{}_{}{}.png"

    # Define the groups and their respective labels and counts
    groups = [
        ("anime", "color", 4),
        ("cereal", "zebra", 4),
        ("candy", "plain", 4),
        ("movie", "bar", 4)
    ]

    # List all window titles
    for w in gw.getAllWindows():
        print(w.title)

    # Initialize the sequence number
    sequence_number = 1

    # Loop through each group to generate filenames
    for group in groups:
        category, label, count = group
        for i in range(1, count + 1):
            # Generate filename
            file_name = base_name.format(sequence_number, category, label, i)

            save_path = os.path.join(base_dir, file_name)

            # Taking screenshot
            if not screenshot_window("PowerPoint", save_path):
                print(f"Failed to capture slide for {file_name}")

            print(file_name)

            # Simulate key press to move to the next slide
            pyautogui.press('right')
            time.sleep(2)  # Wait a bit to ensure the slide has changed

            # Increment the sequence number for the next file
            sequence_number += 1

    print("Done taking screenshots.")

if __name__ == "__main__":
    main()