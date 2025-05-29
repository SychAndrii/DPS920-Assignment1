from abc import ABC, abstractmethod

class Operation(ABC):
    """
    Abstract base class for image processing operations.

    Each subclass must implement:
        - transformed_img: returns the processed image.
        - action_desc: returns a description of the performed action.

    Attributes:
        img (np.ndarray): The input image to be processed.
    """
    def __init__(self, img):
        """
        Initialize the operation with the provided image.

        Args:
            img (np.ndarray): The image to be processed.
        """
        self.img = img

    @abstractmethod
    def transformed_img(self):
        """
        Apply the operation to the image and return the transformed result.

        Returns:
            np.ndarray: The processed image.
        """
        pass

    @abstractmethod
    def action_desc(self):
        """
        Return a description of the action performed.

        Returns:
            str: Description of the operation.
        """
        pass