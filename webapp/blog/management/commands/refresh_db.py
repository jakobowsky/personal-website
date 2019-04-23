from django.core.management.base import BaseCommand

from blog.models import InstaPost
from blog.ig_scraper import Scraper

class Command(BaseCommand):

    help = 'Redownload db'

    def handle(self, *args, **kwargs):
        scraper = Scraper()
        results = scraper.profile_page_recent_posts()
        self.update_db(results)

    def add_post(self, post):
        _, created = InstaPost.objects.get_or_create(
            link_id=post['shortcode'],
            defaults={
                'img': post['display_url'],
                'description': post['edge_media_to_caption']['edges'][0]['node']['text'],
                'url':  f"www.instagram.com/jakobowsky/p/{post['shortcode']}",
            }
        )
        return created

    def update_db(self, data):
        InstaPost.objects.all().delete()
        for post in data:
            print(self.add_post(post))
