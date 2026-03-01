import cv2
import numpy as np
points = []
def mouse_callback(event, x, y, flags, param):
    global points, img_display
    if event == cv2.EVENT_LBUTTONDOWN:
        if len(points) < 4:
            points.append((x, y))
            print(f"Point {len(points)}: ({x}, {y})")
            cv2.circle(img_display, (x, y), 5, (0, 0, 255),-1)
            cv2.imshow("Image", img_display)
        if len(points) == 4:
            print("\nFour points selected:")
            for i, p in enumerate(points):
                print(f"P{i+1}: {p}")
            print("Press any key to exit.")
        
img = cv2.imread("turf.jpg")
if img is None:
    raise FileNotFoundError("Image not found.")
img_display = img.copy()
cv2.namedWindow("Image")
cv2.setMouseCallback("Image", mouse_callback)
cv2.imshow("Image", img_display)
cv2.waitKey(0)
cv2.destroyAllWindows()
points = np.array(points, dtype=np.float32)
print("\nFinal array of selected points:")
print(points)