from .Operation import Operation
from .GrayscaleOperation import GrayscaleOperation
import cv2
import numpy as np

class ThresholdOperation(Operation):
    """
    Concrete implementation of the Operation class for applying thresholding.

    Attributes:
        img (np.ndarray): The input image.
        threshold (int): The threshold value.
        max_value (int): The maximum value to use with thresholding.
        threshold_type (int): OpenCV threshold type (BINARY or BINARY_INV).
    """
    def __init__(self, img):
        """
        Initialize with the image.

        Args:
            img (np.ndarray): The input image.
        """
        super().__init__(img)
        self.threshold = 127  # default threshold
        self.max_value = 255  # default max value
        self.threshold_type = cv2.THRESH_BINARY  # default threshold type

    def transformed_img(self):
        """
        Prompt the user for a threshold value and threshold type, then apply thresholding.

        Returns:
            np.ndarray: Thresholded image.
        """
        threshold = int(input("Enter threshold value (0 to 255): "))
        if not (0 <= threshold <= 255):
            raise ValueError("Please enter a value between 0 and 255.")
        self.threshold = threshold

        print("\nChoose thresholding type:")
        print("1: cv2.THRESH_BINARY")
        print("2: cv2.THRESH_BINARY_INV")
        type_choice = input("Enter choice (1 or 2): ").strip()

        if type_choice == "1":
            self.threshold_type = cv2.THRESH_BINARY
        elif type_choice == "2":
            self.threshold_type = cv2.THRESH_BINARY_INV
        else:
            raise ValueError("Invalid choice. Please enter 1 or 2.")

        if len(self.img.shape) == 3:
            grayscale_operaiton = GrayscaleOperation(self.img)
            gray_image = grayscale_operaiton.transformed_img()
        else:
            gray_image = self.img

        _, thresholded_image = cv2.threshold(
            gray_image,
            self.threshold,
            self.max_value,
            self.threshold_type
        )
        return thresholded_image

    def action_desc(self):
        """
        Return a string describing the thresholding operation.

        Returns:
            str: Description of the thresholding.
        """
        type_desc = "BINARY" if self.threshold_type == cv2.THRESH_BINARY else "BINARY_INV"
        return f"Applied {type_desc} thresholding at {self.threshold}."
