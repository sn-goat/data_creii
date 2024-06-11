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
        self.__results_instagram = self.__data_collector_instagram()

    @property
    def results_facebook(self) -> list:
        return self.__results_facebook

    @property
    def results_linkedin(self) -> list:
        return self.__results_linkedin

    @property
    def results_instagram(self) -> list:
        return self.__results_instagram

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

    def __data_collector_instagram(self) -> list:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True, slow_mo=self.SLOW_MO)
            page = browser.new_page()
            page.goto("https://www.instagram.com", timeout=self.TIMEOUT)
            page.get_by_label("Phone number, username, or email").fill("creii.mtl")
            page.get_by_label("Password").fill("Julie2021")
            page.keyboard.press("Enter")
            time.sleep(self.SLEEP)

            creii_page = "https://www.instagram.com/accounts/insights/?timeframe=30"
            page.goto(creii_page)
            time.sleep(self.SLEEP)

            results = []

            elements = page.query_selector_all("span.x1lliihq.x1plvlek.xryxfnj.x1n2onr6.x193iq5w.xeuugli.x1fj9vlw.x13faqbe.x1vvkbs.x1s928wv.xhkezso.x1gmr53x.x1cpjm7i.x1fgarty.x1943h6x.x1i0vuye.xggs18q.xuv8nkb.x5n08af.xudqn12.xw06pyt.x10wh9bi.x1wdrske.x8viiok.x18hxmgj")

            for el in elements:
                results.append(int(el.text_content().strip()))

            results.pop(0)
            results.pop(1)

            results.append(datetime.today().strftime('%Y-%m-%d'))

            print(results)

            return results



    def __csv_writer_results(self, website: str, results: list) -> None:
        abs_path = "/Users/sergilenyouvop/Desktop/SUMMER_WORK_24/data_creii/"

        with open( abs_path + website, mode='a', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(results)


    def csv_writer_results(self) -> None:
        self.__csv_writer_results("data_facebook.csv", self.__results_facebook)
        self.__csv_writer_results("data_linkedin.csv", self.__results_linkedin)
        self.__csv_writer_results("data_instagram.csv", self.__results_instagram)



