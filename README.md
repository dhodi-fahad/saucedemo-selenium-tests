# SauceDemo Test Automation
This project contains automated Selenium Python tests for 
SauceDemo.com a simulated e-commerce website

### Technologies Used
- Python 3.10
- pytest (Test runner)
- Selenium WebDriver (Web browser automation)

### Project Structure
- `views:` Python modules containing Page Object classes for 
different website pages (Home, Product, Cart, Checkout)
- `tests:` Python modules containing test cases
- `README.md:` This file (you're reading it!)

- `requirements.txt:` File listing required Python libraries

### Running Tests
1. Install required libraries: `pip install -r requirements.txt`
2. Run tests with pytest: `pytest tests`

### Page Object Model
This project utilizes the Page Object Model (POM) for 
improved test organization and maintainability. 
Each page has a dedicated class with methods for 
interacting with its elements.

### Disclaimer
This project is for demo purposes only and does not represent 
a complete e-commerce automation solution. It focuses on demonstrating 
basic Selenium testing techniques with the POM.
