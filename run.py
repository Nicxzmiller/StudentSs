from app import create_app, db
from werkzeug.serving import run_simple

# runs the entire application
app = create_app()
options = {"use_reloader":True, "use_debugger":True}
if __name__ == '__main__':
    run_simple(hostname="127.0.0.1", port=8080, application=app, **options)
