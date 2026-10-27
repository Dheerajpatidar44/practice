import cv2

image = cv2.imread("LMC5429A.jpg")

if image is None:
    print("image not found")

else:
    print("image found")

    resized = cv2.resize(image, (600,400))

    cv2.imshow("original image", image)
    cv2.imshow("resized image", resized)

    cv2.imwrite("resized image.jpg", resized)

    cv2.waitKey(0)
    cv2.destroyAllWindows()