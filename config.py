from decouple import config


# The Config class contains a SECRET_KEY attribute that is retrieved from a configuration file.
class Config():
    SECRET_KEY = config('SECRET_KEY')


# The above class is a configuration class for development purposes with the DEBUG mode enabled.
class DevelopmentConfig(Config):
    DEBUG = True

# The DeployConfig class is a subclass of the Config class with the DEBUG attribute set to False.
class DeployConfig(Config):
    DEBUG = False

# The `config` dictionary is defining different configurations for different environments. It maps the
# environment names ('development' and 'deploy') to the corresponding configuration classes
# (`DevelopmentConfig` and `DeployConfig`). This allows you to easily switch between different
# configurations based on the environment you are working in.
config = {
    'development': DevelopmentConfig,
    'deploy': DeployConfig
}
