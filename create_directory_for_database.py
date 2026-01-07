import os
from config import config

def create_dir():
    folder_name = f"{config['title']} Database"
    db_dir = rf"C:\ProgramData\{folder_name}"

    if not os.path.exists(db_dir):
        os.makedirs(db_dir)
        print("Directory created successfully")
    else:
        print("Directory already exists")

    return folder_name