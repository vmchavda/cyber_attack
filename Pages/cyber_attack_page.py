from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from BrowserManager import Browser
from Pages.BasePage import UiObject
from time import sleep

class CyberAttackPage:
    sort_data=UiObject(By.XPATH,"//select[@name='sort-select']")
    filter_data=UiObject(By.XPATH,"//input[@name='filter-input']")

    names=UiObject(By.XPATH,"//div[@class='table-data data-name']")
    no_of_cases=UiObject(By.XPATH,"//div[@class='table-data data-cases']")
    imapact=UiObject(By.XPATH,"//div[@class='table-data data-averageImpact']")
    complexity=UiObject(By.XPATH,"//div[@class='table-data data-complexity']")

    rows=UiObject(By.XPATH,"//div[@class='table-row']")
    def get_name(self,no):
        return Browser.get_driver().find_element(By.XPATH,"(//div[@class='table-data data-name'])[{}]".format(no))
    def get_no_of_cases(self,no):
        return Browser.get_driver().find_element(By.XPATH,"(//div[@class='table-data data-cases'])[{}]".format(no))
    def get_avg_impact_score(self,no):
        return Browser.get_driver().find_element(By.XPATH,"(//div[@class='table-data data-averageImpact'])[{}]".format(no))
    def get_complexity(self,no):
        return Browser.get_driver().find_element(By.XPATH,"(//div[@class='table-data data-complexity'])[{}]".format(no))

    def get_sort_data(self,name):
        select = Select(Browser.get_driver().find_element_by_id('sort-select'))
        select.select_by_visible_text(name)
    def convert_value(self,t):
        if 'k' in t:
            t = t.replace('k', '000')
            t = t.replace('.', '')

        if 'M' in t:
            t = t.replace('M', '000000')
            t = t.replace('.', '')
        if 'B' in t:
            t = t.replace('B', '000000000')
            t = t.replace('.', '')

        return int(t)




