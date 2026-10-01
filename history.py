import json

FILE_NAME = "history.json"


def load_history():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_history(history):
    with open(FILE_NAME, "w") as file:
        json.dump(history, file, indent=4)


def add_to_history(expression, result):
    history = load_history()

    history.append({
        "expression": expression,
        "result": result
    })

    save_history(history)


def show_history():
    history = load_history()

    if not history:
        print("No calculation history.")
        return

    print("\n===== HISTORY =====")

    for item in history:
        print(f"{item['expression']} = {item['result']}")