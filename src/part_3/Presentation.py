import os
import cv2

class Presentation:
    def get_initial_image(self):
        image_name = input("Enter the image name (located inside of img/part_3 folder): ")
        script_dir = os.path.dirname(os.path.abspath(__file__))
        img_path = os.path.abspath(os.path.join(script_dir, f'../../img/part_3/{image_name}'))

        image = cv2.imread(img_path)
        if image is None:
            print("Could not load image. Check img/part_3 folder.")
            raise ValueError(f"Image was not found at this path: {img_path}")
        return image
    
    def show_menu(self):
        print("\n==== Mini Photo Editor ====")
        print("1. Adjust Brightness")
        print("2. Adjust Contrast")
        print("3. Convert to Grayscale")
        print("4. Add Padding (choose border type & ratio)")
        print("5. Apply Thresholding (binary or inverse)")
        print("6. Blend with Another Image (manual alpha)")
        print("7. Undo Last Operation")
        print("8. View History of Operations")
        print("9. Save and Exit")
        choice = input("Select an option: ")
        return choice