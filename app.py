from app_module import create_app
from Routes.message_bp import message_bp

app = create_app()

app.register_blueprint(message_bp, url_prefix = '/')

if __name__ == '__main__':
    app.debug = True
    app.run()