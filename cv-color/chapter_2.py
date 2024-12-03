import cv2
import numpy as np


blue_lower = np.array([90, 150, 0])
blue_upper = np.array([140, 255, 255])

yellow_lower = np.array([20, 100, 100])
yellow_upper = np.array([40, 255, 255])


img = cv2.imread("opencv/image.png")


alpha = 1
beta = 0
img = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)


imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


blue_mask = cv2.inRange(imgHSV, blue_lower, blue_upper)
yellow_mask = cv2.inRange(imgHSV, yellow_lower, yellow_upper)


contours_blue, _ = cv2.findContours(
    blue_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)

contours_yellow, _ = cv2.findContours(
    yellow_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)

for contour in contours_blue:
    if cv2.contourArea(contour) > 1000:
        x, y, w, h = cv2.boundingRect(contour)

        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(
            img, "Blue", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2
        )
for contour in contours_yellow:
    if cv2.contourArea(contour) > 1000:
        x, y, w, h = cv2.boundingRect(contour)

        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
        cv2.putText(
            img, "Yellow", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 255), 2
        )
cv2.imshow("Detected Colors", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
