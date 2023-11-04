import requests
from unstructured.partition.html import partition_html
import yaml
from bs4 import BeautifulSoup
import json


# extract open ai api key from config.yaml

with open("config.yaml", "r") as config:
    open_ai_key = yaml.load(config, Loader=yaml.FullLoader)["openai"]


class GetJobs(object):
    def __init__(self):
        self.filename = "job5.html"

    def extract_jobs(self):
        with open(self.filename) as f:
            soup = BeautifulSoup(f, "html.parser")

        # Extracting information
        title = soup.title.text

        # blurb = soup.find("p", {"data-test-task-summary"}).text.strip()

        submission_link = soup.find("a", {"data-test-cta": "submit-design"})["href"]

        price_div = soup.find("div", class_="column shrink")
        price = price_div.text if price_div else "Price not found"

        """
        deadline = (
            soup.find("h5", {"data-test-time-left"})
            .find(text=True, recursive=False)
            .strip()
        )

        requirements = {
            "mustHave": [
                i.text
                for i in soup.find("h6", text="Must have")
                .find_next_sibling("ul")
                .find_all("li")
            ],
            "niceToHave": [
                i.text
                for i in soup.find("h6", text="Nice to have")
                .find_next_sibling("ul")
                .find_all("li")
            ],
            "shouldNotHave": [
                i.text
                for i in soup.find("h6", text="Should not have")
                .find_next_sibling("ul")
                .find_all("li")
            ],
        }
        """
        # Outputting information as a JSON object
        output = json.dumps(
            {
                "title": title,
                # "blurb": blurb,
                "link_for_submission": submission_link,
                "price": price,
                # "deadline": deadline,
                # "requirements": requirements,
            },
            indent=4,
        )
        print(output)

    def save_to_db(self):
        pass

    def assess_jobs(self):
        jobs = self.extract_jobs()


def main():
    get_jobs = GetJobs()
    get_jobs.extract_jobs()


if __name__ == "__main__":
    main()
