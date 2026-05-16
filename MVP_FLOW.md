# ResolveMate MVP Flow

## Goal
Build a customer support agent that remembers past customer interactions using Hindsight.

## User Flow

### 1. New Customer Issue
User enters:
- customer name
- issue type
- complaint details
- customer tone

### 2. Memory Recall
ResolveMate checks whether this customer has previous memory.

### 3. Response Generation
If no memory exists:
- generate a normal support reply

If memory exists:
- generate a response using previous issue history, rejected solutions, and preferences

### 4. Memory Save
After the interaction, store:
- customer name
- issue
- resolution
- rejected solution
- tone preference

## Demo Scenario

### First Interaction
Customer: Ravi Kumar  
Issue: Wrong order delivered  
Rejected solution: Coupon  
Preferred resolution: Refund  

Agent gives a support response and stores this memory.

### Second Interaction
Customer: Ravi Kumar  
Issue: Late delivery  

Agent recalls that Ravi rejected coupons earlier and gives a refund-focused response instead.
