from playwright.sync_api import sync_playwright
import time
from datetime import datetime
import csv

def data_collector_linkedin():
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
        time.sleep(5)

        results = []

        followers = page.query_selector("a.ember-view.text-body-xsmall-bold.org-organizational-page-admin-navigation__follower-count")
        elements = page.query_selector_all("p.text-heading-xlarge")

        results.append(int("".join([i for i in followers.text_content().strip() if i.isdigit()])))

        for idx, el in enumerate(elements):
            if idx < 3:
                continue
            results.append(int(el.text_content().strip()))

        results.append(datetime.today().strftime('%Y-%m-%d'))

        with open('data_linkedin.csv', mode='a', newline='') as csvfile:
            csv_writer = csv.writer(csvfile, delimiter=',')
            csv_writer.writerow(results)

        browser.close()
        print(results)
