from memory import remember_customer, recall_customer

from memory import remember_customer
from agent import generate_support_response


remember_customer(
    customer_name="Ravi Kumar",
    issue="Wrong food order delivered",
    resolution="Full refund requested",
    rejected_solution="Coupon",
    tone="Apologetic and direct"
)

response = generate_support_response(
    customer_name="Ravi Kumar",
    current_issue="Late delivery"
)

print(response)

memory = recall_customer("Ravi Kumar")

if memory:
    print("Memory found:")
    print(memory)
else:
    print("No memory found.")