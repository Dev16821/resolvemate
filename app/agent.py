from hindsight_adapter import HindsightAdapter

memory_adapter = HindsightAdapter()


def generate_support_response(customer_name, current_issue):
    recalled_memory = memory_adapter.recall_memory(
        customer_name=customer_name,
        current_issue=current_issue
    )

    if recalled_memory is None:
        return f"""
No previous memory found for {customer_name}.

Draft Response:
Hi {customer_name}, we are sorry for the inconvenience caused.
We understand your concern regarding {current_issue}.
Our support team will review this issue and assist you as soon as possible.
"""

    return f"""
Previous memory found for {customer_name}.

Recalled Context:
{recalled_memory}

Draft Response:
Hi {customer_name}, we sincerely apologize that you are facing another issue.

Based on your previous interaction, we will avoid repeating solutions that did not work for you.

Regarding your current issue: {current_issue}, we will handle this with your past preferences in mind.
"""