from .Operation import Operation
import cv2
import numpy as np
import os

class BlendingOperation(Operation):
    """
    Concrete implementation of the Operation class for blending two images.

    Attributes:
        img (np.ndarray): The primary input image.
        second_img (np.ndarray): The second image to blend.
        second_img_filename (str): The filename of the second image.
        alpha (float): The blending weight for the first image (0 to 1).
    """
    def __init__(self, img):
        """
        Initialize with the primary image.

        Args:
            img (np.ndarray): The primary input image.
        """
        super().__init__(img)
        self.second_img = None
        self.second_img_filename = ""
        self.alpha = 0.5  # default blending ratio

    def transformed_img(self):
        """
        Prompt the user for the second image name and alpha, then blend the images.

        Returns:
            np.ndarray: The blended image.
        """
        image_name = input("Enter the image name (located inside of img/part_3 folder): ").strip()
        self.second_img_filename = image_name
        script_dir = os.path.dirname(os.path.abspath(__file__))
        img_path = os.path.abspath(os.path.join(script_dir, f'../../../img/part_3/{image_name}'))

        if not os.path.isfile(img_path):
            raise FileNotFoundError(f"Image not found at: {img_path}")

        second_img = cv2.imread(img_path)
        if second_img is None:
            raise ValueError(f"Failed to read the image at: {img_path}. Ensure it's a valid image file.")

        # Resize second image to match primary image's dimensions
        second_img_resized = cv2.resize(second_img, (self.img.shape[1], self.img.shape[0]))

        # Ensure both images have the same number of channels
        if len(self.img.shape) != len(second_img_resized.shape):
            if len(self.img.shape) == 2:
                # Primary is grayscale, convert second image to grayscale
                second_img_resized = cv2.cvtColor(second_img_resized, cv2.COLOR_BGR2GRAY)
            elif len(second_img_resized.shape) == 2:
                # Second image is grayscale, convert to color
                second_img_resized = cv2.cvtColor(second_img_resized, cv2.COLOR_GRAY2BGR)

        alpha_input = float(input("Enter alpha value for blending (0 to 1): ").strip())
        if not (0.0 <= alpha_input <= 1.0):
            raise ValueError("Alpha must be a value between 0 and 1.")
        self.alpha = alpha_input

        blended_image = cv2.addWeighted(self.img, self.alpha, second_img_resized, 1 - self.alpha, 0)
        self.second_img = second_img_resized
        return blended_image

    def action_desc(self):
        """
        Return a detailed description of the blending operation.

        Returns:
            str: Detailed description of the blending.
        """
        beta = 1 - self.alpha
        h, w = self.img.shape[:2]
        return (
            f"Blended primary image (size: {w}x{h}) with second image '{self.second_img_filename}'. "
            f"Alpha (weight for primary): {self.alpha:.2f}, Beta (weight for second): {beta:.2f}."
        )
