import flask
import numpy as np
import requests

url = "https://www.plugai.xyz/inference/integer/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiS2FkdW5hX1J1cmFsXzUwIn0.BpTaJr8s-BblYLcEnRKDbfwy1olk3PBOQ8iCUkze26g"

app=flask.Flask(__name__,template_folder='templates')
@app.route('/', methods=['GET','POST'])
def main():

    if flask.request.method == 'GET':
        return flask.render_template('main.html')

    if flask.request.method == 'POST':
        if flask.request.form['gender_male'] == 'Male':
            gender_male=1
        else:
            gender_male=0
        if flask.request.form['may'] == 'Yes':
            may=1
        else:
            may=0
        if flask.request.form['march'] == 'Yes':
            march=1
        else:
            march=0
        if flask.request.form['august'] == 'Yes':
            august=1
        else:
            august=0
        if flask.request.form['september'] == 'Yes':
            september=1
        else:
            september=0
        if flask.request.form['june'] == 'Yes':
            june=1
        else:
            june=0
        if flask.request.form['february'] == 'Yes':
            february=1
        else:
            february=0
        if flask.request.form['october'] == 'Yes':
            october=1
        else:
            october=0
        if flask.request.form['november'] == 'Yes':
            november=1
        else:
            november=0
        if flask.request.form['july'] == 'Yes':
            july=1
        else:
            july=0
        if flask.request.form['december'] == 'Yes':
            december=1
        else:
            december=0
        if flask.request.form['april'] == 'Yes':
            april=1
        else:
            april=0
        if flask.request.form['january'] == 'Yes':
            january=1
        else:
            january=0
        age=flask.request.form['age']
        if flask.request.form['adult_group'] == 'Adult':
            adult_group=1
        else:
            adult_group=0
        if flask.request.form['NmA'] == 'Yes':
            NmA=1
        else:
            NmA=0
        if flask.request.form['NmC'] == 'Yes':
            NmC=1
        else:
            NmC=0
        if flask.request.form['NmW'] == 'Yes':
            NmW=1
        else:
            NmW=0
        if flask.request.form['alive'] == 'Alive':
            alive=1
        else:
            alive=0

        payload={'fig': ','.join([str(gender_male),str(may),str(march),str(august),str(september),str(june),str(february),str(october),str(november),str(july),str(december),str(april),str(january),str(age),str(adult_group),str(NmA),str(NmC),str(NmW),str(alive)])}

        files = [

        ]

        headers = {
        'Cookie': '__cfduid=dff1fabb883912efdce5fe0da9af16c871603217819'
        }
        response = requests.request("POST", url, headers=headers, data = payload, files = files)
        idx2class={0: 'NO', 1: 'A'}
        model=response.text.split('[[')[1].split(']]')[0]
        a=np.rint(float(model))
        u,inv=np.unique(a,return_inverse=True)
        prediction=np.array([idx2class[x] for x in u])[inv].reshape(a.shape)
        prediction
        if prediction=='NO':
            percent=(float(model)/0.5)*100
        else:
            percent=((1-float(model))/0.5)*100

        return flask.render_template('main.html',percent=percent,result=prediction)
if __name__=='__main__':
    app.run()