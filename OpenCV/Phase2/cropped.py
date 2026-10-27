import cv2

image = cv2.imread("LMC5429A.jpg")

if image is None:
    print("Image is note found")

else:
    print("image is found")
    cropped = image [100:200, 50:150]
    cv2.imshow("original", image)
    cv2.imshow("cropped", cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
