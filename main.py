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
  

def renew(principal: int, days: int):
    interest = compute_interest(principal=principal, days=days)

    if interest == "forfeit":
        print("\n⚠ Pawn ticket has exceeded 120 days.")
        print("Item status: FORFEITED\n")
        return

    percent = days_equivalent(days=days)

    print("\n-------------------------------")
    print("        RENEWAL SUMMARY        ")
    print("-------------------------------")
    print(f" Principal:         P{principal:,.2f}")
    print(f" Interest ({percent}%):  P{interest:,.2f}")
    print(f" + Service Fee:     P10.00")
    print("-------------------------------")
    print(f" TOTAL:             P{interest + 10:,.2f}")
    print("-------------------------------")
    print("Please pay the Total Amount. Thank you!\n")
    
    
def redeem(principal: int, days: int):
    interest = compute_interest(principal=principal, days=days)

    if interest == "forfeit":
        print("\n⚠ Pawn ticket has exceeded 120 days.")
        print("Item status: FORFEITED\n")
        return

    percent = days_equivalent(days=days)

    print("\n-------------------------------")
    print("        RENEWAL SUMMARY        ")
    print("-------------------------------")
    print(f" Principal:           P{principal:,.2f}")
    print(f" + Interest ({percent}%):  P{interest:,.2f}")
    print(f" + Service Fee:       P10.00")
    print("-------------------------------")
    print(f" TOTAL:               P{principal + interest + 10:,.2f}")
    print("-------------------------------")
    print("Please pay the Total Amount. Thank you!\n")
  

def main():
  print("------Hellow, Welcome to my PAWN SHOP MEOW!------")
  princicpal = int(input("Enter Principal Amount: "))
  days = int(input("Enter number of Days after Loan: "))
  
  print("Choose Transation: ")
  print("A) Renew (Extend Loan)")
  print("B) Redeem (Recover collateral)")
  print("C) Forfeit (Surrender Item)")
  choice = input("Answer: ")
  
  if choice.lower() == "a":
    renew(principal=princicpal, days=days)
  elif choice.lower() == "b":
    redeem(principal=princicpal, days=days)
  else:
    print("\n-------------------------------")
    print("        ITEM FORFEITED        ")
    print("-------------------------------")
      



if __name__ == "__main__":
    main()