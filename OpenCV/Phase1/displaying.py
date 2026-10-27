import cv2
image = cv2.imread("images.jpg")

if image is not None:
    cv2.imshow("Image", image)  #open the window
    cv2.waitKey(0)  #wait for user to press any key
    cv2.destroyAllWindows()  #close the window
else:
    print("Image not found")