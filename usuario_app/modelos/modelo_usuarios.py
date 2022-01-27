from usuario_app.config.mysqlconnection import MySQLConnection, connectToMySQL

class Usuario:
    def __init__(self,nombre,apellido,email,created_at,updated_at):
        self.nombre=nombre
        self.apellido=apellido
        self.email=email
        self.created_at=created_at
        self.updated_at=updated_at
        
    @classmethod
    def agregarUsuario(cls,nuevoUsuario):
        query = "insert into usuario(nombre,apellido,email,created_at,updated_at) VALUES (%(nombre)s,%(apellido)s,%(email)s,NOW(),NOW());"
        resultado = connectToMySQL("usuario").query_db(query,nuevoUsuario)
        return resultado

    @classmethod
    def listaUsuario(self):
        query = "SELECT* FROM usuario;"
        resultado=connectToMySQL("usuario").query_db(query)
        listaUsuarios = []
        for usuarios in resultado:
            listaUsuarios.append( Usuario( usuarios["nombre"], usuarios["apellido"], usuarios["email"],usuarios["created_at"],usuarios["updated_at"]))
        return listaUsuarios
        
        