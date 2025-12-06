def days_equivalent(days: int):
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
  rate = days_equivalent(days=days)
  if rate == "forfeit":
    return "forfeit"
  else:
    interest = principal * rate
    return interest
  
def print_summary(transaction: str, percentage: int, interest: float, d_principal: int, principal: int = 0, service_fee: float = 0):
    total = principal + interest + service_fee
    print("\n-------------------------------")
    print(f"      {transaction} SUMMARY        ")
    print("-------------------------------")
    print(f" Principal:             P{d_principal:,.2f}")
    print(f" Interest {percentage}:          P{interest:,.2f}")
    if service_fee > 0:
        print(f" Service Fee:            P{service_fee:,.2f}")
    print("-------------------------------")
    print(f" TOTAL:                 P{total:,.2f}")
    print("-------------------------------")
    print("Please pay the Total Amount. Thank you!\n")
  

def renew(principal: int, days: int):
    interest = compute_interest(principal=principal, days=days)

    if interest == "forfeit":
        print("\n⚠ Pawn ticket has exceeded 120 days.")
        print("Item status: FORFEITED\n")
        return

    percent = days_equivalent(days=days)

    print_summary(transaction="RENEWAL", percentage=percent, d_principal=principal, interest=interest, service_fee=10)
    
    
def redeem(principal: int, days: int):
    interest = compute_interest(principal=principal, days=days)

    if interest == "forfeit":
        print("\n⚠ Pawn ticket has exceeded 120 days.")
        print("Item status: FORFEITED\n")
        return

    percent = days_equivalent(days=days)

    print_summary(transaction="REDEEM", percentage=percent, d_principal=principal, principal=principal, interest=interest, service_fee=10)
    
def pay(principal: int, days: int):
    interest = compute_interest(principal=principal, days=days)

    if interest == "forfeit":
        print("\n⚠ Pawn ticket has exceeded 120 days.")
        print("Item status: FORFEITED\n")
        return

    percent = days_equivalent(days=days)

    print_summary(transaction="PAY INTEREST", percentage=percent, d_principal=principal, interest=interest)
  

def main():
  print("------Hellow, Welcome to my PAWN SHOP MEOW!------")
  principal = int(input("Enter Principal Amount: "))
  days = int(input("Enter number of Days after Loan: "))
  
  print("Choose Transaction: ")
  print("A) Pay Interest Only")
  print("B) Renew (Extend Loan)")
  print("C) Redeem (Recover collateral)")
  print("D) Forfeit (Surrender Item)")
  choice = input("Answer: ")
  
  if choice.lower() == "a":
    pay(principal=principal, days=days)
  elif choice.lower() == "b":
    renew(principal=principal, days=days)
  elif choice.lower() == "c":
    redeem(principal=principal, days=days)
  else:
    print("\n-------------------------------")
    print("        ITEM FORFEITED        ")
    print("-------------------------------")
      



if __name__ == "__main__":
    main()