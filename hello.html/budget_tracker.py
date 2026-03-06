import time

def get_budget():
    while True:
        try:
            val = input("💰 Enter your total monthly budget (LKR): ")
            return float(val)
        except ValueError:
            print("❌ Invalid input. Please enter a numerical value for your budget.")

def main():
    print("💸 --- SMART BUDGET TRACKER --- 💸")
    print("Stay on top of your spending! 🚀")
    
    total_budget = get_budget()
    current_balance = total_budget
    expenses = []

    print("\n📝 Start entering your expenses.")
    print("💡 Tip: Type 'done' when you are finished.")

    while True:
        entry = input(f"\n💵 Current Balance: {current_balance:.2f} LKR\n➡️ Enter expense amount (or 'done'): ").strip().lower()
        
        if entry == 'done':
            break
            
        try:
            expense_amount = float(entry)
            if expense_amount < 0:
                print("⚠️ Expenses cannot be negative!")
                continue
                
            expenses.append(expense_amount)
            current_balance -= expense_amount
            
            if current_balance < 0:
                print("🧨 Oh no! You've exceeded your budget!")
            elif current_balance < 500:
                print("⚠️ Warning: Low Funds")
                
        except ValueError:
            print("❌ Please enter a valid number or type 'done'.")

    print("\n" + "="*35)
    print("📊 FINAL BUDGET SUMMARY 📊")
    print("-" * 30)
    print(f"Initial Budget    : {total_budget:.2f} LKR")
    print(f"Total Expenses    : {sum(expenses):.2f} LKR")
    print(f"Remaining Balance : {current_balance:.2f} LKR")
    print("-" * 30)
    
    if current_balance < 0:
        print("🛑 STATUS: OVER BUDGET")
    elif current_balance < 500:
        print("⚠️ STATUS: LOW FUNDS")
    else:
        print("✅ STATUS: HEALTHY")
    
    print("="*35)
    print("Happy saving! 🐷💰")

if __name__ == "__main__":
    main()
