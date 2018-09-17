DEBUG = True
class Config(object):
    """
    Common configuration
    # Put any configurations here that are common across all environments
    """

class DevelopmentConfig(Config):
    """
    Development configuration
    """

    DEBUG = True
    SQLALCHEMY_ECHO = True
    TESTING = True

class StagingConfig(Config):
    """
    Staging configuration
    """
    TESTING = True
    DEBUG = True
    SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
    """
    Production Configuration
    """

    DEBUG = False

app_config = {
    'development': DevelopmentConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

