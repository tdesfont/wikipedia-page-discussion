from unittest import TestCase

from src.scrapper.wikipedia_scrapper import fetch_page, extract_text


class Test(TestCase):

    def test_scrape_wikipedia(self):
        wikipedia_url = "https://en.wikipedia.org/wiki/Neil_Armstrong"
        html = fetch_page(wikipedia_url)
        text = extract_text(html)
        assert len(text) > 0