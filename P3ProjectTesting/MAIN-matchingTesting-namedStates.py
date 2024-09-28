import cv2
import numpy as np
import os

# Array to store filenames of the pictures taken
filenames = []

white_threshold = 50

# Function to manipulate the image (example implementation)
def getBinaryImage(frame, gestureName):
    # Save the image
    cv2.imwrite('captured_image.png', frame)
    print("Image saved as 'captured_image.png'")
    image = cv2.imread('captured_image.png')

    # Convert the image to grayscale, for easier manipulation
    grayImg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Converting the image to binary - aka turning light pixels to white and dark pixels to black
    flattened_image = grayImg.flatten()
    for i in range(len(flattened_image)):
        if flattened_image[i] < white_threshold:
            flattened_image[i] = 0
        else:
            flattened_image[i] = 255
    binaryImg = np.reshape(flattened_image, grayImg.shape)

    # Save the manipulated image
    binary_filename = f'{gestureName}_binary.png'
    cv2.imwrite(binary_filename, binaryImg)
    print(f"Manipulated image of {gestureName} saved")

    # Append binary filename to the list
    filenames.append(binary_filename)

    # Delete the original captured image
    try:
        os.remove('captured_image.png')
        print("Original image deleted.")
    except FileNotFoundError:
        print("Error: Original image file not found.")
    except Exception as e:
        print(f"Error deleting the image: {e}")
    return binaryImg

def getBinaryVideo(frame):
    # Convert the frame to grayscale, for easier manipulation
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Converting the image to binary - aka turning light pixels to white and dark pixels to black
    flattened_frame = gray_frame.flatten()
    for i in range(len(flattened_frame)):
        if flattened_frame[i] < white_threshold:
            flattened_frame[i] = 0
        else:
            flattened_frame[i] = 255
    binaryImg = np.reshape(flattened_frame, gray_frame.shape)

    return binaryImg

def displayText(image, text):
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(image, text, (10, 30), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    return image

def displayMatchAccuracy(image, match):
    # Display the match accuracy on the frame in the bottom left corner
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(image, f'Match: {match}', (10, image.shape[0] - 10), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    return image

def close_application():
    print("Closing application")
    cap.release()
    cv2.destroyAllWindows()

def full_close_application():
    cap.release()
    cv2.destroyAllWindows()
    # Delete all the files in the filenames array
    for filename in filenames:
        try:
            os.remove(filename)
            print(f"Deleted file: {filename}")
        except FileNotFoundError:
            print(f"Error: File {filename} not found.")
        except Exception as e:
            print(f"Error deleting the file {filename}: {e}")

def state_no_contours(raw_frame):
    frame = displayText(raw_frame.copy(), 'Error: No contours found in some of the images')
    cv2.imshow('Video Feed', frame)
    return 'no_contours'


#TODO: Samle capture gestures functions til en function
# State functions
# Function to handle the state of capturing the first gesture
def state_capture_gesture1(raw_frame):

    # Display instructions on the frame
    frame = displayText(raw_frame.copy(), 'Press "s" to save the image, "q" to quit')
    cv2.imshow('Video Feed', frame)  # Show the frame in the 'Video Feed' window

    if key == ord('s'):  # If 's' key is pressed
        getBinaryImage(raw_frame, 'gesture1')  # Save the image as 'gesture1'
        return 'capture_gesture2'  # Transition to the next state
    
    return 'capture_gesture1'  # Remain in the current state

# Function to handle the state of capturing the second gesture
def state_capture_gesture2(raw_frame):

    # Display instructions on the frame
    frame = displayText(raw_frame.copy(), 'Press "q" to quit')
    cv2.imshow('Video Feed', frame)  # Show the frame in the 'Video Feed' window

    if key == ord('s'):  # If 's' key is pressed
        getBinaryImage(raw_frame, 'gesture2')  # Save the image as 'gesture2'
        return 'process_gestures'  # Transition to the next state

    return 'capture_gesture2'  # Remain in the current state

# Function to handle the state of processing the gestures
# It is getting the contours of all the gestures, so as not to load during runtime
def state_process_gestures(raw_frame):

    # Load the global variables
    global contours1, contours2

    # Display instructions on the frame
    frame = displayText(raw_frame.copy(), 'Press "q" to quit')
    cv2.imshow('Video Feed', frame)  # Show the frame in the 'Video Feed' window

    # Load all gesture images
    gesture1 = cv2.imread(filenames[0], cv2.IMREAD_GRAYSCALE)
    gesture2 = cv2.imread(filenames[1], cv2.IMREAD_GRAYSCALE)

    # Find the contours of all gestures
    contours1, _ = cv2.findContours(gesture1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours2, _ = cv2.findContours(gesture2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # If no contours are found, display an error message, go to no contour state
    if len(contours1) == 0 or len(contours2) == 0:
        print("Error: No contours found in the images")
        return 'no_contours'

    return 'match_gesture'  # Transition to the next state

# Function to handle the state of matching the captured gesture with the live feed
def state_match_gesture(raw_frame):

    # Load the global variables
    global contours1, contours2

    # Display instructions on the frame
    frame = displayText(raw_frame.copy(), '')
    binary_frame = getBinaryVideo(raw_frame)  # Convert the frame to binary

    # Find the contours in the binary frame
    contoursLive, _ = cv2.findContours(binary_frame, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Set the contours to compare the gestures with the live feed
    match_gesture1 = round(cv2.matchShapes(contoursLive[0], contours1[0], 1, 0.0), 2)
    match_gesture2 = round(cv2.matchShapes(contoursLive[0], contours2[0], 1, 0.0), 2)

    displayMatchAccuracy(frame, match_gesture1)  # Display the match accuracy on the frame

    # If the match is above a certain threshold, display a match message
    if match_gesture1 < 0.2:
        frame = displayText(frame, 'Gesture1')
    elif match_gesture2 < 0.2:
        frame = displayText(frame, 'Gesture2')
    else:
        frame = displayText(frame, 'No gesture')

    # Show the frames in the respective windows
    cv2.imshow('Video Feed', frame)
    cv2.imshow('Binary Frame', binary_frame)

    return 'match_gesture'  # Remain in the current state

# State dictionary
states = {
    'capture_gesture1': state_capture_gesture1,
    'capture_gesture2': state_capture_gesture2,
    'process_gestures': state_process_gestures,
    'match_gesture': state_match_gesture,
    'no_contours': state_no_contours
}

# Open the camera
cap = cv2.VideoCapture(0)

# Initial state
current_state = 'capture_gesture1'

while current_state:
    # Capture frame-by-frame
    ret, frame = cap.read()
    raw_frame = cv2.flip(frame, 1)  # Flip the frame horizontally (mirror effect)
    
    if not ret:
        break

    #Define the key press
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        close_application()
        
    # Execute the current state function
    current_state = states[current_state](raw_frame)

