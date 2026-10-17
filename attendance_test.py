import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

ATTENDANCE_URL = "https://the-internet.herokuapp.com/checkboxes"


class AttendanceTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(ATTENDANCE_URL)
        self.boxes = self.driver.find_elements(
            By.CSS_SELECTOR, "#checkboxes input[type='checkbox']"
        )

    def test_mark_student_present(self):
        """TC-A01: ticking the checkbox marks the student present."""
        student1 = self.boxes[0]
        if not student1.is_selected():
            student1.click()
        self.assertTrue(student1.is_selected())

    def test_mark_student_absent(self):
        """TC-A02: unticking the checkbox marks the student absent."""
        student2 = self.boxes[1]          # ticked by default on this page
        if student2.is_selected():
            student2.click()
        self.assertFalse(student2.is_selected())

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()