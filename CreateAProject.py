import sys
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


def create_a_project():
    ########### Elements' attributes on Log In Page ###########
    username_field = "login"
    password_field = "password"
    sign_in_field = "commit"

    ########### Log in credentials ###########
    username_cred = "hhphu"
    password_cred = "It'sthe2ndPassword>.<"

    ########### Create new repository page ###########
    repository_name_field = "repository_name"
    create_repository_button_xpath = "//button[@class='btn btn-primary first-in-line']"

    # Path to the Projects Folder. Modify the path if needed
    projects_path = '/Users/phu/Projects'

    # Path to the chromedriver. Modify the path if needed
    chromedriver_path="/usr/local/bin/chromedriver"

    # Take the new folder's name & create a new folder
    folderName = str(sys.argv[1])
    #print("Current Directory: " + os.getcwd())
    os.chdir(projects_path)
    #print("Current Directory: " + os.getcwd())
    os.mkdir(folderName)
    new_project_path = os.path.join(projects_path , folderName)
    os.chdir(new_project_path)
    #print("Current Directory: " + os.getcwd())

    # Go to GitHub login page.
    browser = webdriver.Chrome(chromedriver_path)
    browser.get('https://github.com/login')
    browser.fullscreen_window()

    # Log in GitHub
    username = browser.find_element_by_name(username_field)
    password = browser.find_element_by_name(password_field)
    sign_in = browser.find_element_by_name(sign_in_field)
    username.click()
    username.send_keys(username_cred)
    password.click()
    password.send_keys(password_cred)
    sign_in.click()

    # Create a new repository
    browser.get("https://github.com/new")
    repository_name = browser.find_element_by_id(repository_name_field)
    repository_name.send_keys(folderName)

    # wait till the Create Repository button clickable
    browser.implicitly_wait(10)
    create_repository_button = browser.find_element_by_xpath(create_repository_button_xpath)
    create_repository_button.submit()
    browser.implicitly_wait(10)
    browser.quit()


if __name__ == "__main__":
    create_a_project()
