from WikiScraper import WikiScraper
import json

Start = "Potato"
JSON_Directory  = f"JSON/Wikipedia_{Start}"

testing = WikiScraper(Start)
titles = testing.Scraper()
 
json_string = json.dumps(titles)

with open(JSON_Directory, "w") as json_file:
    json.dump(titles, json_file, indent=4)

print("success")