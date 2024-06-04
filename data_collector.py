from playwright.sync_api import sync_playwright
import time
from datetime import datetime
import csv

class DataColector:
    def __init__(self):
        self.__results_facebook = self.__data_collector_facebook()
        self.__results_linkedin = self.__data_collector_linkedin()

    @property
    def results_facebook(self):
        return self.__results_facebook

    @property
    def results_linkedin(self):
        return self.__results_linkedin

    def __data_collector_facebook(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False, slow_mo=50)
            page = browser.new_page()
            page.goto("https://www.facebook.com", timeout=60000)
            page.get_by_placeholder("Email or phone number").fill("nyouvopserge@gmail.com")
            page.get_by_placeholder("Password").fill("pororo2003")
            page.keyboard.press("Enter")
            time.sleep(10)

            creii_stats = "https://business.facebook.com/latest/insights/benchmark?asset_id=110865937928716&ad_account_id=120215388370280339&entity_type=FB_PAGE&audience_tab=trends"

            page.goto(creii_stats)
            time.sleep(5)

            results = []

            elements = page.query_selector_all("span.x1xqt7ti.x10d9sdx.x1iikomf.xrohxju.x1heor9g.xq9mrsl.x1h4wwuj.xeuugli")

            for idx, el in enumerate(elements):
                if idx == 0:
                    continue
                results.append(int(el.text_content().strip()))

            results.append(datetime.today().strftime('%Y-%m-%d'))

            print(results)

            return results

    def __data_collector_linkedin(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False, slow_mo=50)
            page = browser.new_page()
            page.goto("https://www.linkedin.com/login", timeout=60000)
            page.get_by_label("Email or Phone").fill("nyouvopserge@gmail.com")
            page.get_by_label("Password").fill("pororo2003")
            page.keyboard.press("Enter")
            time.sleep(10)

            creii_page = "https://www.linkedin.com/company/94176093/admin/dashboard/"
            page.goto(creii_page)
            time.sleep(10)

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

    def __csv_writer_results_facebook(self):
        with open('data_facebook.csv', mode='a', newline='') as csvfile_facebook:
            csv_writer_facebook = csv.writer(csvfile_facebook)
            csv_writer_facebook.writerow(self.__results_facebook)

    def __csv_writer_results_linkedin(self):
        with open('data_linkedin.csv', mode='a', newline='') as csvfile_linkedin:
            csv_writer_linkedin = csv.writer(csvfile_linkedin)
            csv_writer_linkedin.writerow(self.__results_linkedin)

    def csv_writer_results(self):
        self.__csv_writer_results_facebook()
        self.__csv_writer_results_linkedin()


