from audio_module.audio_module import Audio
from camera_module.camera_module import CameraModule
from yolo.detector import Detector


def run():
    """
    This is the main function that connect and call all the utility functions.
    """
    camera_module = CameraModule()
    detector = Detector()
    audio = Audio()

    camera_module.capture_image()
    output_data = detector.detect()
    audio.generate_audio(outputs=output_data)


run()
