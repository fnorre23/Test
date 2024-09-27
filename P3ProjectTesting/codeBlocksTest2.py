import cv2
import tkinter as tk
from threading import Thread

# Initialize video capture
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Flag to track if the video should be in grayscale mode
is_grayscale = False

def switch_to_grayscale():
    global is_grayscale
    is_grayscale = True
    print("Grayscale mode activated.")

def close_application():
    global running
    running = False

# Create a Tkinter window
root = tk.Tk()
root.title("Video Control")

# Create a button to switch to grayscale
button_grayscale = tk.Button(root, text="Switch to Grayscale", command=switch_to_grayscale)
button_grayscale.pack(pady=20)

# Create a button to quit the application
button_quit = tk.Button(root, text="Quit", command=close_application)
button_quit.pack(pady=20)

# Run the Tkinter window in a separate thread
def run_tkinter():
    root.mainloop()

# Start the Tkinter GUI in a separate thread
Thread(target=run_tkinter, daemon=True).start()

# Main loop to display the video feed
running = True
try:
    while running:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame.")
            break

        # If the flag is set, convert the frame to grayscale
        if is_grayscale:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the frame in a window
        cv2.imshow('Video Feed', frame)

        # Check for key press events
        key = cv2.waitKey(1) & 0xFF

        # If 'q' is pressed, exit the program entirely
        if key == ord('q'):
            print("Exiting video feed...")
            break

finally:
    # Release the video capture object and close any OpenCV windows
    cap.release()
    cv2.destroyAllWindows()
