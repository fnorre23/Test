import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

# Function to manipulate the image (example implementation)
def getBinaryImage(image, gestureName):
    # Convert the image to binary
    grayImg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #_, image = cv2.threshold(grayImg, 127, 255, cv2.THRESH_BINARY)

    # Turning light pixels to white and dark pixels to black
    flattened_image = grayImg.flatten()
    for i in range(len(flattened_image)):
        if flattened_image[i] < 127:
            flattened_image[i] = 0
        else:
            flattened_image[i] = 255
    new_image = np.reshape(flattened_image, grayImg.shape)
    

    # Save the manipulated image
    cv2.imwrite(f'{gestureName}_binary.png', new_image)
    print(f"Manipulated image of {gestureName} saved")

    # Delete the original captured image
    try:
        os.remove('captured_image.png')
        print("Original image deleted.")
    except FileNotFoundError:
        print("Error: Original image file not found.")
    except Exception as e:
        print(f"Error deleting the image: {e}")
    return new_image

def displayText(image, text):
    # Display the text on the image in the top left corner
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(image, text, (10, 30), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    return image

def close_application():
    cap.release()
    cv2.destroyAllWindows()

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

    displayText(frame, 'Press "s" to save the image')

    # Wait for a key press (1 ms delay)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('s'):  # Press 's' to save the image
        cv2.imwrite('captured_image.png', frame)
        print("Image saved as 'captured_image.png'")

        # Manipulate the image
        getBinaryImage(frame, 'gesture1')

        cv2.destroyWindow('Video Feed 1')  # Close the video window
        break

    elif key == ord('q'):  # Press 'q' to quit
        # Release the camera and close windows
        close_application()
        break

# Take image for 2nd gesture
    ret, frame = cap.read()  # Read a frame from the video feed
    frame = cv2.flip(frame, 1)  # Flip the frame horizontally (mirror effect)

    if not ret:
        print("Error: Could not read frame.")
        break

    cv2.imshow('Video Feed 2', frame)  # Display the frame

    displayText(frame, 'Press "s" to save the image')

    # Wait for a key press (1 ms delay)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('s'):  # Press 's' to save the image
        cv2.imwrite('captured_image.png', frame)
        print("Image saved as 'captured_image.png'")

        # Manipulate the image
        getBinaryImage(frame, 'gesture2')

        cv2.destroyWindow('Video Feed 2')  # Close the video window
        break

    elif key == ord('q'):  # Press 'q' to quit
        # Release the camera and close windows
        close_application()
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

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        close_application()
        break


