import json
from pathlib import Path

MEMORY_FILE = Path("./data/memory.json")


def load_memory():
    if not MEMORY_FILE.exists():
        return []

    with open(MEMORY_FILE, "r") as file:
        return json.load(file)


def save_memory(memory):
    with open(MEMORY_FILE, "w") as file:
        json.dump(memory, file, indent=4)


def remember_customer(customer_name, issue, resolution, rejected_solution, tone):
    memory = load_memory()

    memory.append({
        "customer_name": customer_name,
        "issue": issue,
        "resolution": resolution,
        "rejected_solution": rejected_solution,
        "tone": tone
    })

    save_memory(memory)


def recall_customer(customer_name):
    memory = load_memory()

    for item in memory:
        if item["customer_name"].lower() == customer_name.lower():
            return item

    return None

def get_all_memories():
    return load_memory()