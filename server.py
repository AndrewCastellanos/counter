from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = ' keep it safe'

@app.route('/')
def index():
    if 'count' in session:
        session['count'] +=1
    else:
        session['count'] = 1
    if 'real_count' not in session:
        session['real_count'] =1
    return render_template("index.html", how_many_=session['count'], how_many_real=session['real_count'])

@app.route('/', methods=['POST'])
def index2():
    how_many_to_add = request.form['adnum']
    if how_many_to_add == "1":
        return redirect('/destroy_session')
    elif how_many_to_add == "2":
        session['count'] +=1
        session['real_count'] +=1
        return render_template("index.html", how_many=session['count'], how_many_real=session['real_count'])
    elif how_many_to_add == "3":
        session['count'] +=2
        session['real_count'] +=1
        return render_template("index.html", how_many=session['count'], how_many_real=session['real_count'])
    else:
        session['count'] += int(how_many_to_add)
        session['real_count'] +=1
        return render_template("index.html", how_many_=session['count'], how_many_real=session['real_count'])


@app.route('/destroy_session')
def clear_cookie():
    session.clear()		
    
    return redirect('/')


if __name__ == '__main__':
    app.run(debug = True)