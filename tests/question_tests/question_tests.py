#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_d.question_d import test_config, get_person_category

class Test_Config(unittest.TestCase):

    def test_question_d_config(self):
        self.assertEqual(True, test_config())

    def test_get_person_year(self):
        self.assertEqual(get_person_category(0), "Infant")
        self.assertEqual(get_person_category(2), "Child")
        self.assertEqual(get_person_category(14), "Teenager")
        self.assertEqual(get_person_category(20), "Adult")