from .Operation import Operation
import cv2
import numpy as np

class PaddingOperation(Operation):
    """
    Concrete implementation of the Operation class for adding padding.

    Attributes:
        img (np.ndarray): The input image.
        top, bottom, left, right (int): Padding sizes.
        border_type (int): OpenCV border type flag.
        color (tuple): Color for constant padding.
    """
    def __init__(self, img):
        """
        Initialize with the image.

        Args:
            img (np.ndarray): The input image.
        """
        super().__init__(img)
        self.top = 0
        self.bottom = 0
        self.left = 0
        self.right = 0
        self.border_type = cv2.BORDER_CONSTANT
        self.color = (0, 0, 0)

    def transformed_img(self):
        """
        Prompt the user for padding size, border type, and ratio, and apply it.

        Returns:
            np.ndarray: Image with padding.
        """
        print("\nChoose border type:")
        print("1. Constant")
        print("2. Reflect")
        print("3. Replicate")
        choice = input("Select option (1-3): ").strip()
        if choice == '1':
            self.border_type = cv2.BORDER_CONSTANT
            color_input = input("Enter border color as B,G,R (e.g., 255,0,0 for blue): ").strip()
            color_values = color_input.split(',')
            if len(color_values) != 3:
                raise ValueError("Color must have 3 comma-separated values.")
            self.color = tuple(map(int, color_values))
            if not all(0 <= c <= 255 for c in self.color):
                raise ValueError("Each color component must be between 0 and 255.")
        elif choice == '2':
            self.border_type = cv2.BORDER_REFLECT
        elif choice == '3':
            self.border_type = cv2.BORDER_REPLICATE
        else:
            raise ValueError("Invalid choice for border type.")

        print("\nChoose padding ratio:")
        print("1. Square")
        print("2. Rectangle (original aspect ratio)")
        print("3. Custom Ratio (e.g., 4:5)")
        ratio_choice = input("Select option (1-3): ").strip()
        if ratio_choice not in ('1', '2', '3'):
            raise ValueError("Invalid choice for ratio.")

        total_padding = int(input("Enter padding size per side in pixels (>=0): "))
        if total_padding < 0:
            raise ValueError("Total padding must be >= 0.")

        h, w = self.img.shape[:2]

        if ratio_choice == '1':
            if h > w:
                diff = h - w
                self.left = diff // 2
                self.right = diff - self.left
                self.top = self.bottom = 0
            elif w > h:
                diff = w - h
                self.top = diff // 2
                self.bottom = diff - self.top
                self.left = self.right = 0
            else:
                # Already square
                self.top = self.bottom = self.left = self.right = 0

            self.top += total_padding
            self.bottom += total_padding
            self.left += total_padding
            self.right += total_padding
        elif ratio_choice == '2':
            self.top = total_padding
            self.bottom = total_padding
            self.right = total_padding
            self.left = total_padding
        elif ratio_choice == '3':
            custom_ratio_input = input("Enter custom ratio as W:H (e.g., 4:5): ").strip()
            if ':' not in custom_ratio_input:
                raise ValueError("Custom ratio must be in W:H format.")
            w_ratio, h_ratio = map(int, custom_ratio_input.split(':'))
            if w_ratio <= 0 or h_ratio <= 0:
                raise ValueError("Both width and height ratios must be positive integers.")

            desired_ratio = w_ratio / h_ratio
            current_ratio = w / h
            if current_ratio > desired_ratio:
                new_h = int(w / desired_ratio)
                diff = new_h - h
                self.top = diff // 2
                self.bottom = diff - self.top
                self.left = self.right = 0
            else:
                new_w = int(h * desired_ratio)
                diff = new_w - w
                self.left = diff // 2
                self.right = diff - self.left
                self.top = self.bottom = 0

        padded_image = cv2.copyMakeBorder(
            self.img,
            self.top,
            self.bottom,
            self.left,
            self.right,
            self.border_type,
            value=self.color
        )
        return padded_image

    def action_desc(self):
        """
        Return a string describing the padding operation.

        Returns:
            str: Description of the padding applied.
        """
        border_type_str = {
            cv2.BORDER_CONSTANT: "BORDER_CONSTANT",
            cv2.BORDER_REFLECT: "BORDER_REFLECT",
            cv2.BORDER_REPLICATE: "BORDER_REPLICATE"
        }.get(self.border_type, f"Unknown ({self.border_type})")

        return (
            f"Padding added - top:{self.top}, bottom:{self.bottom}, "
            f"left:{self.left}, right:{self.right}, border_type:{border_type_str}."
        )
