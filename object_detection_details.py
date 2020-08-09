import cv2

def generate_images(Results):
    img1= cv2.imread("Input Frame/"+ str(Results['original_frame']+5) +".jpg")
    img2= cv2.imread("Input Frame/"+ str(Results['copied_frame']+6) +".jpg")

    cv2.imwrite("Output/Original.jpg" , img1)
    
    gray1=cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2=cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    
    diff = cv2.absdiff(gray1,gray2)
    blur = cv2.GaussianBlur(diff, (25,25), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)

    contour_image=img1.copy()
    _,contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:         
        (x, y, w, h) = cv2.boundingRect(contour)

        if cv2.contourArea(contour) < 900:
            continue
        cv2.drawContours(contour_image, contours, -1, (0, 255, 255), 2)
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(img1, (x, y), (x+w, y+h), (0, 255, 255), 2)
        
    
    cv2.imwrite("Output/Grayscale.jpg" , gray1)
    cv2.imwrite("Output/Difference.jpg" , diff)
    cv2.imwrite("Output/Gaussian_blur.jpg" , blur)
    cv2.imwrite("Output/Threshold.jpg" , thresh)
    cv2.imwrite("Output/Dilation.jpg" , dilated)
    cv2.imwrite("Output/Contours.jpg" , contour_image)
    cv2.imwrite("Output/Bounding_box.jpg" , img1)   
            
