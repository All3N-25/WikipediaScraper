from WikiScraper import WikiScraper
import BrowserControl

import json
import time

import SentenceBert as SBert

jsonDirectory = "JSON/Wikipedia_"

pw_instance, browser, page = BrowserControl.runBrowser()

while(True):
        start = input("Starting point: ")
        
        validity = WikiScraper(start)
        if (validity.checkIfExists()):
                break
while(True):
        target = input("Target Destination: ")

        validity = WikiScraper(target)
        if (validity.checkIfExists()):
                break
        
BrowserControl.openNext(page, start)
        
while(True):
        if(start != target):
                scraper = WikiScraper(start)
        
                scrapedTitles = scraper.Scraper()
                
                #jsonString = json.dumps(scrapedTitles)
                
                # #Write the JSON file
                # with open(jsonDirectory, "w") as json_file:
                #     json.dump(scrapedTitles, json_file, indent=4)
                
                # #Read the JSON file
                # with open(jsonDirectory, "r") as file:
                #     data_dict = json.load(file)
                
                titles = list(scrapedTitles.keys())
                query = target
                
                titleIndex = SBert.bestMatch(query, titles)
                title = titles[titleIndex]
                link = scrapedTitles[title]
                
                print(f"{title} -> {link}")
                
                start = title        
                
                BrowserControl.openNext(page, start)
        else:
                time.sleep(1000)
                break
