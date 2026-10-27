import cv2
image = cv2.imread("LMC5429A.jpg")

if image is not None:
    h, w, c = image.shape
    print(f"height : {h} px")
    print(f"width : {w} px")
    print(f"channels : {c}")
else:
    print("Image not found")