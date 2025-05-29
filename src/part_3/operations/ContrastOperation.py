from .Operation import Operation
import cv2
import numpy as np

class ContrastOperation(Operation):
    """
    Concrete implementation of the Operation class for adjusting contrast.

    Attributes:
        img (np.ndarray): The input image.
        scale (float): The contrast adjustment scale factor.
    """
    def __init__(self, img):
        """
        Initialize with the image.

        Args:
            img (np.ndarray): The input image.
        """
        super().__init__(img)
        self.scale = 1.0

    def transformed_img(self):
        """
        Prompt the user for contrast adjustment scale and apply it.

        Returns:
            np.ndarray: Contrast-adjusted image.
        """
        scale = float(input("Enter contrast scale factor (>0, e.g., 1.2 for increase, 0.8 for decrease): "))
        if scale <= 0:
            raise ValueError("Scale factor must be positive.")

        self.scale = scale

        adjusted_image = cv2.multiply(
            self.img,
            np.ones(self.img.shape, dtype="uint8"),
            scale=self.scale
        )
        return adjusted_image

    def action_desc(self):
        """
        Return a string describing the contrast operation.

        Returns:
            str: Description of the contrast adjustment.
        """
        return f"Contrast adjusted by a scale of {self.scale}."
