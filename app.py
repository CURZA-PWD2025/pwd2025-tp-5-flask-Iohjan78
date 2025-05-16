from flask import Flask
from data.data_productos import productos, categorias

app = Flask (__name__)



@app.route("/home")
def home():
    return "<h1>Hola Mundo!</h1><br><p>Soy Juan Manuel Yurcombich y estoy aprendiendo a utilizar flask! se que es un largo camino el de programador, pero espero pronto ya estar trabajando en este mundillo</p>"

@app.route("/productos")
def listar_productos():
    lista_producto= "<h1>Lista de Productos</h1><br>"
    for producto in productos:
        lista_producto += f"ID: {producto['id']} - Descripcion: {producto['descripcion']} - Categoria ID: {producto['categoria_id']}<br>"
    return lista_producto

@app.route("/categorias")
def listar_categoria():
    lista_categoria = "<h1>Lista de Categorias</h1><br>"
    for categoria in categorias:
        lista_categoria += f"ID: {categoria['id']} - Descripcion: {categoria['descripcion']}<br>"
    return lista_categoria

if __name__ == "__main__":
    app.run(debug=True)