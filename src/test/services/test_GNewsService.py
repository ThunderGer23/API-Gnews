# Services
from src.services.GNewsService import GNewsService


def test_get_articles_not_none():
    articles = GNewsService.get_articles()
    assert articles != None


def test_get_articles_has_elements():
    articles = GNewsService.get_articles()
    assert len(articles) > 0


def test_get_articles_check_elements_length():
    articles = GNewsService.get_articles()
    for article in articles:
        assert len(article) > 0
