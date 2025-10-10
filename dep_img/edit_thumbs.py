import cv2
import numpy as np

# --- Load the image ---
img = cv2.imread("dep_img\Like_copy.bmp")

# Convert to RGBA (so we can have transparency)
img_rgba = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)

# --- Convert to grayscale for masking ---
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# --- Threshold to detect the circle area (colored circle ≠ white) ---
# This assumes the white areas have high grayscale values.
_, mask = cv2.threshold(gray, 250, 255, cv2.THRESH_BINARY_INV)

# --- Find the largest contour (should be the circle) ---
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
if contours:
    largest_contour = max(contours, key=cv2.contourArea)
    
    # Create an empty mask and draw the circle area
    circle_mask = np.zeros_like(gray)
    cv2.drawContours(circle_mask, [largest_contour], -1, 255, thickness=cv2.FILLED)
    
    # Invert mask to find outside region
    outside_mask = cv2.bitwise_not(circle_mask)
    
    # Set alpha=0 (transparent) for outside pixels
    img_rgba[outside_mask == 255] = (0, 0, 0, 0)

# --- Save the result ---
cv2.imwrite("Like_no_outside_white.png", img_rgba)

print("✅ Saved: Dislike_no_outside_white.png")
