def display_ticket_details(ticket_no, data):
  renewal_date = data.get("Renewal Date")
  print("\n------------------ PAWN TICKET DETAILS -------------------")
  print(f"Ticket Number : {ticket_no}")
  print(f"Customer Name : {data.get('Customer Name')}")
  print(f"Item Type     : {data.get('Item Type')}")
  print(f"Loan Amount   : P{data.get('Principal Loan'):,.2f}")
  print(f"Pawn Date     : {data.get('Pawn Date')}")
  if renewal_date:
    print(f"Renewal Date  : {data.get('Renewal Date')}")
  print(f"Maturity Date : {data.get('Maturity Date')}")
  print(f"Status        : {data.get('Status')}")
  print("----------------------------------------------------------\n")
    
    
def days_equivalent(days: int):
  if days == 0:
    return 0
  if days <= 30:
    return 0.04
  elif days <= 60:
    return 0.08
  elif days <= 90:
    return 0.15
  elif days <= 120:
    return 0.20
  else:
    return "forfeit"


def compute_interest(principal: int, days: int):
  rate = days_equivalent(days)
  if rate == "forfeit":
    return "forfeit"
  else:
    interest = principal * rate
    return interest