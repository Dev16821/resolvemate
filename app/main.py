from app.agent import generate_support_response
from app.hindsight_adapter import HindsightAdapter
import json

memory_adapter = HindsightAdapter()


def get_required_input(label):
    while True:
        value = input(label).strip()

        if value:
            return value

        print("This field cannot be empty. Try again.")


def load_sample_data():
    with open("data/sample_customers.json", "r") as file:
        customers = json.load(file)

    for customer in customers:
        memory_adapter.retain_memory(
            customer_name=customer["customer_name"],
            issue=customer["issue"],
            resolution=customer["resolution"],
            rejected_solution=customer["rejected_solution"],
            tone=customer["tone"]
        )

    print(f"\nLoaded {len(customers)} sample customers successfully.")

def view_all_memories():
    memories = memory_adapter.get_all_memories()

    if not memories:
        print("\nNo memories stored yet.")
        return

    print("\n=== Stored Memories ===")

    for index, memory in enumerate(memories, start=1):
        print(f"\nMemory {index}")
        print(f"Customer: {memory['customer_name']}")
        print(f"Issue: {memory['issue']}")
        print(f"Resolution: {memory['resolution']}")
        print(f"Rejected Solution: {memory['rejected_solution']}")
        print(f"Tone: {memory['tone']}")


def show_menu():
    print("\n=== ResolveMate ===")
    print("1. Store customer memory")
    print("2. Generate support response")
    print("3. Load sample data")
    print("4. View all memories")
    print("5. Exit")


def main():
    while True:
        show_menu()

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            customer_name = get_required_input("Customer name: ")
            issue = get_required_input("Previous issue: ")
            resolution = get_required_input("Previous resolution: ")
            rejected_solution = get_required_input("Rejected solution: ")
            tone = get_required_input("Preferred tone: ")

            memory_adapter.retain_memory(
                customer_name=customer_name,
                issue=issue,
                resolution=resolution,
                rejected_solution=rejected_solution,
                tone=tone
            )

            print("\nMemory stored successfully.")

        elif choice == "2":
            customer_name = get_required_input("Customer name: ")
            current_issue = get_required_input("Current issue: ")

            response = generate_support_response(
                customer_name=customer_name,
                current_issue=current_issue
            )

            print("\nGenerated Response:")
            print(response)

        elif choice == "3":
            load_sample_data()

        elif choice == "4":
            view_all_memories()

        elif choice == "5":
            print("\nExiting ResolveMate. Goodbye.")
            break

        else:
            print("\nInvalid option. Choose 1, 2, 3, 4, or 5.")


if __name__ == "__main__":
    main()