import json

def save_data(data, json_name):
    try:
        with open(json_name, 'a', encoding='utf-8') as file_obj2:
            json.dump(data, file_obj2, ensure_ascii=False)
            file_obj2.write("\n")
        file_obj2.close()
    except Exception as e:
        print(e)