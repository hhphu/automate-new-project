#!/usr/bin/python3

import getpass
import os
import time
import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

VARIABLES ={
    'createRepository_xpath' : '//button[@class="btn btn-primary first-in-line"]',
    'login_name' : 'login',
    'password_name' : 'password',
    'repository_id' : 'repository_name',
    'signIn_name' : 'commit',
    'url_login' : 'https://github.com/login',
    'url_newRepository' : 'https://github.com/new'
}

def create_a_project():

    # Acqurire the path to the "Projects" directory
    projects_path = input("Input your Projects directory: ")

    # Acquire login credentials from users
    login_cred = input("Username or Email Address: ")
    password_cred = getpass.getpass("Password: ")

    # Take the new folder's name 
    folderName = str(sys.argv[1])

    # Path to the chromedriver 
    chromedriver_path="./chromedriver.exe"

    # Go to GitHub login page.
    browser = webdriver.Chrome(chromedriver_path)
    browser.get(VARIABLES['url_login'])
    browser.fullscreen_window()

    # Log in GitHub
    login = browser.find_element_by_name(VARIABLES['login_name'])
    password = browser.find_element_by_name(VARIABLES['password_name'])
    signIn = browser.find_element_by_name(VARIABLES['signIn_name'])
    login.send_keys(login_cred)
    password.send_keys(password_cred)
    signIn.click()
    time.sleep(3)

    # Go to new repository page
    browser.get(VARIABLES['url_newRepository'])

    # Input the new repository name
    repositoryName = browser.find_element_by_id(VARIABLES['repository_id'])
    repositoryName.send_keys(folderName)

    # Create a new repository with the given name
    createRepository = browser.find_element_by_xpath(VARIABLES['createRepository_xpath'])
    createRepository.submit()

    time.sleep(10)
    browser.quit()
 
    # Change to the Project directory
    os.chdir(projects_path) 

    # Create a new folder with the input name
    os.mkdir(folderName)

    # Change directory to newly created folder
    new_project_path = os.path.join('.' , folderName)
    os.chdir(new_project_path)


if __name__ == "__main__":
    create_a_project()
