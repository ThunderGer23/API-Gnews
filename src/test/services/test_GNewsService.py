# Services
from src.services.GNewsService import GNewsService


def test_get_articles_not_none():
    """
    The function `test_get_articles_not_none` checks if the `articles` variable returned by the
    `get_articles` method of the `GNewsService` class is not `None`.
    """
    articles = GNewsService.get_articles()
    assert articles != None


def test_get_articles_has_elements():
    """
    The function `test_get_articles_has_elements` checks if the `articles` list returned by the
    `get_articles` method of the `GNewsService` class has elements.
    """
    articles = GNewsService.get_articles()
    assert len(articles) > 0


def test_get_articles_check_elements_length():
    """
    The function `test_get_articles_check_elements_length` checks if the length of each article obtained
    from the GNewsService is greater than 0.
    """
    articles = GNewsService.get_articles()
    for article in articles:
        assert len(article) > 0
