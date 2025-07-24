{
    "name": "School",
    "version": "18.0.1.0",
    "depends": ["base"],
    "author": "Lekhnath",
    "category": "Education",
    "description": """
        School Management Module
    """,
    "data": [
        "security/ir.model.access.csv",
        "views/school_default_view.xml",
        "views/student/form_view.xml",
        "views/student/tree_view.xml",
        "views/student/kanban_view.xml"
    ],
    "assets": {
        "web.assets_backend": [
            "school/static/css/global.css",
        ]
    },
    "license": "LGPL-3",
    "installable": True,
    "application": True,
}
