# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Videoclub",
    "version": "19.0.1.0",
    "author": "Alejandro Pozo",
    "license": "AGPL-3",
    "website": "https://github.com/alaslibress",
    "category": "Tools",
    "summary": "Modulo de gestion de peliculas para SGE - 2 DAM",
    "description": """
        Modulo Videoclub creado para la asignatura SGE.
        Permite gestionar peliculas, categorias y companias cinematograficas.
        Incluye campos calculados, herencia de modelos y control de permisos.
    """,
    "depends": ["base", "contacts"],
    "data": [
        "security/videoclub_security.xml",
        "security/ir.model.access.csv",
        "views/videoclub.xml",
    ],
    "demo": [],
    "application": True,
    "installable": True,
}
