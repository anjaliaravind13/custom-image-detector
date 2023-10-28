from pathlib import Path

import cv2


class CameraModule:
    def capture_image(self):
        """
        This function will capture the image and save to darknet/tmp.

        """
        filename = self.get_path()
        print(filename)

        cam = cv2.VideoCapture(0)
        result = True
        while result:
            ret, frame = cam.read()
            cv2.imshow(filename, frame)
            cv2.imwrite(filename, frame)
            result = False

        cam.release()
        cv2.destroyAllWindows()

    def get_path(self):
        """
        This function will return the path.

        Returns:
            str : path for save the image
        """
        current_path = str(Path.cwd())
        current_path = (
            "/home/user/Desktop/project/image_detector/"
            "yolo/darknet/tmp/image.jpg"
        )
        return current_path
