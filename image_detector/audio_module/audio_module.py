from gtts import gTTS
from playsound import playsound


class Audio:
    def __init__(self) -> None:
        pass

    def generate_audio(self, outputs):
        """
        This function help us to generate audio.
        Here we get the output generated by the detector.

        """
        cleaned_string = self.clean(outputs)
        self.mp3_generator(text=cleaned_string, language="en")
        self.play_audio()

    def clean(self, outputs):
        """
        This function helps to construct a
        proper sentence with detected objects.

        Args:
            outputs (str): This is the output after detecting the objects.

        Returns:
            str: sentence as output
        """
        if not outputs:
            return "There are no obstacles detected in front of you"
        base_string = f"There are {len(outputs)} object in front of you, They are,"
        for idx, output in enumerate(outputs):
            if idx + 1 == len(outputs):
                base_string += " and " + output
                continue
            base_string += output + ","
        return base_string

    def mp3_generator(self, text, language):
        """
        This function will convert an input string to an mp3 format.

        Args:
            text (str): the string that need to be converted to mp3.

        """
        myobj = gTTS(text=text, lang=language, slow=False)
        myobj.save("output_audio.mp3")

    def play_audio(self):
        """
        This function will play the mp3 file after generating.

        """
        playsound("output_audio.mp3")
        print("playing sound using  playsound")