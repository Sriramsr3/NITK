from flask import Flask, render_template

app = Flask(__name__)

# Route to render HTML file
@app.route('/')
def home():
    return render_template('hello.html')

if __name__ == '__main__':
    app.run(debug=True)
