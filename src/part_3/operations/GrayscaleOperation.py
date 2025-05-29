from .Operation import Operation
import cv2
import numpy as np

class GrayscaleOperation(Operation):
    """
    Concrete implementation of the Operation class for converting an image to grayscale.

    Attributes:
        img (np.ndarray): The input image.
    """
    def __init__(self, img):
        """
        Initialize with the image.

        Args:
            img (np.ndarray): The input image.
        """
        super().__init__(img)

    def transformed_img(self):
        """
        Convert the input image to grayscale.

        Returns:
            np.ndarray: Grayscale image.
        """
        grayscale_image = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        return grayscale_image

    def action_desc(self):
        """
        Return a string describing the grayscale operation.

        Returns:
            str: Description of the grayscale conversion.
        """
        return "Image converted to grayscale."
