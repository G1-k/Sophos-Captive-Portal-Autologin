# Autologin Captive Portal

## Raspberry Pi 

### 1. Install Dependencies
```
sudo apt-get upgrade
sudo apt-get update
sudo apt-get install iceweasel
sudo pip3 install selenium
```
### 2. Install Geckodriver

#### Check the geckodriver version required for your firefox version:
https://firefox-source-docs.mozilla.org/testing/geckodriver/Support.html

Here version of firefox in Pi was `firefox v78.0`, Hence `geckodriver v0.21.0` was installed 

1. Download the geckodriver from mozilla: 
https://github.com/mozilla/geckodriver/releases/download/v0.21.0/geckodriver-v0.21.0-arm7hf.tar.gz


2. Extract the downloaded file
```
tar -xzvf geckodriver-v0.21.0-arm7hf.tar.gz
cd geckodriver-v0.21.0-arm7hf.tar.gz
```

3. Copy file to /usr/local/bin
```
sudo cp geckodriver /usr/local/bin/
```
4. Test the geckodriver installation
```
python3
>>> from selenium import webdriver
>>> browser = webdriver.Firefox()
```
A Browser pops up (and stays without any errors)

### 3. Run Python File for Auto Login

Put appropriate captive-portal link and login credentials in `python.py`, then
```
python3 auto-login.py
```
Firefox GUI should pop up and automatically enter the credentials and login


## PC/Laptops 
 ...
