
import json
from pathlib import Path

user_data_file_path = Path(__file__).resolve().parent.parent / "data" / "user_data.json"

if not user_data_file_path.exists():
    print('data folder doesnt exist. Creating one...')
    user_data_file_path.parent.mkdir(parents=True, exist_ok=True)
    print('Creaing the json file...')
    user_data_file_path.write_text("{}\n", encoding="utf-8")
    print('Done!')

def view_user_data():
    """view user json file written by you"""
    with user_data_file_path.open("r", encoding="utf-8") as user_data_file:
        return json.load(user_data_file)

def edit_user_data(edited_user_data: str):
    """Edit the user JSON file with data provided as a JSON string."""
    user_data = json.loads(edited_user_data)

    with user_data_file_path.open("w", encoding="utf-8") as user_data_file:
        json.dump(user_data, user_data_file, indent=2, ensure_ascii=False)
        user_data_file.write("\n")

    return user_data
        