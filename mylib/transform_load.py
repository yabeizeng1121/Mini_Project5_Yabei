"""
Transforms and Loads data into the local SQLite3 database
Example:
,general name,count_products,ingred_FPro,avg_FPro_products,avg_distance_root,ingred_normalization_term,semantic_tree_name,semantic_tree_node
"""
import sqlite3
import csv
#import os

#load the csv file and insert into a new sqlite3 database
def load(dataset="/workspaces/sqlite-lab/data/cars.csv"):
    """Transforms and Loads data into the local SQLite3 database"""

    payload = csv.reader(open(dataset, newline=''), delimiter=',')
    conn = sqlite3.connect('GroceryDB.db')
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS CarsDB")
    # Update the columns below based on the structure of cars.csv
    c.execute("CREATE TABLE CarsDB (Brand TEXT, Price REAL, Body TEXT,
    Mileage INTEGER, EngineV REAL, Engine_Type TEXT, Registration TEXT, 
    Year INTEGER, Model TEXT)")
    
    c.executemany(
        "INSERT INTO CarsDB (Brand, Price, Body, Mileage, EngineV, Engine_Type, Registration, Year, Model) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
        payload
    )
    conn.commit()
    conn.close()
    return "GroceryDB.db"

