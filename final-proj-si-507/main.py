from flask import Flask, render_template, request, redirect, url_for
import model
import mapping

app = Flask(__name__)
                      
@app.route('/',methods=['GET','POST'])
def search():
    if request.method == 'POST':
        try:
            view = request.form['view']
        except:
            view = 'list'
        q = request.form['q']
        return redirect(url_for('results',view=view,q=q))
    elif request.method == 'GET':
        return render_template('index.html')

@app.route('/results')
def results():
    view = request.args.get('view')
    q = request.args.get('q')
    artworks = model.search_index(q)
    if view == 'list':
        return render_template('results.html',artworks=artworks,q=q,view=view)
    if view == 'map':
        locatedWorks = model.locate(artworks)
        mapJSON, layoutJSON = mapping.map_for(locatedWorks)
        return render_template('results.html',
            mapJSON=mapJSON,layoutJSON=layoutJSON,q=q,view=view,
            artworks=artworks)

@app.route('/object/<pid>')
def object(pid):
    work = model.get_work_by_pid(pid)
    return render_template('object.html',work=work)

if __name__ == '__main__':
    print('starting Flask app', app.name)
    app.run(debug=True)
