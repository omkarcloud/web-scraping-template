from bose import *

class ScrapeLinksTask(BaseTask):
    task_config = TaskConfig(output_filename = "links")

    
    def run(self, driver):
        """
            To begin, verify whether the sitemap or RSS feed of the target website includes your desired links. 
            If the links are present, extract and store them as a list in "local_storage.json" under the variable name `links`.

            If the sitemap or RSS feed of the target website don't contains your desired links, use the provided code to perform links scraping:
        """

        def perform_scrape():
            # Write Code here to visit each page, extract links from each page and return it. 
            pass

        # ... Code to scrape Google Maps links
        driver.organic_get("https://target-website.com/auth/sign-up/") 

        scraped_links = perform_scrape()
        LocalStorage.set_item('links', scraped_links)
        return scraped_links
