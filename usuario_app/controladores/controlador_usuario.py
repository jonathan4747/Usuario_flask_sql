from flask import Flask, render_template, request, redirect, session
from usuario_app import app
from usuario_app.modelos.modelo_usuarios import Usuario

@app.route('/')
def paginablanca():
    return redirect('/user')


@app.route('/user',methods=['GET'])
def paginaUsuario():
        listaUsuarios=Usuario.listaUsuario()
        return render_template("index.html", usuarios=listaUsuarios)
    
@app.route('/user/new' , methods=['GET'])
def paginaRegistor():
    return render_template("plataforma.html")

@app.route('/añadir',methods=['GET'])
def botonAñadir():
    return redirect('/user/new')

@app.route('/registro',methods=['POST'])
def añadirRegistro():
    nuevoUsuario = {
        "nombre" : request.form["nombre"],
        "apellido" : request.form["apellido"],
        "email" : request.form["email"]
    }
    #session["nombre"]=request.form["nombre"]
    #session["apellido"]=request.form["apellido"]
    #session["email"]=request.form["email"]
    resultado = Usuario.agregarUsuario(nuevoUsuario)
    return redirect('/user')



