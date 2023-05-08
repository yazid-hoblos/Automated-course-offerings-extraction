# Automated-course-offerings-extraction

# Description

This code is designed to automate the extraction of the course offerings for the Department of computer science and mathematics at LAU. It will take the user credentials as arguments, access the university website, and navigate it accordingly to get to the course offerings page and save the course offerings for BIF, CSC, and MTH in Byblos for Fall 2023 in a csv file.

Accessing the website and navigating it to get to the course offerings page was done through the python package selenium.


# Running the script

**Mode 1:** _python3 run.py <username> <password>_
 
The initial code uses microsoft edge through selenium. This is the version executed by running the script without the argument -i (interactive). This will proceed without asking the user for any input, assuming that the user has the microsoft edge browser (binary) downloaded and present in its default location. As for the driver, it will proceed to download it through the code.

The microsoft edge browser was downloaded to the terminal using the commands:
 * curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg
 * sudo install -o root -g root -m 644 microsoft.gpg /etc/apt/trusted.gpg.d/
 * sudo sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/edge stable main" > /etc/apt/sources.list.d/microsoft-edge-dev.list'
 * sudo apt-get install microsoft-edge-dev
 
**Mode 2:** _python3 run.py -i <username> <password>_
 
Adding an argument -i (interactive) will allow the user to choose between chrome and microsoft edge, and to specify the path for the browser it it is not in its default location.
If microsoft edge is chosen the user will be asked for the paths of the edge browser (binary) and driver.
If chrome is chosen, the user will be asked whether he would like to specify the path for the browser (binary), or would like to let the code download the driver for him and detect the browser path in its default location.

The chrome driver was downloaded to terminal using the commands:
 * wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
 * sudo sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
 * sudo apt-get update
 * sudo apt-get install google-chrome-stable

For both browser options, the argument headless was added so that the browser will not be shown and only the final results will appear for the user.


 # Output
 
 The output csv data could be found in this repository and it is outputted as output.csv. Some courses were found to occupy 2 rows, since they have a lab part in addition to the course part, so another csv file (mutated_data.csv) was created to merge the rows of these classes into one. In addition, this mutated dataset applies some changes to the column names to be more understandable.

 The output files output.csv and mutated_data.csv should be found in the same directory of run.py one the execution is completed.
 
 # Selenium 4.9.0 Error !!!
 
 Attempting to run my code, I found an error that seems to be due to an inappropriate object inheritence in selenium 4.9.0:** AttributeError:** _'Options' object has no attribute '_ignore_local_proxy'_
 
 This was fixed by applying minor changes to  selenium/webdriver/chromium/webdriver.py and selenium/webdriver/remote/webdriver.py (commenting the 2 lines causing the issue).
 The updated 2 files are found in this repository as remote_webdriver.py (webdriver.py of the directory remote within selenium) and chromium_webdriver.py (webdriver.py of the directory chromium within selenium), so if run into this error you may navigate to your selenium package folder and substitue them accordingly by the ones in this repository, or the lines specified in the error could be fixed. 

# Submitted files
 
 The file submission.py is the initial code all within 1 file.
 Atomic commits were also submitted: run.py / read_arguments.py / interaction_mode.py / no_interaction_mode.py / navigate_url.py / output_csv.py.
 To execute the script you must have all of them whithin same directory, and execute python3 run.py <-i>(optional) <username> <password>
 
 
