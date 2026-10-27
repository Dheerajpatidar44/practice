# import cv2

# image = cv2.imread("LMC5429A.jpg")

# if image is None:
#     print("image not found")

# else:
#     (h,w) = image.shape[:2]
#     center = (w/2, h/2)

#     M = cv2.getRotationMatrix2D(center, 45, 1.0)
#     rotated = cv2.warpAffine(image, M, (w, h))


#     cv2.imshow("original", image)
#     cv2.imshow("rotated", rotated)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()


import cv2
image = cv2.imread("LMC5429A.jpg")

if image is None:
    print("image not found")
else:
    flipped_horizontal = cv2.flip(image,1)
    flipped_vertical = cv2.flip(image,0)
    flipped_both = cv2.flip(image, -1)

    cv2.imshow("Original image", image)
    cv2.imshow("Horizontal Flip", flipped_horizontal)
    cv2.imshow("Vertical Flip", flipped_vertical)
    cv2.imshow("Both Flip", flipped_both)       

    cv2.waitKey(0)
    cv2.destroyAllWindows()