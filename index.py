from config import config
from src import init_app

# The code is retrieving the configuration settings for the 'development' environment from the
# `config` dictionary and assigning it to the variable `configuration`.
configuration = config['development']
app = init_app(configuration)

if __name__ == '__main__':
    app.run()
