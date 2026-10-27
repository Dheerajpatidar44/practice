import cv2

image_path = input("LMC5429A.jpg").strip()
if not image_path:
    image_path = "LMC5429A.jpg"


image = cv2.imread(image_path)

if image is not None:

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # 4. User se window ka title / naam lena (kaha show karwana hai)
    window_name = input("colour image").strip()
    if not window_name:
        window_name = "Grayscale Window"
    
    # Window open karna aur display karna
    cv2.imshow(window_name, gray_image)
    print(f"Image display ho rahi hai window '{window_name}' me. Aage badhne ke liye koi bhi key dabaye...")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    # 5. User se output file ka naam lena (save ke liye)
    output_name = input("Enter output file name to save (press Enter for 'output_gray.jpg'): ").strip()
    if not output_name:
        output_name = "output_gray.jpg"
        
    # Grayscale image ko save karna
    success = cv2.imwrite(output_name, gray_image)
    if success:
        print(f"Image successfully save ho gayi: '{output_name}'")
    else:
        print("Image save nahi ho saki!")
else:
    print(f"Image not found: '{image_path}'")
