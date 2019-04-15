import requests
import json
from bs4 import BeautifulSoup
from pprint import pprint

from django.core.management.base import BaseCommand


class Command(BaseCommand):

    help = 'Update instagram-posts'

    def handle(self, *args, **kwargs):
        scraper = Scraper()
        results = scraper.profile_page_recent_posts()
        scraper.extract_useful_info(results[1])




class Scraper:

    def __init__(self):
        self.link = 'https://www.instagram.com/jakobowsky/'

        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
            'AppleWebKit/537.11 (KHTML, like Gecko) '
            'Chrome/23.0.1271.64 Safari/537.11',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'none',
            'Accept-Language': 'en-US,en;q=0.8',
            'Connection': 'keep-alive'
        }

    def __request_url(self):
        try:
            response = requests.get(
                self.link,
                timeout=4,
                headers=self.headers,
            ).text
        except requests.HTTPError:
            raise requests.HTTPError('Received non 200 status code from Instagram')
        except requests.RequestException:
            raise requests.RequestException
        else:
            return response

    @staticmethod
    def extract_json_data(html):
        soup = BeautifulSoup(html, 'html.parser')
        body = soup.find('body')
        script_tag = body.find('script')
        raw_string = script_tag.text.strip().replace('window._sharedData =', '').replace(';', '')
        return json.loads(raw_string)
    @staticmethod
    def extract_2(html):
        soup = BeautifulSoup(html, 'html.parser')
        body = soup.find('body')
        return body.prettify()

    def profile_page_metrics(self):
        # nice function but not needed for now
        results = {}
        try:
            response = self.__request_url()
            json_data = self.extract_json_data(response)
            metrics = json_data['entry_data']['ProfilePage'][0]['graphql']['user']
        except Exception as e:
            raise e
        else:
            for key, value in metrics.items():
                if key != 'edge_owner_to_timeline_media':
                    if value and isinstance(value, dict):
                        value = value['count']
                        results[key] = value
                    elif value:
                        results[key] = value
        return results
 
    def profile_page_recent_posts(self):
        results = []
        try:
            response = self.__request_url()
            json_data = self.extract_json_data(response)
            #pprint(json_data)
            metrics = json_data['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']["edges"]
        except Exception as e:
            raise e
        else:
            for node in metrics:
                node = node.get('node')
                if node and isinstance(node, dict):
                    results.append(node)
        return results


    def extract_useful_info(self, context):
        print(context.get('display_url'))
        print(context['edge_media_to_caption']['edges'][0]['node']['text'])
        print(context['shortcode'])
        

        
