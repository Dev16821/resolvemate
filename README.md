# ResolveMate

A customer support memory agent that stores customer complaints, resolutions, rejected solutions, and tone preferences—then recalls that memory to generate better support responses.

## Problem
Customer support teams often forget previous customer complaints, rejected solutions, and customer preferences. This leads to generic responses and repeated customer frustration.

## Solution
ResolveMate remembers customers' past interactions and generates personalized support responses based on their history.

## Features
- **Store Customer Memory**: Save customer issues, resolutions, rejected solutions, and tone preferences
- **Recall Memory**: Retrieve past interactions for any customer
- **Generate Smart Responses**: Get generic responses for new customers, personalized responses for returning customers
- **View All Memories**: Review all stored customer interactions
- **Load Sample Data**: Quickly populate the system with example customer data

## Installation

### Prerequisites
- Python 3.8+

### Setup
```bash
# Clone the repository
git clone <repo-url>
cd resolvemate

# Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

### Run the CLI
```bash
python -m app.main
```

### Menu Options
1. **Store customer memory** - Save a customer's issue, resolution, and preferences
2. **Generate support response** - Get a response tailored to the customer's history
3. **Load sample data** - Populate with 3 example customers
4. **View all memories** - Display all stored customer interactions
5. **Exit** - Close the application

### Example Workflow

**First Interaction (No Memory):**
```
Customer: Ravi Kumar
Issue: Wrong order delivered
→ Agent generates generic response
→ Memory is stored
```

**Later Interaction (With Memory):**
```
Customer: Ravi Kumar
Issue: Late delivery
→ Agent recalls that Ravi rejected coupons before
→ Agent generates refund-focused response (not coupon)
```

## Data Storage
- Memories are stored in `data/memory.json`
- Uses local JSON storage (no database required)
- Sample customers defined in `data/sample_customers.json`

## Project Structure
```
app/
  __init__.py
  main.py              # CLI entry point
  agent.py             # Response generation logic
  memory.py            # Local JSON memory management
  hindsight_adapter.py # Memory adapter layer
  config.py            # Configuration (supports .env)
data/
  memory.json          # Persistent customer memory
  sample_customers.json # Sample data for demo
```

## Requirements
- python-dotenv (for environment configuration)

## Environment Configuration
Create a `.env` file (optional):
```
HINDSIGHT_API_KEY=your_key_here
HINDSIGHT_PROJECT_ID=your_project_id_here
```
Note: Currently using local JSON memory. Hindsight SDK integration is optional for future enhancement.
