from memory import recall_customer


def generate_support_response(customer_name, current_issue):
    memory = recall_customer(customer_name)

    if memory is None:
        return f"""
No previous memory found for {customer_name}.

Draft Response:
Hi {customer_name}, we are sorry for the inconvenience caused. 
We understand your concern regarding {current_issue}. 
Our support team will review this issue and assist you as soon as possible.
"""

    return f"""
Previous memory found for {customer_name}.

Past Issue:
{memory["issue"]}

Past Resolution:
{memory["resolution"]}

Rejected Solution:
{memory["rejected_solution"]}

Preferred Tone:
{memory["tone"]}

Draft Response:
Hi {customer_name}, we sincerely apologize that you are facing another issue.

We noticed that you previously experienced: {memory["issue"]}.
At that time, the preferred resolution was: {memory["resolution"]}.
Since you had rejected: {memory["rejected_solution"]}, we will avoid suggesting that again.

Regarding your current issue: {current_issue}, we will handle this with a {memory["tone"].lower()} approach.
"""