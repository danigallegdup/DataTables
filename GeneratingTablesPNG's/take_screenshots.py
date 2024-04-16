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

# Naming and category details
categories = ['anime', 'cereal', 'candy', 'movie']
styles = ['color', 'zebra', 'plain', 'bar']
slides_per_category_style = 4




# List all window titles
for w in gw.getAllWindows():
    print(w.title)


dataset_number= 1
rep_of_DS =1
rep_of_cat = 1

# Main loop to take screenshots
for i, category in enumerate(categories, start=1):
    for j, style in enumerate(styles, start=1):
        for k in range(1, slides_per_category_style + 1):
            # Constructing filename
            file_name = f"DS{(dataset_number)}_{category}_{styles[k-1]}{rep_of_cat}.png"
            
            rep_of_DS += 1

            if rep_of_DS == 5:
                dataset_number += 1
                rep_of_cat += 1
                rep_of_DS = 1
                if rep_of_cat == 5:
                    rep_of_cat = 1
            if dataset_number ==17:
                dataset_number = 1

            save_path = os.path.join(base_dir, file_name )

            # Taking screenshot
            if not screenshot_window("PowerPoint", save_path):
                print(f"Failed to capture slide for {file_name}")

            print(file_name)
            # Simulate key press to move to the next slide
            pyautogui.press('right')
            time.sleep(2)  # Wait a bit to ensure the slide has changed

print("Done taking screenshots.")
