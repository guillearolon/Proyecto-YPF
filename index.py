from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def crear_db():
    conexion = sqlite3.connect('ctmypf.db')
    cursor = conexion.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS registros 
                   (
                   jobname VARCHAR(40) NULL,
                   changeid VARCHAR(40) NULL,
                   gruposn VARCHAR(40) NULL,
                   correo1 VARCHAR(40) NULL,
                   correo2 VARCHAR(40) NULL,
                   correo3 VARCHAR(40) NULL
                   ) ''')
    conexion.commit()
    conexion.close()

crear_db()

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        with app.app_context():
            conexion = sqlite3.connect('ctmypf.db')     
            cursor = conexion.cursor()

            jobname = request.form.get('jobname')
            changeid = request.form.get('changeid')
            gruposn = request.form.get('gruposn')
            correo1 = request.form.get('correo1')
            correo2 = request.form.get('correo2')
            correo3 = request.form.get('correo3')

            cursor.execute('INSERT INTO registros (jobname, changeid, gruposn, correo1, correo2, correo3) VALUES (?,?,?,?,?,?)', (jobname,changeid,gruposn,correo1,correo2,correo3,))
            conexion.commit()

        return redirect(url_for('index'))

    with app.app_context():
        conexion = sqlite3.connect('ctmypf.db')     
        cursor = conexion.cursor()
        job_name = request.args.get('jobname', '')
        changeid = request.args.get('changeid', '')
        gruposn = request.args.get('gruposn', '')
        correo1 = request.args.get('correo1', '')
        correo2 = request.args.get('correo2', '')
        correo3 = request.args.get('correo3', '')
    
        cursor.execute('SELECT * FROM registros WHERE jobname = ? AND changeid = ? AND gruposn = ? AND correo1 = ? AND correo2 = ? AND correo3 = ?', (job_name, changeid, gruposn, correo1, correo2, correo3))
        resultado = cursor.fetchall()

        conexion.commit()
        conexion.close()    

    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run('localhost', debug=True)