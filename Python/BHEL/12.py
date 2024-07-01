
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import pytesseract

# Display and save character subplots
num_chars = len(char)  # Assuming `char` contains images of license plate characters
plt.figure(figsize=(num_chars * 2, 2))  # Adjust figure size based on the number of characters

for i in range(num_chars):
    plt.subplot(1, num_chars, i + 1)
    plt.imshow(char[i], cmap='gray')  # Display in grayscale
    plt.axis('off')  # Hide axes for cleaner appearance

# Save the plot to a file
output_path = 'Car-Plates-Char(Seperated).png'
try:
    plt.savefig(output_path, bbox_inches='tight')
    print(f"Saved to {output_path}")
except Exception as e:
    print(f"Error saving the plot: {e}")

# Convert NumPy array to PIL image and perform OCR
# Ensure `img_result` contains valid image data
try:
    plate_image = Image.fromarray(img_result)
    plate_text = pytesseract.image_to_string(output_path)
    print("Plate number is:", plate_text)
except Exception as e:
