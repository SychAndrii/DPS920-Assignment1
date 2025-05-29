import os
import cv2
import numpy as np

script_dir = os.path.dirname(os.path.abspath(__file__))

img1_path = os.path.abspath(os.path.join(script_dir, '../img/part_2/summer.jpg'))
img2_path = os.path.abspath(os.path.join(script_dir, '../img/part_2/winter.jpg'))
img_res_path = os.path.abspath(os.path.join(script_dir, '../img/part_2/manual_blend.jpg'))

print("Absolute path to image1:", img1_path)
print("Absolute path to image2:", img2_path)

img1 = cv2.imread(img1_path)
img2 = cv2.imread(img2_path)

if img1 is None:
    print(f"Error: Cannot read {img1_path}")
    exit()
if img2 is None:
    print(f"Error: Cannot read {img2_path}")
    exit()

img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

alpha = 0.5
blend = (1 - alpha) * img1 + alpha * img2
blend = blend.astype(np.uint8)

cv2.imshow('Blended Image', blend)
cv2.imwrite(img_res_path, blend)
cv2.waitKey(0)
cv2.destroyAllWindows()
