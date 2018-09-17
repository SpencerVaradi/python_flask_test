import os
from app import create_app
print os.getenv('FLASK_CONFIG')
config_name = 'default' #os.getenv('FLASK_CONFIG') #or 'default'
app = create_app(config_name)

if __name__ == '__main__':
    app.run()