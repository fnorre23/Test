import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

# Function to manipulate the image (example implementation)
def manipulate_image(image):
    # Example manipulation: convert to grayscale
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Open the camera
cap = cv2.VideoCapture(0)

# Take image for 1st gesture
while True:
    ret, frame = cap.read()  # Read a frame from the video feed
    frame = cv2.flip(frame, 1)  # Flip the frame horizontally (mirror effect)

    if not ret:
        print("Error: Could not read frame.")
        break

    cv2.imshow('Video Feed 1', frame)  # Display the frame

    # Wait for a key press (1 ms delay)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('s'):  # Press 's' to save the image
        cv2.imwrite('captured_image.png', frame)
        print("Image saved as 'captured_image.png'")

        # Manipulate the image
        manipulated_image = manipulate_image(frame)
        
        # Save the manipulated image
        cv2.imwrite('manipulated_image1.png', manipulated_image)
        print("Manipulated image saved as 'manipulated_image1.png'")

        # Delete the original captured image
        try:
            os.remove('captured_image.png')
            print("Original image deleted.")
        except FileNotFoundError:
            print("Error: Original image file not found.")
        except Exception as e:
            print(f"Error deleting the image: {e}")

        cv2.destroyWindow('Video Feed 1')  # Close the video window
        break

    elif key == ord('q'):  # Press 'q' to quit
        # Release the camera and close windows
        cap.release()
        cv2.destroyAllWindows()
        break

# Take image for 2nd gesture
while True:
    ret, frame = cap.read()  # Read a frame from the video feed
    frame = cv2.flip(frame, 1)  # Flip the frame horizontally (mirror effect)

    if not ret:
        print("Error: Could not read frame.")
        break

    cv2.imshow('Video Feed 2', frame)  # Display the frame

    # Wait for a key press (1 ms delay)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('s'):  # Press 's' to save the image
        cv2.imwrite('captured_image.png', frame)
        print("Image saved as 'captured_image.png'")

        # Manipulate the image
        manipulated_image = manipulate_image(frame)
        
        # Save the manipulated image
        cv2.imwrite('manipulated_image2.png', manipulated_image)
        print("Manipulated image saved as 'manipulated_image2.png'")

        # Delete the original captured image
        try:
            os.remove('captured_image.png')
            print("Original image deleted.")
        except FileNotFoundError:
            print("Error: Original image file not found.")
        except Exception as e:
            print(f"Error deleting the image: {e}")
        
        cv2.destroyWindow('Video Feed 2')  # Close the video window
        break

    elif key == ord('q'):  # Press 'q' to quit
        # Release the camera and close windows
        cap.release()
        cv2.destroyAllWindows()
        break


        

# Begin the main loop
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)  # Flip the frame horizontally (mirror effect)
    
    if not ret:
        break

    # Display the frame
    cv2.imshow('Third Code Block', frame)

    # Load the manipulated image
    manipulated_image2 = cv2.imread('manipulated_image2.png')

    # Display the manipulated image
    cv2.imshow('Manipulated Image 2', manipulated_image2)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close windows
cap.release()
cv2.destroyAllWindows()

