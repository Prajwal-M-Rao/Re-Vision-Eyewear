import cv2
import pytesseract
from PIL import Image
import matplotlib.pyplot as plt
import os

def capture_image(filename="temp.jpg"):
    """
    Captures a single image from the default webcam and saves it.
    Returns the image path if successful, otherwise None.
    """
    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()
    if ret:
        cv2.imwrite(filename, frame)
    camera.release()
    return filename if ret else None

def grayscale(image):
    """
    Converts a BGR image to grayscale.
    """
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def display(im_path):
    """
    Displays an image with matplotlib at actual size.
    """
    dpi = 80  # Dots per inch for accurate sizing
    im_data = plt.imread(im_path)
    height, width = im_data.shape[:2]
    figsize = width / dpi, height / dpi

    fig = plt.figure(figsize=figsize)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.imshow(im_data, cmap='gray')
    ax.axis('off')  # Hide axes for cleaner view
    plt.show()

def perform_ocr(image_path):
    """
    Performs OCR on the given image and returns the extracted text.
    """
    return pytesseract.image_to_string(Image.open(image_path))

if __name__ == "__main__":
    # Step 1: Capture image from webcam
    image_path = capture_image()
    
    if image_path:
        # Step 2: Convert to grayscale
        img = cv2.imread(image_path)
        gray_image = grayscale(img)

        # Step 3: Save grayscale image
        gray_path = os.path.join(os.getcwd(), "gray.jpg")
        cv2.imwrite(gray_path, gray_image)

        # Step 4: OCR processing
        print("Performing OCR...")
        extracted_text = perform_ocr(image_path)
        print("Extracted Text:")
        print(extracted_text)

        # Step 5: Display the grayscale image
        display(gray_path)
    else:
        print("Failed to capture image from camera.")
