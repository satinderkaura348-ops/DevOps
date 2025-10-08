from app import app

@app.route('/')
@app.route('/')

def index():
    user = {"username" : "Sammy"}
    return render_template('index.html', title='Home', user=user)

