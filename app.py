from waitress import serve
from applications.main import app

if __name__ == "__main__":
    serve(app, port=5000)
