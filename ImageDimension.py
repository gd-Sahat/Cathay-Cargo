import cv2 

# Load the image 
img = cv2.imread(r"C:\Users\User\Documents\GitHub\Cathay-Cargo\a_closed_box_on_conveyor_belt_from_the_top_view.png") 
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# Convert to grayscale 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
cv2.imshow('Image', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
#to separate the object from the background 
ret, thresh = cv2.threshold(gray, 127, 255, 0) 

# Find the contours of the object 
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 

# Draw the contours on the original image 
cv2.drawContours(img, contours, -1, (0,255,0), 3) 

# Get the area of the object in pixels 
area = cv2.contourArea(contours[0]) 

# Convert the area from pixels to a real-world unit of measurement (e.g. cm^2) 
scale_factor = 0.1 # 1 pixel = 0.1 cm 
size = area * scale_factor ** 2

# Print the size of the object 
print('Size:', size) 

# Display the image with the contours drawn 
cv2.imwrite(r"C:\Users\User\Documents\GitHub\Cathay-Cargo\a.png", img) 
cv2.waitKey(0) 

# Save the image with the contours drawn to a file 
cv2.imwrite('.\\object_with_contours.jpg', img)

# import cv2

# # Load the image
# img = cv2.imread(r"C:\Users\User\Documents\GitHub\Cathay-Cargo\a_closed_box_on_conveyor_belt_from_the_top_view.png")

# # Convert to grayscale
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# # Apply thresholding to separate the object from the background
# ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# # Find contours of the object
# contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# minimum_area_threshold = 1000

# # Filter contours based on area
# filtered_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > minimum_area_threshold]

# # Draw bounding boxes around the filtered contours
# for cnt in filtered_contours:
#     x, y, w, h = cv2.boundingRect(cnt)
#     cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
#     size = w * h  # Calculate size based on width and height

#     # Print the size of each bounding box
#     print('Size:', size)

# # Display the image with bounding boxes
# cv2.imshow('Object Detection', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()