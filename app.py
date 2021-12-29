from flask import Flask, request, url_for, redirect, abort, render_template

app = Flask(__name__,
            # static_folder = "./test/static",
            # template_folder="./test/templates"
            )

@app.route('/')
def basic_controller():
    return "Hello World\n"

# Recuperar params (el tipo del param (int) es opcional)
@app.route('/blog/<string:blog_id>', methods=['GET', 'POST'])
def param_controller(blog_id):
    print(type(blog_id))
    if request.method == "GET":
        return f"The blog ID is {blog_id}\n"
    else:
        return "POST Request\n"

# Recuperar Datos formulario - Body - Form data
@app.route('/form', methods=['POST', 'GET'])
def form_controller():
    print(request.form)
    name = request.form['name']
    email = request.form['email']
    return f"Name: {name}\nemail: {email}"

# Redirecciones
@app.route('/redirect', methods=['GET'])
def redirect_controller():
    return redirect(url_for('param_controller', blog_id=2))	

# Codigos de error
@app.route('/error', methods=['GET'])
def error_controller():
    abort(400, description="This is not a proper request")

# Devolver / Renderizar pagina HTML como respuesta
@app.route('/html', methods=['GET'])
def html_controller():
    return render_template('example.html')

# Devolver / Renderizar pagina HTML como respuesta con variables
@app.route('/html-extra', methods=['GET'])
def html_controller_extra():
    return render_template('home.html', message={"msg": "Hello World"})

# Devolver respuesta en formato JSON
@app.route('/json', methods=['GET'])
def json_controller():
    return {
        "ok": "true",
        "res": "Everything is gonna be ok"
    }



