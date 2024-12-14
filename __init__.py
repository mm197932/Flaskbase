from flask import Flask, render_template
from .controllers.myapp import myapp
from .helpers.helpers import utility_processor
import os

def create_app():
    app = Flask(__name__)
    
    app_name = [
        myapp,
    ]

    for i in app_name:
        app.register_blueprint(i)
    
    app.context_processor(utility_processor)

    print(os.getenv("FLASK_ENV"))

    # /err にアクセスするとエラーが発生するルーティング
    @app.route('/err')
    def index():
        print("hoge" + 1)
        return render_template('myapp/index.html')

    @app.errorhandler(404)
    def error_404(error):
      return render_template('error/404.html')
    
    @app.errorhandler(500)
    def internal_server_error(error):
      return render_template('error/500.html')
    
    return app