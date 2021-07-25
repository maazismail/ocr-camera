import cv2
import pytesseract

cam = cv2.VideoCapture(0)
cv2.namedWindow("OG")

while True:
    ret, frame = cam.read()
    flip = cv2.flip(frame, 1)  #flipping camera to fix alignment    

    cv2.imshow("OG", flip)

    k = cv2.waitKey(1)
    if k%256 == 32:
        cv2.imwrite("capture.png", frame)
        print("Printing...")
        img = cv2.imread('capture.png')
        custom_config = r'--oem 3 --psm 6'
        print(pytesseract.image_to_string(img, config=custom_config))

    elif k%256 == 27:
        print("Closing...")
        break

cam.release()
cv2.destroyAllWindows()