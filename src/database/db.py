from decouple import config
from config import config as cfg
import pymysql
import traceback

# Logger
from src.utils.Logger import Logger

def get_connection():
    """
    The function `get_connection` returns a connection object based on the type of connection specified
    in the `cfg` dictionary.
    :return: a connection object.
    """
    type_connection = list(cfg.keys())
    try:
        if (type_connection == 'development'):
            return pymysql.connect(
                host=config('MYSQL_HOST'),
                user=config('MYSQL_USER'),
                password=config('MYSQL_PASSWORD'),
                db=config('MYSQL_DB')
            )
        else:
            return pymysql.connect(
                host=config('MYSQL_HOST_REMOTE'),
                port=config('MYSQL_PORT_REMOTE'),
                user=config('MYSQL_USER_REMOTE'),
                password=config('MYSQL_PASSWORD_REMOTE'),
                db=config('MYSQL_DB_REMOTE')
            )
    except Exception as ex:
        Logger.add_to_log("error", str(ex))
        Logger.add_to_log("error", traceback.format_exc())
