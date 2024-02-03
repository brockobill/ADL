
import re  # provides support for regular expressions in Python
import unittest  # built-in unit testing framework for writing and running tests


def find_animals(animals, patterns):
    results = (
        []
    )  # stores output = strings indicating which patterns are found in which animals
    for animal in animals:  # loops over each item in animal list
        for pattern in patterns:  # loops over each item in the pattern list
            if re.search(
                pattern, animal
            ):  # checks if current pattern is found anywhere in current animal string.
                results.append((f"found {pattern} in {animal}"))  # if found message
    return results


"""
The TestAnimalPatterns class inherits from unittest.TestCase.
This class  is used to write test cases.

"""
class TestAnimalPatterns(unittest.TestCase):
    def test_find_animals(self):
        """
        Defines a method in the test class.
        This method will contain the test code for the find_animals function.

        """
        animals = (  # tuple of animal name
            "bandicoot",
            "bear",
            "blue tongue lizard",
            "boa constrictor",
            "brushtail possum",
            "cobra",
            "kookaburra",
            "python",
            "wombat",
            "zebra",
        )
        patterns = [
            "b.a",
            "^b.a",
            "ba",
            "b.*a",
            "b.+a$",
        ]  
        # regular expression patterns and test inputs for function
        expected_results = [
            "found ba in bandicoot",
            "found b.*a in bandicoot",
            "found b.a in bear",
            "found ^b.a in bear",
            "found b.*a in bear",
            "found ba in bandicoot",
            "found b.*a in blue tongue lizard",
            "found b.a in boa constrictor",
            "found ^b.a in boa constrictor",
            "found b.*a in boa constrictor",
            "found b.*a in brushtail possum",
            "found b.a in cobra",
            "found b.*a in cobra",
            "found b.+a$ in cobra",
            "found b.*a in kookaburra",
            "found b.+a$ in kookaburra",
            "found ba in wombat",
            "found b.*a in wombat",
            "found b.a in zebra",
            "found b.*a in zebra",
            "found b.+a$ in zebra",
        ]
        """
        This line is the actual test assertion. 
        It calls the find_animals function with the test inputs and checks if the output matches the expected_results. 
        If they match, the test passes; if not, it fails.
        
        """
        self.assertEqual(find_animals(animals, patterns), expected_results)
       

"""
Line 1: Runs if the script is executed as the main program and not imported as a module in another script.
Line 2: Runs the test when the script is executed. It looks for classes that inherit from unittest. TestCase and runs the test methods defined in them.
"""
if __name__ == "__main__":
    unittest.main()
    
