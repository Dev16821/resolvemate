from memory import remember_customer, recall_customer

remember_customer(
    customer_name="Ravi Kumar",
    issue="Wrong food order delivered",
    resolution="Full refund requested",
    rejected_solution="Coupon",
    tone="Apologetic and direct"
)

memory = recall_customer("Ravi Kumar")

if memory:
    print("Memory found:")
    print(memory)
else:
    print("No memory found.")