import cv2
image = cv2.imread("LMC5429A.jpg")

if image is not None:
    success = cv2.imwrite("new_image.jpg", image)
    if success:
        print("image saved successfully as new_image.jpg")
    else:
        print("image not saved")
else:
    print("Image not found")
 
 
