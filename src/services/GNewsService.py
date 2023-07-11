import traceback
import urllib.request
import json

from src.utils.Logger import Logger


# The GNewsService class is a Python class that represents a service for retrieving news articles from
# the GNews API.
class GNewsService():

    @classmethod
    def get_articles(cls):
        """
        The function `get_articles` retrieves articles from the GNews API using a specified API key and
        returns a list of articles.
        
        :param cls: The parameter `cls` is typically used as a convention to refer to the class itself
        within a class method. In this case, it seems that the `get_articles` function is defined within
        a class, and `cls` is used as a reference to that class. However, since `cls`
        :return: The function `get_articles` returns a list of articles.
        """
        try:
            apikey='16f3b09d70a4e1aca16a7c1ceca73bf4'
            url = f'https://gnews.io/api/v4/search?q=example&apikey={apikey}'

            articles = []

            with urllib.request.urlopen(url) as response:
                data = json.loads(response.read().decode("utf-8"))
                articles = data["articles"]

            return articles
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())
