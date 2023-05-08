# Automated-course-offerings-extraction

Accessing the website and navigating it to get to the course offerings page was done through the python package selenium.

The initial code uses microsoft edge through selenium. This is the version executed by running the code without the argument -i (interactive). This will proceed without asking the user for any input, assuming that the user has the microsoft edge browser (binary) downloaded and present in its default location. As for the driver, it will proceed to download it through the code.

Adding an argument -i (interactive) will allow the user to choose between chrome and microsoft edge, and to specify the path for the browser it it is not in its default location.
If microsoft edge is chosen the user will be asked for the paths of the edge browser (binary) and driver.
If chrome is chosen, the user will be asked whether he would like to specify the paths for the browser (binary) and driver, or would like to let the code download the driver for him and detect the browser path in its default location.

For both option, the argument headless was added so that the browser will not be shown and only the final results will appear for the user.

 wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
 sudo sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
 sudo apt-get update
 sudo apt-get install google-chrome-stable
 
 
curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg
sudo install -o root -g root -m 644 microsoft.gpg /etc/apt/trusted.gpg.d/
sudo sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/edge stable main" > /etc/apt/sources.list.d/microsoft-edge-dev.list'
sudo apt-get install microsoft-edge-dev

