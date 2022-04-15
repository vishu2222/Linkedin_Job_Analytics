from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import secretKeys

path = 'D:\drive\projects\jobSkillAnalytics\pythonSelenium\pythonSelenium\chromedriver.exe'
url = 'https://www.linkedin.com/'
driver = webdriver.Chrome(path)
driver.get(url = url)
driver.maximize_window()
un = secretKeys.username
pwd = secretKeys.pwd
job_key = "Data Science\n"

# login
driver.find_element_by_name("session_key").send_keys(un)
driver.find_element_by_name("session_password").send_keys(pwd)
button = driver.find_element_by_class_name("sign-in-form__submit-button")
button.click()
sleep(3)

# search data science jobs
try:
    jobs = driver.find_element_by_xpath('//*[@id="global-nav-typeahead"]/input')
except:
    jobs = driver.find_element_by_class_name('search-global-typeahead__input.always-show-placeholder')
finally:
    jobs.send_keys(job_key)
    jobs.send_keys(Keys.ENTER)

sleep(5)





# expand the search results
try:
    seeAll = driver.find_element_by_class_name("app-aware-link")
except:
    print('unable to expand')
finally:
    seeAll.click()
    sleep(4)



jobTitles = driver.find_elements_by_class_name("disabled.ember-view.job-card-container__link.job-card-list__title")
links = [job.get_attribute('href') for job in jobTitles]
job_dictionary = {}
i=0
for link in links:
    driver.get(url=link)
    sleep(3)
    description = driver.find_element_by_css_selector('button[aria-label="Click to see more description"]')
    description.click()
    details = driver.find_element_by_id("job-details")
    text = details.text
    # print(text)
    job_dictionary[i] = [link,text]
    i=i+1
    sleep(3)








sleep(20)
driver.close()
driver.quit()








