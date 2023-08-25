# OHRM_Python
# Create the virtual environment before running the test files
# Run "pip install -r--requirements.txt" to install the dependencies

Listed below keywords for which WebDriverWait is added for 10 secs.

# Use as click_element(__attribute_value__)
1. click_element(self, att):
        ele = WebDriverWait(self.driver, self.wait).until(expected_conditions.visibility_of_element_located(att))
        ele.click()

# Use as send_text(__attribute_value__, __entryData__)
2. send_text(self, att, value):
        ele = WebDriverWait(self.driver, self.wait).until(expected_conditions.visibility_of_element_located(att))
        ele.send_keys(value)

# Use as is_visible(__attribute_value__)
3. is_visible(self, att):
        ele = WebDriverWait(self.driver, self.wait).until(expected_conditions.visibility_of_element_located(att))
        return bool(ele)

# Use as take_screenshot()
4. take_screenshot(self):
        filename = str(int(time.time())) + ".png"
        print(filename)
        os.chdir("../")
        filepath = os.path.join("Resources/Screenshots/" + filename)
        self.driver.save_screenshot(filepath)

# Reports

To run the report install the dependency "pytest-html-reporter"
https://github.com/prashanth-sams/pytest-html-reporter

The HTML report will auto generate while running the pytest tests in CLI "pytest -v"
