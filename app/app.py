from nicegui import ui

# pretend this came from a query, e.g. session.query(Recipe).all()
rows = [
    {'id': 1, 'name': 'Chicken Stir Fry', 'calories': 450},
    {'id': 2, 'name': 'Overnight Oats', 'calories': 320},
    {'id': 3, 'name': 'Turkey Chili', 'calories': 380},
]

columns = [
    {'name': 'name', 'label': 'Recipe', 'field': 'name', 'sortable': True},
    {'name': 'calories', 'label': 'Calories', 'field': 'calories', 'sortable': True},
]

ui.table(columns=columns, rows=rows, row_key='id')

ui.run()