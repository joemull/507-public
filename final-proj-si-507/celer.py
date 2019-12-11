from flask import Flask, render_template, request
from aio import revolve


app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def search():
    if request.method == 'POST':
        q = request.form['q']
        return render_template('search.html',artworks=revolve(q=q))
    else:
        return render_template('index.html')

if __name__ == '__main__':
    print('starting Flask app', app.name)
    app.run(debug=True)
