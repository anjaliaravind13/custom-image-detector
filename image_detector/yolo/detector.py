import os


class Detector:
    def __init__(self) -> None:
        pass

    def detect(self):
        """
        This function detects the object
        received by the camera module and
        write as an output file.

        Returns:
            Data(list): Output as list
        """
        filename = os.path.join(os.path.dirname(__file__), "runner.sh")
        os.system(f"bash {filename}")
        data = self.output_loader()
        return data

    def output_loader(self):
        """
        This function will read the outputs file.
        and return as string.

        Returns:
            Data(list): Output as list
        """
        filename = os.path.join(os.path.dirname(__file__), "darknet/output.txt")
        with open(filename, "r") as file:
            data = file.readlines()
            cleaned_data = self.clean(data)
            return cleaned_data

    def clean(self, outputs):
        """
        This function will clean the outputs data.
        and return as list.

        Args:
            outputs (str): This is the output after detecting the objects.

        Returns:
            list[str]: Cleaned output as list of strings
        """
        data_to_return = []
        for output in outputs[1:]:
            output = output.strip()
            output = output.split(": ")
            output = output[0]
            data_to_return.append(output)

        return data_to_return
