import cv2
import numpy as np

img = np.zeros((600, 600, 3), dtype=np.uint8)

outer_radius = 100
gap_size = 50
gap_thickness = 22

center_x = 300
top_center = (center_x, 210)
left_center = (center_x - 120, 400)
right_center = (center_x + 120, 400)

cv2.ellipse(img, top_center, (outer_radius, outer_radius), 0, 0, 360, (0, 0, 255), 20, cv2.LINE_AA)
cv2.ellipse(img, top_center, (outer_radius, outer_radius), 0, 90 - gap_size // 2, 90 + gap_size // 2, (0, 0, 0), gap_thickness, cv2.LINE_AA)

cv2.ellipse(img, left_center, (outer_radius, outer_radius), 0, 0, 360, (0, 255, 0), 20, cv2.LINE_AA)
cv2.ellipse(img, left_center, (outer_radius, outer_radius), 0, 330 - gap_size // 2, 330 + gap_size // 2, (0, 0, 0), gap_thickness, cv2.LINE_AA)

cv2.ellipse(img, right_center, (outer_radius, outer_radius), 0, 0, 360, (255, 0, 0), 20, cv2.LINE_AA)
cv2.ellipse(img, right_center, (outer_radius, outer_radius), 0, 270 - gap_size // 2, 270 + gap_size // 2, (0, 0, 0), gap_thickness, cv2.LINE_AA)

cv2.putText(img, "OpenCV", (220, 570), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 4, cv2.LINE_AA)

cv2.imshow("OpenCV Logo", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
