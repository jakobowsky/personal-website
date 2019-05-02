import kronos

from blog.models import InstaPost
from blog.ig_scraper import Scraper


def add_post(post):
    _, created = InstaPost.objects.get_or_create(
        link_id=post['shortcode'],
        defaults={
            'img': post['display_url'],
            'description': post['edge_media_to_caption']['edges'][0]['node']['text'],
            'url':  f"www.instagram.com/jakobowsky/p/{post['shortcode']}",
        }
    )
    return created


@kronos.register('0 */2 * * *')
def clear_db_every_hour():
    scraper = Scraper()
    results = scraper.profile_page_recent_posts()

    InstaPost.objects.all().delete()
    for post in results:
        add_post(post)
