from waitress import serve
from flaskr import create_app

app = create_app()
serve(app, host='192.168.1.182', port=5001)