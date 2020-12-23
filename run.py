from app import create_app, db  
from app.models import User

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User}
