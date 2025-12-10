import json
import os
from datetime import datetime 

file_name = "tickets.json"

def load_tickets():
    if not os.path.exists(file_name):
      return {}
    
    if os.path.getsize(file_name) == 0:
          return {}

    with open(file_name, "r") as f:
      return json.load(f)
    
def save_tickets(tickets):
  with open(file_name, "w") as f:
    json.dump(tickets, f, indent=4)


class ticket_CRUD:
  @staticmethod
  def get_ticket(ticket_no):
    tickets = load_tickets()
    key = str(ticket_no)
    
    if key not in tickets:
        print("No Pawn Ticket Found\n")
        return None

    return tickets[key]


  @staticmethod
  def display_tickets_table():
      tickets = load_tickets()

      if not tickets:
          print("No Pawn Tickets Found.\n")
          return

      print("\n-------------------------------------------- PAWN TICKET LIST -----------------------------------------------------")
      print(f"{'Ticket No.':<12} {'Customer Name':<20} {'Item':<15} {'Loan':<15}  {'Status':<20} {'Pawn Date':<12} {'Maturity Date':<12}")
      print("-------------------------------------------------------------------------------------------------------------------")

      for ticket_no, data in tickets.items():
          customer = data.get("Customer Name", "")
          item = data.get("Item Type", "")
          loan = data.get("Principal Loan", "")
          status = data.get("Status", "")
          pawn_date = data.get("Pawn Date", "")
          maturity_date = data.get("Maturity Date", "")

          print(f"{ticket_no:<12} {customer:<20} {item:<15} P{loan:<15,.2f} {status:<20} {pawn_date:<12} {maturity_date:<12}")

      print("-------------------------------------------------------------------------------------------------------------------\n")

  
  @staticmethod
  def add_ticket(ticket_no, data):
    tickets = load_tickets()
    tickets[str(ticket_no)] = data
    save_tickets(tickets)
    print(f"\nNew Pawn added. Ticket no. {ticket_no}")
    
  
  @staticmethod
  def update_ticket(ticket_no, maturity_date=None, pawn_date=None, status=None):
      tickets = load_tickets()
      key = str(ticket_no)

      if key not in tickets:
          print("No Pawn Ticket Found!\n")
          return

      if maturity_date is not None:
          tickets[key]["Maturity Date"] = maturity_date
      
      if pawn_date is not None:
          tickets[key]["Pawn Date"] = pawn_date
      
      if status is not None:
          tickets[key]["Status"] = status

      save_tickets(tickets)


  @staticmethod
  def forfeit_updates():
    tickets = load_tickets()
    today = datetime.now().date()
    updated = False
    
    for _, data in tickets.items():
      maturity = datetime.strptime(data["Maturity Date"], "%Y-%m-%d").date()
      
      if data["Status"].startswith("Active") and today > maturity:
        data["Status"] = "Forfeited"
        updated = True
        
    if updated:
        save_tickets(tickets)
    
