from flask import current_app, render_template
from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface

from .extensions import appbuilder
from .models import Categoria, Ingrediente


class CategoriaView(ModelView):
    datamodel = SQLAInterface(Categoria)

    label_columns = {
        "nombre": "Nombre",
        "descripcion": "Descripción",
        "activo": "Activo",
        "ingredientes": "Ingredientes",
    }

    list_columns = ["nombre", "descripcion", "activo"]
    show_columns = ["id", "nombre", "descripcion", "activo", "ingredientes"]
    add_columns = ["nombre", "descripcion", "activo"]
    edit_columns = add_columns
    search_columns = ["nombre"]
    order_columns = ["nombre"]


class IngredienteView(ModelView):
    datamodel = SQLAInterface(Ingrediente)

    label_columns = {
        "nombre": "Nombre",
        "categoria": "Categoría",
        "cantidad": "Cantidad",
        "unidad_medida": "Unidad de medida",
        "costo_unitario": "Costo unitario",
        "stock_minimo": "Stock mínimo",
        "fecha_vencimiento": "Fecha de vencimiento",
        "activo": "Activo",
    }

    list_columns = [
        "nombre",
        "categoria",
        "cantidad",
        "unidad_medida",
        "costo_unitario",
        "stock_minimo",
        "fecha_vencimiento",
        "activo",
    ]
    show_columns = ["id"] + list_columns
    add_columns = list_columns
    edit_columns = add_columns
    search_columns = ["nombre", "categoria"]
    order_columns = ["nombre"]


appbuilder.add_view(
    CategoriaView,
    "Módulo Categorías",
    icon="fa-tags",
    category="Inventario",
    category_icon="fa-archive",
)
appbuilder.add_view(
    IngredienteView,
    "Módulo Ingredientes",
    icon="fa-cubes",
    category="Inventario",
)


"""
    Application wide 404 error handler
"""


@current_app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )
