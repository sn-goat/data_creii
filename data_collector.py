from playwright.sync_api import sync_playwright
import time
from datetime import datetime
import csv

class DataCollector:
    SLEEP:int = 15
    TIMEOUT:int = 90000
    SLOW_MO:int = 50
    
    def __init__(self) -> None:
        self.__results_facebook = self.__data_collector_facebook()
        self.__results_linkedin = self.__data_collector_linkedin()

    @property
    def results_facebook(self) -> list:
        return self.__results_facebook

    @property
    def results_linkedin(self) -> list:
        return self.__results_linkedin


    def __data_collector_facebook(self) -> list:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True, slow_mo=self.SLOW_MO)
            page = browser.new_page()
            page.goto("https://www.facebook.com", timeout=self.TIMEOUT)
            page.get_by_placeholder("Email or phone number").fill("nyouvopserge@gmail.com")
            page.get_by_placeholder("Password").fill("pororo2003")
            page.keyboard.press("Enter")
            time.sleep(self.SLEEP)

            creii_stats = "https://business.facebook.com/latest/insights/benchmark?asset_id=110865937928716&ad_account_id=120215388370280339&entity_type=FB_PAGE&audience_tab=trends"

            page.goto(creii_stats)
            time.sleep(self.SLEEP)

            results = []

            elements = page.query_selector_all("span.x1xqt7ti.x10d9sdx.x1iikomf.xrohxju.x1heor9g.xq9mrsl.x1h4wwuj.xeuugli")

            for idx, el in enumerate(elements):
                if idx == 0:
                    continue
                results.append(int(el.text_content().strip()))

            results.append(datetime.today().strftime('%Y-%m-%d'))

            print(results)

            return results

    def __data_collector_linkedin(self) -> list:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True, slow_mo=self.SLOW_MO)
            page = browser.new_page()
            page.goto("https://www.linkedin.com/login", timeout=self.TIMEOUT)
            page.get_by_label("Email or Phone").fill("nyouvopserge@gmail.com")
            page.get_by_label("Password").fill("pororo2003")
            page.keyboard.press("Enter")
            time.sleep(self.SLEEP)

            creii_page = "https://www.linkedin.com/company/94176093/admin/dashboard/"
            page.goto(creii_page)
            time.sleep(self.SLEEP)

            results = []

            followers = page.query_selector("a.ember-view.text-body-xsmall-bold.org-organizational-page-admin-navigation__follower-count")
            elements = page.query_selector_all("p.text-heading-xlarge")

            results.append(int("".join([i for i in followers.text_content().strip() if i.isdigit()])))

            for idx, el in enumerate(elements):
                if idx < 3:
                    continue
                results.append(int(el.text_content().strip()))

            results.append(datetime.today().strftime('%Y-%m-%d'))

            print(results)

            return results




    def __csv_writer_results(self, website: str, results: list) -> None:
        abs_path = "/Users/sergilenyouvop/Desktop/SUMMER_WORK_24/data_creii/data/"

        with open( abs_path + website, mode='a', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(results)


    def csv_writer_results(self) -> None:
        self.__csv_writer_results("data_facebook.csv", self.__results_facebook)
        self.__csv_writer_results("data_linkedin.csv", self.__results_linkedin)



