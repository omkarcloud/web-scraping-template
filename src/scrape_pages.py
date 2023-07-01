from bose import *

class ScrapePagesTask(BaseTask):

    def get_data(self):
        scraped_links = LocalStorage.get_item('links', [])
        return [scraped_links]

    def run(self, driver, scraped_links):
        def extract_page_data():
            # Write Code here to extract required data from the page and return as dictionary
            pass

        def perform_scrape():
            items = []
            for link in scraped_links:
                driver.get_by_current_page_referrer(link)
                item = extract_page_data()
                items.append(item)
            return items
    
        driver.organic_get("https://target-website.com/auth/sign-up/") 

        result = perform_scrape()
        return result