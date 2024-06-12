import cv2

def remove_watermark(image_path):
    image = cv2.imread(image_path)
    roi = cv2.selectROI("Select ROI", image, fromCenter=False, showCrosshair=True)
    cv2.destroyWindow("Select ROI")
    x, y, w, h = roi
    replacement_area = image[y-10:y, x:x+w]
    for i in range(y, y+h):
        image[i, x:x+w] = replacement_area[i % replacement_area.shape[0]]

    cv2.imshow("Result", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

image_path = 'image.png'

remove_watermark(image_path)
