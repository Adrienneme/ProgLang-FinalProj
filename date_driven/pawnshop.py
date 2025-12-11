import random
from datetime import datetime, timedelta
from tickets import load_tickets, ticket_CRUD
from utils import display_ticket_details, compute_interest

tickets = {}
used_tickets = []


def generate_ticket():
    while True:
        ticket = f"{random.randint(0, 9999):04d}"
        if ticket not in used_tickets:
            used_tickets.append(ticket)
            return ticket


def create_pawn():
    print("\n---------- Create Pawn ----------")
    customer = input("Enter Customer Name: ")
    item = input("Enter Item Type: ")
    loan = int(input("Enter Loan Amount: "))
    pawn_date = datetime.now()
    maturity_date = datetime.now() + timedelta(days=120)
    status = "Active"
    
    data = {
            "Customer Name": customer,
            "Item Type": item,
            "Principal Loan": loan,
            "Pawn Date": pawn_date.strftime("%Y-%m-%d"),
            "Maturity Date": maturity_date.strftime("%Y-%m-%d"),
            "Status": status 
            }
    
    ticket_num = generate_ticket()
    ticket_CRUD.add_ticket(ticket_num, data)
    
    global used_tickets, tickets
    tickets = load_tickets()
    used_tickets = list(map(int, tickets.keys()))


def renew(ticket_no, data):
    principal = data.get('Principal Loan')
    pawn = data.get("Renewal Date") or data.get("Pawn Date")

    pawn_date = datetime.strptime(pawn, "%Y-%m-%d").date()
    today = datetime.now().date()

    days_passed = (today - pawn_date).days
    interest = compute_interest(principal, days_passed)
    
    maturity_date = datetime.now() + timedelta(days=120)

    print("\n---------- Renew Pawn ----------")
    print(f"Days Passed:       {days_passed}/120")
    print(f"Interest Due:      P{interest:,.2f}")
    print(f"New Maturity Date: {maturity_date.strftime('%Y-%m-%d')}")
    print("\nService Fee:       P10.00")
    print("--------------------------------")
    
    choice = input("Renew this pawn?(y/n): ")
    if choice.lower() == "y":
        print(f"\nPlease pay the total amount of P{interest + 10} to proceed.")
        ticket_CRUD.update_ticket(
            ticket_no,
            maturity_date=maturity_date.strftime("%Y-%m-%d"),
            pawn_date=datetime.now().strftime("%Y-%m-%d"),
            status="Active (Renewed)"
        )
        print("\nYour Pawn Ticket has been renewed. Thank you!")
    else:
        return
        
    
def redeem(ticket_no, data):
    principal = data.get('Principal Loan')
    pawn = data.get("Renewal Date") or data.get("Pawn Date")
    
    pawn_date = datetime.strptime(pawn, "%Y-%m-%d").date()
    today = datetime.now().date()

    days_passed = (today - pawn_date).days
    interest = compute_interest(principal, days_passed)

    print("\n---------- Redeem Pawn ----------")
    print(f"Days Passed:  {days_passed}/120")
    print(f"Principal:    P{principal:,.2f}")
    print(f"Interest Due: P{interest:,.2f}")
    print("\nService Fee:  P10.00")
    print("---------------------------------")
    choice = input("Redeem this pawn?(y/n): ")
    if choice.lower() == "y":
        print(f"\nPlease pay the total amount of P{principal + interest + 10} to proceed.")
        ticket_CRUD.update_ticket(
            ticket_no,
            status="Redeemed"
        )
        print("\nYour Pawn Ticket has been redeemed. Thank you!")
    else:
        return


def forfeit(ticket_no):
    print("\n---------- Forfeit Item ----------")
    choice = input("Are you sure you want to forfeit your item?(y/n): ")
    if choice.lower() == "y":
        ticket_CRUD.update_ticket(
            ticket_no,
            status="Forfeited"
        )
        print("\nYour Pawn Item has been forfeited. Thank you!")
    else:
        return


def main():
    global tickets, used_tickets
    tickets = load_tickets()
    used_tickets = list(map(int, tickets.keys()))
    
    ticket_CRUD.forfeit_updates()
    
    while True:
        print("\n------ Welcome to MEOW Pawnshop ------")
        print("Choose an Action:")
        print("A) Create New Pawn Ticket")
        print("B) View Existing Pawn Tickets")
        print("C) Exit")
        action = input("Enter action: ")

        if action.lower() == "a":
            create_pawn()
            
        elif action.lower() == "b":
            ticket_CRUD.display_tickets_table()
            ticket = input("Find Ticket Number: ")
            res = ticket_CRUD.get_ticket(ticket)
            
            if not res:
                continue
            else:
                display_ticket_details(ticket, res)
                status = res.get("Status")
                if status == "Active" or status == "Active (Renewed)":
                    print("Choose a Transaction:")
                    print("A) Renew Pawn")
                    print("B) Redeem Pawn")
                    print("C) Forfeit Pawn")
                    print("D) Back to Main Menu")
                    transaction = input("Enter transaction: ")

                    if transaction.lower() == "a":
                        renew(ticket_no=ticket, data=res)

                    elif transaction.lower() == "b":
                        redeem(ticket_no=ticket, data=res)

                    elif transaction.lower() == "c":
                        forfeit(ticket_no=ticket)
                        
                    elif transaction.lower() == "d":
                        continue
                else:
                    print("This Pawn is not Active. No transactions allowed")
                    continue

        elif action.lower() == "c":
            print("Exiting... Goodbye!")
            break


if __name__ == "__main__":
  main()