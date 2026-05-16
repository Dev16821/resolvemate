from agent import generate_support_response
from hindsight_adapter import HindsightAdapter

memory_adapter = HindsightAdapter()


def main():
    print("\n=== ResolveMate ===")
    print("1. Store customer memory")
    print("2. Generate support response")

    choice = input("\nChoose an option: ")

    if choice == "1":
        customer_name = input("Customer name: ")
        issue = input("Previous issue: ")
        resolution = input("Previous resolution: ")
        rejected_solution = input("Rejected solution: ")
        tone = input("Preferred tone: ")

        memory_adapter.retain_memory(
            customer_name=customer_name,
            issue=issue,
            resolution=resolution,
            rejected_solution=rejected_solution,
            tone=tone
        )

        print("\nMemory stored successfully.")

    elif choice == "2":
        customer_name = input("Customer name: ")
        current_issue = input("Current issue: ")

        response = generate_support_response(
            customer_name=customer_name,
            current_issue=current_issue
        )

        print("\nGenerated Response:")
        print(response)

    else:
        print("\nInvalid option.")


if __name__ == "__main__":
    main()