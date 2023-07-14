from decouple import config
import pymysql
import traceback

from src.utils.Logger import Logger

def get_connection():
    """
    The function `get_connection` returns a connection object to a MySQL database using the
    configuration values from environment variables.
    :return: a connection object to a MySQL database.
    """
    try:
        return pymysql.connect(
            host=config('MYSQL_HOST'),
            user=config('MYSQL_USER'),
            db=config('MYSQL_DB')
        )
    except Exception as ex:
        Logger.add_to_log("error", str(ex))
        Logger.add_to_log("error", traceback.format_exc())
