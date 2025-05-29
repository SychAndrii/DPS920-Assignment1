from .Operation import Operation
import cv2
import numpy as np

class BrightnessOperation(Operation):
    """
    Concrete implementation of the Operation class for adjusting brightness.

    Attributes:
        img (np.ndarray): The input image.
        value (int): The brightness adjustment value.
    """
    def __init__(self, img):
        """
        Initialize with the image.

        Args:
            img (np.ndarray): The input image.
        """
        super().__init__(img)
        self.value = 0

    def transformed_img(self):
        """
        Prompt the user for brightness adjustment value and apply it.

        Returns:
            np.ndarray: Brightness-adjusted image.
        """
        delta = int(input("Enter brightness delta (-255 to 255): "))
        if -255 <= delta <= 255:
            self.value = delta
        else:
            raise ValueError("Please enter a value between -255 and 255.")

        if self.value > 0:
            bright_image = cv2.add(self.img, np.full_like(self.img, self.value))
        else:
            bright_image = cv2.subtract(self.img, np.full_like(self.img, -self.value))
        return bright_image

    def action_desc(self):
        """
        Return a string describing the brightness operation.

        Returns:
            str: Description of the brightness adjustment.
        """
        return f"Brightness adjusted by {self.value}."
