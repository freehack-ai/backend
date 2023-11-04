import requests
from unstructured.partition.html import partition_html
import yaml

# extract open ai api key from config.yaml

with open("config.yaml", "r") as config:
    open_ai_key = yaml.load(config, Loader=yaml.FullLoader)["openai"]


class GetJobs(object):
    def __init__(self, url):
        self.url = url

    def extract_jobs(self):
        partitioned_html = partition_html(self.url)
        print(partitioned_html)
        return partitioned_html

    def save_to_db(self):
        pass

    def assess_jobs(self):
        jobs = self.extract_jobs()


def main():
    get_jobs = GetJobs(
        url="https://www.freelancer.com/jobs/html_css/?fixed_max=50&hourly_duration=1&languages=en&fixed_min=40"
    )
    get_jobs.extract_jobs()


if __name__ == "__main__":
    main()
