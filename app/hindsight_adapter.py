from memory import (
    remember_customer,
    recall_customer
)


class HindsightAdapter:
    def __init__(self):
        pass

    def retain_memory(
        self,
        customer_name,
        issue,
        resolution,
        rejected_solution,
        tone
    ):
        remember_customer(
            customer_name=customer_name,
            issue=issue,
            resolution=resolution,
            rejected_solution=rejected_solution,
            tone=tone
        )

    def recall_memory(
        self,
        customer_name,
        current_issue=None
    ):
        return recall_customer(customer_name)