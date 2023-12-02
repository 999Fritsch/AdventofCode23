"""
--- Day 1: Trebuchet?! ---

Something is wrong with global snow production, and you've been selected to take a look. The Elves have even given you a map; on it, they've used stars to mark the top fifty locations that are likely to be having problems.

You've been doing this long enough to know that to restore snow operations, you need to check all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").

As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.

The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?
"""
from typing import Tuple, List

class CalibrationValueReader:
    """Reads calibration values from a file.

    Attributes:
        lines (List[str]): A list containing lines read from the file.

    Methods:
        __init__: Initializes CalibrationValueReader with a filepath.
        read_input: Reads lines from the file and stores them.
        read_calibration_value: Reads the calibration values from a line.
        read_all_lines: Reads all lines and calculates the sum of calibration values.
    """

    def __init__(self, filepath: str) -> None:
        """Initializes CalibrationValueReader with a filepath.

        Args:
            filepath (str): The path of the file to be read.
        """
        self.lines: List[str] = []
        self.read_input(filepath)

    def read_input(self, filepath: str) -> None:
        """Reads lines from the file and stores them.

        Args:
            filepath (str): The path of the file to be read.
        """
        with open(filepath, "r") as file:
            self.lines = file.readlines()

    def read_calibration_value(self, line: str) -> Tuple[int, int]:
        """Reads the calibration values from a line.

        Args:
            line (str): A string containing characters.

        Returns:
            Tuple[int, int]: A tuple containing the first and last digits found in the line.
        """
        first_digit: int = -1
        current_digit: int = -1

        for character in line:
            if character.isdigit():
                if first_digit == -1:
                    first_digit = int(character)
                current_digit = int(character)

        return first_digit, current_digit
    
    def read_all_lines(self) -> int:
        """Reads all lines and calculates the sum of calibration values.

        Returns:
            int: The sum of all calibration values read from the file.
        """
        self.sum_of_all: int = 0

        for line in self.lines:
            first_digit, last_digit = self.read_calibration_value(line)
            calibration_value: int = first_digit * 10 + last_digit
            print(f"{line.strip()} -> {calibration_value}")
            self.sum_of_all += calibration_value

        return self.sum_of_all


if __name__ == "__main__":
    # Usage example
    file_path: str = "day1/dayOneInput.txt"
    reader = CalibrationValueReader(file_path)
    sum_of_all_values = reader.read_all_lines()
    print(f"The sum of all of the calibration values is: {sum_of_all_values}")
