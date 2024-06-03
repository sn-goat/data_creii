from playwright.sync_api import sync_playwright
import time
from datetime import datetime
import schedule
import csv



def data_collector_facebook():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=50)
        page = browser.new_page()
        page.goto("https://www.facebook.com", timeout=60000)
        page.get_by_placeholder("Email or phone number").fill("nyouvopserge@gmail.com")
        page.get_by_placeholder("Password").fill("pororo2003")
        page.keyboard.press("Enter")
        time.sleep(10)

        page_url = page.url
        creii_page = "https://business.facebook.com/latest/home?asset_id=110865937928716"
        creii_stats = "https://business.facebook.com/latest/insights/benchmark?asset_id=110865937928716&ad_account_id=120215388370280339&entity_type=FB_PAGE&audience_tab=trends"
        page.goto(creii_page)
        time.sleep(5)
        page.goto(creii_stats)
        time.sleep(5)

        results = []

        elements = page.query_selector_all('span.x1xqt7ti.x10d9sdx.x1iikomf.xrohxju.x1heor9g.xq9mrsl.x1h4wwuj.xeuugli')

        for idx, el in enumerate(elements):

            results.append(int(el.text_content().strip()))

        results.append(datetime.today().strftime('%Y-%m-%d'))

        with open('data_facebook.csv', mode= 'a', newline='') as csvfile:
            csv_writer = csv.writer(csvfile, delimiter=',')
            csv_writer.writerow(results)


        browser.close()
        print(results)

def main():
    data_collector_facebook()

if __name__ == '__main__':
    schedule.every(1).minutes.do(main)

    while True:
        schedule.run_pending()
        time.sleep(1)