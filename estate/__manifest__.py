{
    "name": "Estate",
    "version": "18.0.1.0",
    "depends": ["base"],
    "author": "Lekhnath",
    "category": "Education",
    "description": """
        Estate Student Management Module
    """,
    "data": [
        "views/course/form_view.xml",
        "views/course/tree_view.xml",
        "views/student/form_view.xml",
        "views/estate_property_views.xml",
        "security/ir.model.access.csv",
    ],
    "assets": {
        "web.assets_backend": [
            "estate/static/css/global.css"
        ],
    },
    "license": "LGPL-3",
    "installable": True,
    "application": True,
}
