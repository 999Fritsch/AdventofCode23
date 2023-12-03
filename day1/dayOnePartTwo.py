from typing import Tuple, Optional
import re
from dayOne import CalibrationValueReader

numbers = {
    1: [1, "one"],
    2: [2, "two"],
    3: [3, "three"],
    4: [4, "four"],
    5: [5, "five"],
    6: [6, "six"],
    7: [7, "seven"],
    8: [8, "eight"],
    9: [9, "nine"]
}


class CalibrationValueReaderTwo(CalibrationValueReader):
    """A class for reading calibration values from a file.

    Args:
        filepath (str): The path to the file.

    Attributes:
        filepath (str): The path to the file being read.
    """

    def __init__(self, filepath: str) -> None:
        """Initializes CalibrationValueReaderTwo.

        Args:
            filepath (str): The path to the file.
        """
        super().__init__(filepath)

    def read_calibration_value(self, line: str) -> Tuple[Optional[int], Optional[int]]:
        """Reads the calibration values from a line.

        This method searches for calibration values in a line and returns a tuple
        containing two integers representing the found values.

        Args:
            line (str): The line to extract values from.

        Returns:
            Tuple[Optional[int], Optional[int]]: A tuple of two integers
            representing the found values. If no values are found, (None, None) is returned.
        """
        first_digit: Tuple[Optional[int], int] = (None, -1)
        current_digit: Tuple[Optional[int], int] = (None, -1)
        
        for number in numbers.values():
            for each in number:
                index_list = [m.start() for m in re.finditer(str(each), line)]
                if index_list:
                    for index in index_list:
                        if first_digit[1] == -1:
                            current_digit = (number[0], index)
                            first_digit = (number[0], index)
                        else:
                            if index < first_digit[1]:
                                first_digit = (number[0], index)
                            elif index > current_digit[1]:
                                current_digit = (number[0], index)
            
        if first_digit[0] is None:
            return None, None

        return first_digit[0], current_digit[0]
    
if __name__ == "__main__":
    # Usage example
    file_path: str = "day1/dayOneInput.txt"
    reader = CalibrationValueReaderTwo(file_path)
    sum_of_all_values = reader.read_all_lines()
    print(f"The sum of all of the calibration values is: {sum_of_all_values}")