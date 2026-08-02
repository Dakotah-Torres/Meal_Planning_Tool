from nicegui import ui
import pandas as pd
from services.sku_lookup import HomeStock
import json



class AppState: 
    def __init__(self):
        self.current_item = None
        self.scanned_stock = []



def app():
    
    state = AppState()
    ui.query('.nicegui-content').classes('p-0')
    
    def build_columns_from_df(df: pd.DataFrame):
        return [
            {'name': col, 'label': col.replace('_', ' ').title(), 'field': col}
            for col in df.columns
        ]
    
    def do_lookup():
        sku = sku_input.value.strip()
        if not sku: 
            ui.notify('Enter a SKU first', type='warning')
            return
        
        state.current_item = HomeStock().look_up_sku(sku)
        
        df = pd.json_normalize(state.current_item)
        
        if not ingredient_table.columns:
            ingredient_table.columns = build_columns_from_df(df)
            ingredient_table.update()
        
        result_label.text = state.current_item.get('product_name', "Unknown item")
        result_label.update()
        
    
    def add_to_table():
        if not state.current_item:
            ui.notify("Look Something up first", type='warning')
            return
        
        state.scanned_stock.append(state.current_item)
        df = pd.json_normalize(state.scanned_stock)
        
        ingredient_table.rows = df.to_dict('records')  # convert back to list-of-dicts for ui.table
        ingredient_table.update() 
        
        state.current_item = None
        sku_input = ''
        sku_input.update()
        result_label = ''
        result_label.update()
        sku_input.run_method('focus')
            
        
        
    def do_import():
        pass
    with ui.column().classes('w-full h-screen p-4'):
        with ui.card():
            with ui.row().classes("w-full item-center"):
                sku_input = ui.input('SKU')
                with ui.column().classes("item-center"):
                    ui.button('Look Up', on_click= lambda: do_lookup())
                    ui.button(icon="add", on_click=lambda: add_to_table())
        
        with ui.card().classes("item-center"):
            result_label = ui.label("Waiting for item...")
        
        with ui.card():
            with ui.row().classes("item-center"):
                ingredient_table = ui.table(columns= [], rows= [], row_key='sku')
                ui.button('Import', on_click=lambda: do_import())
        



