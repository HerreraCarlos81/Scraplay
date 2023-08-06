# Automated Coupon Submission Tool

This Python script automates the process of submitting a coupon on the website [wethrift.com](https://www.wethrift.com/). The code uses Selenium WebDriver with Chrome and the `undetected_chromedriver` library. It takes screenshots at every step of the process and saves them in the `./images/` directory.

## Dependencies

The code uses the following Python libraries:

- `selenium`
- `undetected_chromedriver`
- `csv`
- `os`
- `sys`
- `time`
- `random`

You can install these with pip:
pip install selenium undetected_chromedriver

(Note: The libraries `csv`, `os`, `sys`, `time`, and `random` are part of Python's standard library and do not need to be installed.)

## Chrome WebDriver

You need to have the Chrome WebDriver installed and available on your system path. You can download it from the [ChromeDriver download page](https://sites.google.com/a/chromium.org/chromedriver/downloads).

## Running the Script

To run the script, simply navigate to the directory containing the script and run the following command:

Replace "your_script_name.py" with the name of your Python script.

The script will open the [wethrift.com](https://www.wethrift.com/) website, find a specific coupon, submit a random amount for the savings, and then take a screenshot of the result.

## Screenshots

The process screenshots are saved in the `./images/` directory. The script takes a screenshot at every step of the process, from opening the website to submitting the coupon.

## Notification

The script checks if the final coupon is available on the webpage and if so, it has a placeholder to add code for notifying success. If not, it has a placeholder to add code for notifying failure.

## Support

If you have any issues or questions, please open a new issue on this GitHub repository.





