# OHRM_Python
# Create the virtual environment before running the test files
# Run "pip install -r--requirements.txt" to install the dependencies

Listed below keywords for which WebDriverWait is added for 10 secs.

1. click_element(self, att):
        ele = WebDriverWait(self.driver, self.wait).until(expected_conditions.visibility_of_element_located(att))
        ele.click()

# Use as click_element(__attribute_value__)

3. send_text(self, att, value):
        ele = WebDriverWait(self.driver, self.wait).until(expected_conditions.visibility_of_element_located(att))
        ele.send_keys(value)

# Use as send_text(__attribute_value__, __entryData__)

4. is_visible(self, att):
        ele = WebDriverWait(self.driver, self.wait).until(expected_conditions.visibility_of_element_located(att))
        return bool(ele)

# Use as is_visible(__attribute_value__)

5. take_screenshot(self):
        filename = str(int(time.time())) + ".png"
        print(filename)
        os.chdir("../")
        filepath = os.path.join("Resources/Screenshots/" + filename)
        self.driver.save_screenshot(filepath)
